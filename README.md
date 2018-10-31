# Liulab轮转计划安排

by Shixiang


实验室主页 <http://liuxslab.slst.shanghaitech.edu.cn/>

> 了解实验室一些课题方向，以作参考


## 一些概念

* [参考基因组介绍](https://notes.zz-zigzag.com/2016/10/reference-genome)
* [基因组各版本对应关系](http://www.bio-info-trainee.com/1469.html)
* [生物信息学](https://en.wikipedia.org/wiki/Bioinformatics)
* [肿瘤信息学](https://en.wikipedia.org/wiki/Oncogenomics)
* [癌症免疫治疗](https://en.wikipedia.org/wiki/Cancer_immunotherapy)
* [拷贝数变异](https://en.wikipedia.org/wiki/Copy-number_variation)
* [同义与非同义突变](https://en.wikipedia.org/wiki/Synonymous_substitution)
* [Mutation Signature](https://en.wikipedia.org/wiki/Mutational_signatures)
* [TMB](http://www.globecancer.com/azzx/show.php?itemid=3979)

## 关于CNV的研究

待定


## 关于Neoantigen质量研究

2个方面

### 已发表免疫治疗文献的Neoantigen的详细分析
  * 数据的搜索与下载
  * 预处理与规整
  * 分析特定突变与基因表达（以及它们的抽象，例如模块、网络等）与病人生存关系 - 参考文献：[Signatures of T cell dysfunction and exclusion predict cancer immunotherapy response](https://www.nature.com/articles/s41591-018-0136-1)


### Neoantigen Quality Pipeline

这方面感觉做的人不少了，有些Pipeline已经出来了，技术跟不上，观望观望差不多了。

文献

  * [A neoantigen fitness model predicts tumour response to checkpoint blockade immunotherapy](https://www.nature.com/articles/nature24473)
  * [Signatures of T cell dysfunction and exclusion predict cancer immunotherapy response](https://www.nature.com/articles/s41591-018-0136-1)
  * [Computational pipeline for the PGV-001 neoantigen vaccine trial ](https://www.biorxiv.org/content/biorxiv/early/2017/08/11/174516.full.pdf)
  
流程

  * https://github.com/openvax/neoantigen-vaccine-pipeline
  * https://github.com/rschenck/NeoPredPipe
  * https://github.com/carlomazzaferro/neoantigen
  * https://github.com/ShixiangWang/Variants2Neoantigen
