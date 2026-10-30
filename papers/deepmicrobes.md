# DeepMicrobes：短序列的分类信息，能否由网络学出来？

[论文与方法](README.md) · [检验医学与病原生信](../01_检验医学与病原生信/README.md) · [方法对照](compare.md)

**DeepMicrobes: taxonomic classification for metagenomics with deep learning**<br/>
Liang Q, Bible PW, Liu Y et al. · *NAR Genomics and Bioinformatics* · 2020<br/>
[论文与图表](https://doi.org/10.1093/nargab/lqaa009) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33575556/) · [开放全文](https://europepmc.org/articles/PMC7671387)

DeepMicrobes 把短序列转成 k-mer 序列，再学习用于分类的表示。它也引入来自组装基因组的参考信息，适合连着数据库方法一起读，比较显式匹配与监督学习各自使用了什么。

## 先把问题放在桌上

| 项目 | 内容 |
| --- | --- |
| 输入 | DNA reads、用于训练的参考序列及分类标签 |
| 输出 | 预定义分类集合中的类别概率 |
| 核心思路 | canonical 12-mer embedding → 双向 LSTM → 自注意力 → 分类 |

## 沿着方法读

### 1. 数清 token 的数量

长度为 L 的序列按步长 1 切分，形成 L−12+1 个 12-mer。canonical 表示把序列与反向互补的关系纳入词表设计。

### 2. 看上下文怎样被聚合

embedding 为 token 提供向量，双向 LSTM 组织前后文，自注意力再聚合与分类有关的信息。三者各承担不同计算。

### 3. 回到训练参考的构成

训练标签、参考基因组和样本来源决定模型见过什么。增加未培养微生物的基因组信息，会改变可学习的分类覆盖。

## 找一张图，把关系看清楚

原文 Figure 1 的网络部分适合从下到上重画：先标 token 轴，再标 embedding 维度，接着标 LSTM 与注意力怎样把变长序列变成可分类的表示。 [对照原文](https://doi.org/10.1093/nargab/lqaa009)。

## 读结果时，留意这些信息

- 测试序列是否来自训练中出现的基因组、近缘菌株或独立来源？
- 低置信度和数据库外对象怎样处理？输出概率对应哪些已学习类别？
- 除平均准确率外，查看稀少类别、序列长度和真实样本中的表现。

## 试着做一件小事

写出一段长度 20 的序列能形成多少个 12-mer，并画出“token 数 × embedding 维度”的张量。再说明这个张量与最终类别向量有何不同。

## 接着读，也接着写

**回到知识库：** [方法与模型基础](../01_检验医学与病原生信/04_方法与模型基础/README.md) · [神经网络、Transformer与生物表示](../02_多模态多组学/05_神经网络_Transformer与生物表示/README.md) · [下游任务、迁移与预测方法](../02_多模态多组学/07_下游任务_迁移与预测方法/README.md)。

**相邻论文：** [Kraken 2](kraken2.md) · [BERTax](bertax.md) · [scGPT](scgpt.md) · [方法对照](compare.md)。

你也可以补一段解释、一个小例子，或指出尚未想清楚的地方。[分享笔记与问题](https://github.com/moshookee-ux/AINGS-study-group/issues/new?template=01_resource.yml) · [共建指南](../CONTRIBUTING.md)。
