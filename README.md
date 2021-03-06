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

## 要求

* 代码尽量简洁规范，重要过程留有记录（或是注释，或是用电子笔记本（markdown, Rmarkdown, jupyter notebook etc.））
* 最后结果文件以规范的文本文件（csv，tsv）保存，使用R语言可以采用RData,RDS等压缩文件格式
* 如果存在图片，需要规范出图的数据与代码，尽量保证图片修改比较简单与可自动化
* 第一个月底文献汇报，第二个月月底工作汇报。文献可自己选择，或者进行询问

## 一些重要文献

* Signatures of mutational processes in human cancer - https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3776390/
* Mutation Signature (Nat.Rev) - https://www.nature.com/articles/nrg3729
* Copy-number signatures and mutational processes in ovarian carcinoma - https://www.nature.com/articles/s41588-018-0179-8

## 科学上网

如果无法访问谷歌，请使用XX-net进行上网设置，该软件全平台支持（Mac, Linux and Windows etc.）

* 中文文档：<https://github.com/XX-net/XX-Net/wiki/%E4%B8%AD%E6%96%87%E6%96%87%E6%A1%A3>
* 建议使用谷歌浏览器配置，配置文档为：<https://github.com/XX-net/XX-Net/wiki/%E4%BD%BF%E7%94%A8Chrome%E6%B5%8F%E8%A7%88%E5%99%A8>
* 上述配置成功后，为了保证上网的有效性，需要配置谷歌AppID，即在下方部署服务器部分填入AppID。弄这个很麻烦，可以使用我之前的配置，`adept-box-184316|secret-walker-184316|axial-sight-184316|verdant-art-184316|phonic-jetty-184316|capable-argon-184316|potent-symbol-184316|tribal-primacy-184316|semiotic-cove-184316|plucky-haven-184315`，共10个AppID，每天可以获取10G左右的外网流量。
 ![](https://cloud.githubusercontent.com/assets/5118705/19356731/61e3b1ca-91a1-11e6-85b3-c4e034d99d65.png)
  * 如果想要自己配置，请参考文档<https://github.com/XX-net/XX-Net/wiki/how-to-create-my-appids>


**科学搜索与下载**

* 谷歌学术搜索 - https://scholar.google.com/
* SciHub - http://www.sci-hub.tw/
* 如果上面的失效，使用SCI-Hub科研论文全文下载可用网址（自动更新） - http://tool.yovisun.com/scihub/
* 百度文库下载 - http://wenku.bemfa.com/
* 爱学术 - https://www.ixueshu.com/


## 关于CNV的研究

### CNV断点（breakpoint）精确识别

Study by Sun Gangyu

* References 
  * Korbel, Jan O., et al. "Systematic prediction and validation of breakpoints associated with copy-number variants in the human genome." Proceedings of the National Academy of Sciences 104.24 (2007): 10110-10115.
  * Macintyre, Geoff, et al. "Copy number signatures and mutational processes in ovarian carcinoma." Nature genetics 50.9 (2018): 1262.
* 研究步骤
  * 文献阅读
  * 已有断点识别软件的理解与测试
  * 整合or创新方法
  * 测试数据，评估结果
  
重要概念：

CIGAR

* https://www.drive5.com/usearch/manual/cigar.html
* [What is a CIGAR? ](https://sites.google.com/site/bioinformaticsremarks/bioinfo/sam-bam-format/what-is-a-cigar)
* [Cigar Strings For Dummies](https://jef.works/blog/2017/03/28/CIGAR-strings-for-dummies/)
* [SAM DOC](https://genome.sph.umich.edu/wiki/SAM)
* [SAM doc.pdf](https://samtools.github.io/hts-specs/SAMv1.pdf)
* [生物信息学100个基础问题 —— 第19题 SAM/BAM中的CIGAR值](https://zhuanlan.zhihu.com/p/35574870)


[Sam格式和samtools](http://blog.leanote.com/post/songtaogui/Sam%E6%A0%BC%E5%BC%8F%E5%92%8Csamtools)

### CNV断点（breakpoint）精确识别2

Study by Zhu Xufeng

* novoBreak（<https://github.com/czc/nb_distribution>）的使用，该软件Sun Gangyu已经安装好，目前一个问题是还没有让它work，所以第一步是用几个样本运行出结果，解决不能运行的原因。这个事情可以多余Sun Gangyu交流。



### NGS的CNV calling与肿瘤演化/异质性研究

Study by Song Minfang

* Reference
  * Favero, Francesco, et al. "Sequenza: allele-specific copy number and mutation profiles from tumor sequencing data." Annals of Oncology 26.1 (2014): 64-70.及包文档
  * Jiang, Yuchao, et al. "Assessing intratumor heterogeneity and tracking longitudinal and spatial clonal evolutionary history by next-generation sequencing." Proceedings of the National Academy of Sciences 113.37 (2016): E5528-E5537. 及包文档
  * Burrell, Rebecca A., et al. "The causes and consequences of genetic heterogeneity in cancer evolution." Nature 501.7467 (2013): 338.（相关背景Reivew）
  * Visualizing Clonal Evolution in Cancer https://www.sciencedirect.com/science/article/pii/S1097276516301885
  * Clonal Heterogeneity and Tumor Evolution: Past, Present, and the Future https://www.cell.com/cell/pdf/S0092-8674(17)30066-1.pdf
  * Clonal evolution in cancer https://www.nature.com/articles/nature10762
  * Computational enhancement of single-cell sequences for inferring tumor evolution https://academic.oup.com/bioinformatics/article/34/17/i917/5093219
* 研究步骤
  * 软件包文档阅读及相关文献阅读理解
  * 实现bam文件的自动定位（包括GDC下载文件manifest的解析）
  * WES数据的预处理，一个关注点是必须进行GC校正，参考基因组使用GDC官方；另一个关注点是同一个病人可能有不同的样本号，我们只挑选最优的，参阅我之前的笔记[TCGA barcode以及重名过滤](https://www.jianshu.com/p/74c36463a97e)
  * allelic copy number calling的探索与自动化
  * 上一步的结果整理，主要结果数据包括但不仅限于allelic copy number信息，purity，ploidy
  * 肿瘤克隆演化与异质性研究
  * 相关结果的输出与整理

### NGS的CNV calling流程构建

Study by Wang Xuan

* 在Song Minfang研究的基础上构建CNV calling的代码流程，参考FACETS文献和软件说明
* 分析TCGA NSCLC WES数据



