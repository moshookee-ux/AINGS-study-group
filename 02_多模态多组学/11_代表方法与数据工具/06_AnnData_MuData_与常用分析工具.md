# 11.6 AnnData、MuData 与常用分析工具

[AINGS](../../README.md) · [多模态多组学](../README.md) · [本模块目录](README.md)

**AnnData**将一张带注释矩阵和相关结果放在同一个数据对象中。一个包含 1,000 个细胞、2,000 个基因的对象，可以采用如下组织：[D5](https://anndata.readthedocs.io/en/stable/generated/anndata.AnnData.html)

| 位置 | 示例形状或内容 | 它保存什么 |
| --- | --- | --- |
| `X` | $1000\times2000$ | 当前主分析矩阵，其尺度由处理流程定义 |
| `obs` | 1,000 行注释 | cell_id、供体、类型、批次、质量指标 |
| `var` | 2,000 行注释 | 基因 ID、名称、参考版本、是否高变 |
| `layers["counts"]` | $1000\times2000$ | 在相同坐标下保存的原始计数 |
| `layers["lognorm"]` | $1000\times2000$ | 同形状的 log 归一化数值 |
| `obsm["X_pca"]` | $1000\times30$ | 每个细胞的 PCA 坐标 |
| `obsm["X_model"]` | $1000\times64$ | 每个细胞的模型表示 |
| `obsp` | 如 $1000\times1000$ | 细胞之间的邻接或距离关系 |
| `uns` | 参数和其他说明 | 处理记录、颜色、模型设置等 |

`obs` 和 `var` 分别绑定行列，`layers` 中的矩阵与当前主矩阵保持同形状。可选的 `raw` 属性保存某个阶段的矩阵及变量信息；里面保存的是否为原始 counts，取决于何时写入。对象字段的名称需要与处理记录结合理解。`.h5ad` 文件以层级存储形式保存 AnnData 中的相关内容。

**MuData**把多个模态的 AnnData 组织起来，例如 RNA 是 $1000\times2000$，ATAC 是 $900\times5000$，再保存它们的观测和变量映射。[D6](https://mudata.scverse.org/en/latest/) 这样既保留各自的特征空间，也能表达某些细胞只有一种模态的情况。

常用工具各自连接不同计算环节：

| 工具 | 主要承担的环节 | 读懂使用流程所需的概念 |
| --- | --- | --- |
| Scanpy | Python 中的质控、变换、降维、近邻和聚类 | counts、特征选择、PCA、图和注释 |
| Seurat | R 中的单细胞与多模态分析 | assay、归一化、整合和 WNN |
| Signac | 染色质可及性分析 | fragment、peak、基因组坐标、TF-IDF 和 LSI |
| scvi-tools | 概率模型的训练、推断和任务接口 | 数据注册、观测分布、潜变量和批次 |
| GEO | 已发表功能基因组研究的数据与描述 | 研究、样本、平台、原始与处理后文件 |

其中 **assay** 是一种实验测量或其数据层次的组织单位；**数据注册**是向模型声明哪些字段保存计数、批次、标签等信息；**accession** 是数据平台用于追踪研究或样本的稳定记录编号。[D1](https://scanpy.readthedocs.io/en/latest/api/generated/scanpy.pp.normalize_total.html) [D3](https://stuartlab.org/signac/articles/pbmc_vignette) [D4](https://satijalab.org/seurat/reference/normalizedata) [D7](https://docs.scvi-tools.org/en/stable/) [D8](https://www.ncbi.nlm.nih.gov/geo/info/overview.html)

---

[上一篇：11.5 scGPT：把测量转换成可以迁移的词元表示](05_scGPT_把测量转换成可以迁移的词元表示.md) · [下一篇：11.7 把一次分析保存成可复用的完整流程](07_把一次分析保存成可复用的完整流程.md)
