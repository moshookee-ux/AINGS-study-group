# DeepARG：怎样把序列相似性变成耐药基因的分类特征？

[论文与方法](README.md) · [检验医学与病原生信](../01_检验医学与病原生信/README.md) · [方法对照](compare.md)

**DeepARG: a deep learning approach for predicting antibiotic resistance genes from metagenomic data**<br/>
Arango-Argoty G, Garner E, Pruden A et al. · *Microbiome* · 2018<br/>
[论文与图表](https://doi.org/10.1186/s40168-018-0401-z) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/29391044/) · [开放全文](https://europepmc.org/articles/PMC5796597)

DeepARG 将序列与已知 ARG 的相似性组织成向量，再交给神经网络判断抗生素耐药类别。这篇文章适合连接数据库、比对特征与机器学习，也帮助厘清基因层面的检测任务。

## 先把问题放在桌上

| 项目 | 内容 |
| --- | --- |
| 输入 | 短 reads 或基因长度的序列、整理后的 ARG 参考库 |
| 输出 | 耐药类别的预测概率 |
| 核心思路 | 序列相似性／距离向量 → 深度分类器；短序列与长序列分别建模 |

## 沿着方法读

### 1. 参考库也属于模型的一部分

论文整理多个 ARG 来源，并利用参考序列构建特征空间。数据库条目、类别与人工整理规则，会影响可学习的边界。

### 2. 特征来自比较结果

DeepARG 使用 DIAMOND 比较得到的 bit-score 信息构造归一化距离表示。网络接收的是相对参考序列的特征向量。

### 3. 读清 SS 与 LS 的用途

DeepARG-SS 面向短序列，DeepARG-LS 面向较长的基因序列。输入长度、特征完整性与训练方式需要对应起来。

## 找一张图，把关系看清楚

原文 Figure 4 展示分类框架。依次寻找参考数据库、序列比较、距离向量和神经网络，给每个箭头写上数据形状或对象类型。 [对照原文](https://doi.org/10.1186/s40168-018-0401-z)。

## 读结果时，留意这些信息

- 按耐药类别查看 precision、recall 与类别不平衡，而不只读一个总准确率。
- 测试序列与参考库、训练集的相似程度怎样控制？近重复序列可能使任务更容易。
- 把预测的耐药类别与样本的药敏表型分开记录；后者还需要宿主、表达和实验测量等信息。

## 试着做一件小事

假设一个序列对四条参考 ARG 的相似性分别为 0.9、0.6、0.1、0.0，写出一个四维距离向量。解释为何参考库更换后，同一序列的特征也可能变化。

## 接着读，也接着写

**回到知识库：** [生物信息学基础](../01_检验医学与病原生信/02_生物信息学基础/README.md) · [方法与模型基础](../01_检验医学与病原生信/04_方法与模型基础/README.md) · [数据与统计基础](../01_检验医学与病原生信/03_数据与统计基础/README.md)。

**相邻论文：** [CZ ID](czid.md) · [DeepMicrobes](deepmicrobes.md) · [decontam](decontam.md) · [方法对照](compare.md)。

你也可以补一段解释、一个小例子，或指出尚未想清楚的地方。[分享笔记与问题](https://github.com/moshookee-ux/AINGS-study-group/issues/new?template=01_resource.yml) · [共建指南](../CONTRIBUTING.md)。
