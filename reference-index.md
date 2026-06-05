# 参考文献索引

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

1. `D:\AI-NGS\耐药检测规范解读.word.docx`
2. `D:\AI-NGS\rawdata解读.docx`

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

1. `D:\AI-NGS\code-V3\文献整理\文献总整理.md`
2. `D:\AI-NGS\code-V3\文献整理\06_working_files\kmer降维与输入模型因果关系整理.md`

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
   本地材料：`D:\AI-NGS\汇报文档\暑期\耐药检测\文献整理\单菌 k-mer+Lasso 耐药检测方法总结.docx`

### 我们已有材料

1. `D:\AI-NGS\耐药检测规范解读.word.docx`
2. `D:\AI-NGS\rawdata解读.docx`
3. `D:\AI-NGS\汇报文档\暑期\耐药检测\文献整理\20260524方法论整理.docx`

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
- 如果某篇文献已经在本地有 PDF 或总结材料，建议在后续版本里补一列“本地路径”。
