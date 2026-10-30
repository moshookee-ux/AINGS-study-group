# 参考资料统一索引

[返回统一入口](README.md) · [路线 A](tracks/clinical-bioinformatics.md) · [路线 B](06_多模态多组学/README.md)

第 1–6 节保留原 AINGS 文献主题与条目，第 8 节接入多模态多组学知识库的完整参考资料，第 9 节保留兴趣小组原稿中的参考社群。条目中的“发起者本地材料”仅为原计划的资源线索，文件尚未提供到本仓库。

这个索引按“学习模块”而不是按发表年份组织，优先服务新成员学习。

每条文献尽量说明它更适合：

- 基础入门
- 方法综述
- 具体工具或前沿论文

## 1. 检验医学与临床微生物学

### 基础读物与综述

1. Jorgensen JH, Ferraro MJ. *Antimicrobial Susceptibility Testing: A Review of General Principles and Contemporary Practices*. Clinical Infectious Diseases, 2009.  
   适合：药敏测试基础入门。  
   链接：[Oxford Academic](https://academic.oup.com/cid/article/49/11/1749/344384/)

2. Burnham JP, Leeds J, Nordmann P, O'Grady J, Patel J. *Diagnosing antimicrobial resistance*. Nature Reviews Microbiology, 2017.  
   适合：理解耐药检测为什么不仅是“测一个基因”。  
   链接：[Nature Reviews Microbiology](https://www.nature.com/articles/nrmicro.2017.37)

3. *Antimicrobial Susceptibility Testing: A Comprehensive Review of Currently Used Methods*.  
   适合：对 KB、MIC、ETEST、自动化方法做横向理解。  
   链接：[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9024665/)

### 我们已有材料

1. `耐药检测规范解读.word.docx`（原发起者本地材料，尚未入库）
2. `rawdata解读.docx`（原发起者本地材料，尚未入库）

## 2. 生物信息学基础

### 基础综述

1. Handelsman J. *Metagenomics: Application of Genomics to Uncultured Microorganisms*. Microbiology and Molecular Biology Reviews, 2004.  
   适合：理解 metagenomics 的基本出发点。  
   链接：[ASM](https://journals.asm.org/doi/10.1128/MMBR.68.4.669-685.2004)

2. Thomas T, Gilbert J, Meyer F. *Metagenomics - a guide from sampling to data analysis*. Microbial Informatics and Experimentation, 2012.  
   适合：对 metagenomics 全流程建立框架。  
   链接：[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC3351745/)

### 物种与新物种判断

1. Jain C, Rodriguez-R LM, Phillippy AM, Konstantinidis KT, Aluru S. *High throughput ANI analysis of 90K prokaryotic genomes reveals clear species boundaries*. Nature Communications, 2018.  
   适合：理解 ANI 和物种边界。  
   链接：[Nature Communications](https://www.nature.com/articles/s41467-018-07641-9)

2. Richter M, Rossello-Mora R. *Shifting the genomic gold standard for the prokaryotic species definition*. PNAS, 2009.  
   适合：理解为什么 16S 不足以完成物种定义。  
   链接：[PNAS](https://www.pnas.org/doi/10.1073/pnas.0906412106)

3. Parks DH et al. *A complete domain-to-species taxonomy for Bacteria and Archaea*. Nature Biotechnology, 2020.  
   适合：理解 GTDB 和系统发育分类。  
   链接：[Nature Biotechnology](https://www.nature.com/articles/s41587-020-0501-8)

## 3. 病原识别与 metagenomic 分类

### 方法综述

1. Breitwieser FP, Lu J, Salzberg SL. *A review of methods and databases for metagenomic classification and assembly*. Briefings in Bioinformatics, 2019.  
   适合：系统看数据库分类、组装、sketch、k-mer 路线。  
   链接：[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6781581/)

2. *Guide to k-mer approaches for genomics across the tree of life*.  
   适合：理解 k-mer 方法为什么在不同任务中用途不同。  
   链接：[arXiv](https://arxiv.org/abs/2404.01519)

### 经典工具与论文

1. Wood DE, Salzberg SL. *Kraken: ultrafast metagenomic sequence classification using exact alignments*. Genome Biology, 2014.  
   适合：数据库匹配分类基础。  
   链接：[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4053813/)

2. Ounit R et al. *CLARK: fast and accurate classification of metagenomic and genomic sequences using discriminative k-mers*. BMC Genomics, 2015.  
   适合：判别性 k-mer 分类思路。  
   链接：[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC4428112/)

3. Kim D et al. *Centrifuge: rapid and sensitive classification of metagenomic sequences*. Genome Research, 2016.  
   适合：压缩索引路线。  
   链接：[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5131823/)

4. Menzel P, Ng KL, Krogh A. *Fast and sensitive taxonomic classification for metagenomics with Kaiju*. Nature Communications, 2016.  
   适合：蛋白层分类思路。  
   链接：[Nature Communications](https://www.nature.com/articles/ncomms11257)

5. Krawczyk PS, Lipinski L, Dziembowski A. *PlasFlow: predicting plasmid sequences in metagenomic data using genome signatures*. Nucleic Acids Research, 2018.  
   适合：k-mer composition / genome signature 路线。  
   链接：[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5887522/)

## 4. 物种鉴定中的深度学习路线

1. Liang Q et al. *DeepMicrobes: taxonomic classification for metagenomics with deep learning*. NAR Genomics and Bioinformatics, 2020.  
   适合：canonical 12-mer + BiLSTM + attention 路线。  
   链接：[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC7671387/)

2. Kretschmer M et al. *BERTax: Taxonomic classification of DNA sequences beyond sequence similarity using deep neural networks*. PNAS, 2022.  
   适合：3-mer + BERT-like + unknown taxa 视角。  
   链接：[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC9436379/)

3. *MetaTransformer: deep metagenomic sequencing read classification using self-attention models*. 2023.  
   适合：sequence token + Transformer 路线。  
   链接：[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC10495543/)

4. Zhao et al. *DSNetax: a deep learning species annotation method based on a deep-shallow parallel framework*. 2024.  
   适合：DNABERT embedding + task head 思路。  
   链接：建议结合本地文献整理和正式期刊页面使用。

### 我们已有材料

1. `文献总整理.md`（原发起者本地材料，尚未入库）
2. `kmer降维与输入模型因果关系整理.md`（原发起者本地材料，尚未入库）

## 5. ARG 与耐药检测

### 基础综述与 benchmark

1. Arango-Argoty G et al. *DeepARG: a deep learning approach for predicting antibiotic resistance genes from metagenomic data*. Microbiome, 2018.  
   适合：ARG 深度学习检测基础。  
   链接：[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6022705/)

2. *Simultaneous detection of pathogens and antimicrobial resistance genes with the open source, cloud-based, CZ ID pipeline*.  
   适合：病原识别与 AMR 模块联动的工程思路。  
   链接：建议后续补正式发表版本或本地 PDF。

### 表型或机制加权路线

1. 单菌 `k-mer + Lasso` 路线  
   适合：理解从纯菌株 WGS 到表型预测的轻量可解释方法。  
   本地材料：`单菌 k-mer+Lasso 耐药检测方法总结.docx`（原发起者本地材料，尚未入库）

### 我们已有材料

1. `耐药检测规范解读.word.docx`（原发起者本地材料，尚未入库）
2. `rawdata解读.docx`（原发起者本地材料，尚未入库）
3. `20260524方法论整理.docx`（原发起者本地材料，尚未入库）

## 6. 数据与统计基础

### 推荐综述

1. Gloor GB et al. *Microbiome Datasets Are Compositional: And This Is Not Optional*. Frontiers in Microbiology, 2017.  
   适合：理解相对丰度、组成型数据问题。  
   链接：[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC5695134/)

2. Davis NM et al. *Simple statistical identification and removal of contaminant sequences in marker-gene and metagenomics data*. Microbiome, 2018.  
   适合：理解污染控制。  
   链接：[PMC](https://pmc.ncbi.nlm.nih.gov/articles/PMC6298009/)

3. Nearing JT et al. *Microbiome differential abundance methods produce different results across 38 datasets*. Nature Communications, 2022.  
   适合：理解为什么统计方法选择会影响结论。  
   链接：[Nature Communications](https://www.nature.com/articles/s41467-022-28034-z)

## 7. 备注

- 本索引优先收“值得做读书会主线”的材料，而不是追求全收集。
- 若后续新增文献，建议在这里先登记，再决定拆到具体模块。
- 如果某篇文献已经在本地有 PDF 或总结材料，建议在材料可公开共享后补充仓库相对链接或稳定来源入口。

## 8. 多模态多组学：完整参考资料与阅读顺序

完整条目、作者、年份与原始链接见[知识库第 13 章](06_多模态多组学/多模态多组学知识库.md#十三参考资料)。以下按阅读目的连接到已有材料，不要求一次读完。

| 想理解什么 | 从哪里读 | 对应知识 |
| --- | --- | --- |
| 生物对象与统计学习 | [生物学与统计学习基础](06_多模态多组学/多模态多组学知识库.md#131-生物学与统计学习基础)、[生物基础与测量流程](06_多模态多组学/多模态多组学知识库.md#136-生物基础与测量流程) | 第 1–4 章；NHGRI、分子生物学教材、统计学习教材 |
| 联合测量与多组学方法 | [测量技术与多组学方法](06_多模态多组学/多模态多组学知识库.md#132-测量技术与多组学方法) | CITE-seq、TEA-seq、WNN、totalVI、MultiVI、GLUE、scVAEIT、MOFA+、scGPT |
| 表示、网络与迁移 | [神经网络与迁移](06_多模态多组学/多模态多组学知识库.md#133-神经网络表示与迁移)、[网络组件与计算效率](06_多模态多组学/多模态多组学知识库.md#137-网络组件优化与计算效率)、[配对学习与连续提示](06_多模态多组学/多模态多组学知识库.md#138-配对学习与连续提示) | VAE、Transformer、Perceiver、图、LoRA、归一化与注意力效率 |
| 评价与统计推断 | [集成、评价与统计推断](06_多模态多组学/多模态多组学知识库.md#134-集成评价与统计推断)、[统计检验、图与可视化](06_多模态多组学/多模态多组学知识库.md#1310-统计检验图与可视化) | 交叉验证、重复、整合评价、校准、FDR、UMAP、Leiden |
| 数据容器与工具 | [官方文档与数据入口](06_多模态多组学/多模态多组学知识库.md#135-官方文档与数据入口) | Scanpy、Seurat、Signac、AnnData、MuData、scvi-tools、GEO |
| 扩展到其他生物问题 | [空间、序列、知识与实验设计](06_多模态多组学/多模态多组学知识库.md#139-空间序列知识与实验设计) | 空间转录组、ESM、CPA、GO、Reactome、RAG、实验选择 |

可以先读第 1–3 章认识测量，再按感兴趣的方法补充第 4–8 章，最后读对应原始论文。开展方法分享时，说明其输入、配对要求、目标和输出，再比较它与自己问题的关系。

## 9. 参考社群与交流方式

兴趣小组原稿列举的 NCI AI Community Group、Bioinformatics & AI XChange、Biolà、Mila Biology + AI Reading Group、PLoB 和集智生物医学大模型读书会，均保留在[小组介绍的参考社群](community.md#参考社群与来源)中。

这些来源提供交流组织方式和主题的参考。具体活动日期、报名与参与方式，以相应主办方页面为准。

## 10. 继续补充资料时

记录标题、作者、年份、原始链接、适合背景和阅读目的。资料暂未提供稳定入口时，保留待补状态；有了可访问的正文、代码或数据后再更新。采用工具或数据库时，在实际学习记录中写明使用版本和日期。
