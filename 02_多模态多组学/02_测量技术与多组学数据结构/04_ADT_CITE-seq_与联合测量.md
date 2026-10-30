# 2.4 ADT、CITE-seq 与联合测量

[AINGS](../../README.md) · [多模态多组学](../README.md) · [本模块目录](README.md)

**ADT（antibody-derived tag，抗体来源标签）**来自带有寡核苷酸标签的抗体。抗体结合目标表位，寡核苷酸标签通过测序读取，进而形成与抗体通道相关的计数。**表位（epitope）**是抗体识别的目标结构。常见应用测量一组细胞表面蛋白，实际覆盖范围由抗体面板和实验设计决定。[R2](https://www.nature.com/articles/nmeth.4380)

ADT 数值受到目标量、抗体结合、实验背景和测序过程的影响。两个通道计数不同，也可能与两种抗体的性质不同有关。将一个抗体通道用于同一实验中的细胞比较，与把不同通道解释成可直接比较的绝对蛋白分子数，具有不同的假设要求。

| 技术或实验组合 | 同一捕获单位的测量 | 形成的典型关系 |
| --- | --- | --- |
| scRNA-seq | RNA | 单模态的细胞表达矩阵 |
| scATAC-seq | 染色质可及性 | 单模态的细胞×区域矩阵 |
| CITE-seq | RNA＋抗体标签 | 同一细胞的 RNA 与选定蛋白标签配对 |
| RNA–ATAC Multiome | RNA＋染色质可及性 | 同一细胞核的转录与可及性配对 |
| TEA-seq | RNA＋表位标签＋染色质可及性 | 同一细胞的三类测量配对 |

技术名称帮助识别大致组合；数据中最终保留的细胞、特征和模态还取决于处理与质控。CITE-seq、TEA-seq 及支持联合数据的模型，分别展示了这些组合的实验与分析方式。[R2](https://www.nature.com/articles/nmeth.4380) [R3](https://elifesciences.org/articles/63632) [R7](https://www.nature.com/articles/s41592-023-01909-9)

---

[上一篇：2.3 scATAC-seq 如何得到一个区域计数](03_scATAC-seq_如何得到一个区域计数.md) · [下一篇：2.5 矩阵、行列坐标与元数据](05_矩阵_行列坐标与元数据.md)
