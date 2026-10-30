from math import log1p, exp
from statistics import mean

# cell_id, donor, split, label, RNA(G1,G2), ATAC(P1,P2)
rows = [
    ("D1_a", "D1", "train", "A", (8, 2), (1, 0)),
    ("D1_b", "D1", "train", "B", (2, 8), (0, 1)),
    ("D2_a", "D2", "train", "A", (6, 4), (1, 0)),
    ("D2_b", "D2", "train", "B", (4, 6), (0, 1)),
    ("D3_a", "D3", "valid", "A", (7, 3), (1, 0)),
    ("D3_b", "D3", "valid", "B", (3, 7), (0, 1)),
    ("D4_a", "D4", "test", "A", (5, 5), (1, 0)),
    ("D4_b", "D4", "test", "B", (5, 5), (0, 1)),
]
labels = ("A", "B")  # A 对应甲，B 对应乙；平分时按此顺序选择

def encode(row, multimodal):
    rna, atac = row[4], row[5]
    total = sum(rna)
    if total <= 0:
        raise ValueError("RNA 总计数必须大于零")
    normalized = [10.0 * value / total for value in rna]
    r = log1p(normalized[0]) - log1p(normalized[1])
    return (r, atac[0] - atac[1]) if multimodal else (r,)

def fit_prototypes(training_rows, multimodal):
    centers = {}
    for label in labels:
        vectors = [
            encode(row, multimodal)
            for row in training_rows if row[3] == label
        ]
        centers[label] = tuple(mean(values) for values in zip(*vectors))
    return centers

def predict(row, centers, multimodal):
    vector = encode(row, multimodal)
    scores = [
        -sum((value - center) ** 2
             for value, center in zip(vector, centers[label]))
        for label in labels
    ]
    # 减最大值提高数值稳定性，不改变 softmax 结果。
    weights = [exp(score - max(scores)) for score in scores]
    probabilities = [weight / sum(weights) for weight in weights]
    selected = max(range(len(labels)), key=lambda index: probabilities[index])
    return labels[selected], probabilities

def metrics(truth, predicted):
    accuracy = sum(y == p for y, p in zip(truth, predicted)) / len(truth)
    per_class_f1 = []
    for label in labels:
        tp = sum(y == label and p == label for y, p in zip(truth, predicted))
        fp = sum(y != label and p == label for y, p in zip(truth, predicted))
        fn = sum(y == label and p != label for y, p in zip(truth, predicted))
        denominator = 2 * tp + fp + fn
        per_class_f1.append(2 * tp / denominator if denominator else 0.0)
    return accuracy, mean(per_class_f1)

training = [row for row in rows if row[2] == "train"]
for multimodal in (False, True):
    name = "RNA+ATAC" if multimodal else "RNA"
    centers = fit_prototypes(training, multimodal)
    print(name, "prototypes", centers)
    for split in ("valid", "test"):
        selected_rows = [row for row in rows if row[2] == split]
        predictions = []
        for row in selected_rows:
            label, probabilities = predict(row, centers, multimodal)
            predictions.append(label)
            print(name, split, row[0], label,
                  [round(p, 4) for p in probabilities])
        accuracy, macro_f1 = metrics(
            [row[3] for row in selected_rows], predictions
        )
        print(name, split,
              "accuracy =", round(accuracy, 4),
              "macro-F1 =", round(macro_f1, 4))

# None 表示 ATAC 未测量；按预先规定的规则退回 RNA 坐标。
full_centers = fit_prototypes(training, multimodal=True)
rna_centers = {
    label: (center[0],) for label, center in full_centers.items()
}
missing_atac = ("D4_a", "D4", "test", "A", (5, 5), None)
label, probabilities = predict(missing_atac, rna_centers, multimodal=False)
print("ATAC missing", label, [round(p, 4) for p in probabilities])
