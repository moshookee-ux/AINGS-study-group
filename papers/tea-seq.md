# TEA-seq：同一细胞的三种测量怎样彼此补充？

[论文与方法](README.md) · [多模态多组学](../02_多模态多组学/README.md) · [方法对照](compare.md)

**Simultaneous trimodal single-cell measurement of transcripts, epitopes, and chromatin accessibility using TEA-seq**<br/>
Swanson E, Lord C, Reading J et al. · *eLife* · 2021<br/>
[论文与图表](https://doi.org/10.7554/elife.63632) · [PubMed](https://pubmed.ncbi.nlm.nih.gov/33835024/) · [开放全文](https://europepmc.org/articles/PMC8034981)

TEA-seq 将转录本、表面蛋白表位与染色质可及性联合测量。它让“多模态”从两张矩阵扩展到三种实验读出，也使样本处理和各模态质量之间的取舍更值得仔细看。

## 先把问题放在桌上

| 项目 | 内容 |
| --- | --- |
| 输入 | 经过相应处理的细胞、抗体标记与联合建库流程 |
| 输出 | 同一细胞的 RNA、ADT 与 ATAC 信息 |
| 核心思路 | 联合测量 transcripts、epitopes 与 chromatin accessibility |

## 沿着方法读

### 1. 顺着实验改进过程阅读

论文从样本制备与 ATAC 测量出发，也介绍了 ICICLE-seq 等相关步骤。把技术开发的阶段与最终三模态流程区分开。

### 2. 各模态用自己的质量指标

RNA 的基因与 UMI、ADT 的信号与背景、ATAC 的片段与富集信息，衡量的是不同测量质量。

### 3. 把互补信息落到细胞上

同一细胞的三种读出可以支持细胞类型与状态的交叉观察。检查哪些结论由单模态已能支持，哪些需要联合信息。

## 找一张图，把关系看清楚

原文 Figure 1 聚焦单细胞 ATAC 样本制备与质量比较。可先读片段、TSS 等质量信息，再沿正文进入三模态测量与联合分析的图。 [对照原文](https://doi.org/10.7554/elife.63632)。

## 读结果时，留意这些信息

- 样本制备改变时，三种读出的质量是否一起变化？
- 低质量细胞的筛选规则是否偏向某一模态或某类细胞？
- 三模态联合结果中，新增模态在哪些细胞群提供了具体区分信息？

## 试着做一件小事

做一张“模态—观测对象—质量指标—可能的背景”四列表，分别填写 RNA、ADT、ATAC，再与 CITE-seq 的两模态版本比较。

## 接着读，也接着写

**回到知识库：** [测量技术与多组学数据结构](../02_多模态多组学/02_测量技术与多组学数据结构/README.md) · [质量控制、预处理与数据表示](../02_多模态多组学/03_质量控制_预处理与数据表示/README.md) · [多模态整合、融合与预训练](../02_多模态多组学/06_多模态整合_融合与预训练/README.md)。

**相邻论文：** [CITE-seq](cite-seq.md) · [WNN](wnn.md) · [MultiVI](multivi.md) · [方法对照](compare.md)。

你也可以补一段解释、一个小例子，或指出尚未想清楚的地方。[分享笔记与问题](https://github.com/moshookee-ux/AINGS-study-group/issues/new?template=01_resource.yml) · [共建指南](../CONTRIBUTING.md)。
