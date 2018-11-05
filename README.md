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

### NGS的CNV calling与肿瘤演化/异质性研究

Study by Song Minfang

* Reference
  * Favero, Francesco, et al. "Sequenza: allele-specific copy number and mutation profiles from tumor sequencing data." Annals of Oncology 26.1 (2014): 64-70.及包文档
  * Jiang, Yuchao, et al. "Assessing intratumor heterogeneity and tracking longitudinal and spatial clonal evolutionary history by next-generation sequencing." Proceedings of the National Academy of Sciences 113.37 (2016): E5528-E5537. 及包文档
  * Burrell, Rebecca A., et al. "The causes and consequences of genetic heterogeneity in cancer evolution." Nature 501.7467 (2013): 338.（相关背景Reivew）
* 研究步骤
  * 软件包文档阅读及相关文献阅读理解
  * 实现bam文件的自动定位（包括GDC下载文件manifest的解析）
  * WES数据的预处理，一个关注点是必须进行GC校正，参考基因组使用GDC官方；另一个关注点是同一个病人可能有不同的样本号，我们只挑选最优的，参阅我之前的笔记[TCGA barcode以及重名过滤](https://www.jianshu.com/p/74c36463a97e)
  * allelic copy number calling的探索与自动化
  * 上一步的结果整理，主要结果数据包括但不仅限于allelic copy number信息，purity，ploidy
  * 肿瘤克隆演化与异质性研究
  * 相关结果的输出与整理

## Noncoding driver mutaiton discovery validation

Study by Zhang jing etc., validate by Sun Gangyu

* 研究步骤
  * 论文背景及一些方法阅读
  * 机器学习相关背景学习与逻辑回归的理解与探究
  * 聚焦问题：使用逻辑回归基于特征进行突变概率计算。目前个人认为问题在于特征的选择、优化与解释上。
  * 探讨与研究问题，并提出解决方案
* 注释项目
  * [ENCODE](https://www.encodeproject.org/)
  * [RoadMap](http://www.roadmapepigenomics.org/)
* 参考资料
  * [三大特征选择策略，有效提升你的机器学习水准](https://www.jiqizhixin.com/articles/2017-10-23-2)
  * [机器学习之（四）特征工程以及特征选择的工程方法](https://blog.csdn.net/boon_228/article/details/51749646)
  * [数据一样，y却不一样的样本该怎么处理？](http://sofasofa.io/forum_main_post.php?postid=1002044)
  * [数据特征 标准化和归一化你了解多少？](https://www.tinymind.cn/articles/1217)
  * [Machine Learning Algorithms: Which One to Choose for Your Problem](https://blog.statsbot.co/machine-learning-algorithms-183cc73197c)
  * [An Introduction to Feature Selection](https://machinelearningmastery.com/an-introduction-to-feature-selection/)
  * [Preparing data for a machine learning model.](https://www.jeremyjordan.me/preparing-data-for-a-machine-learning-model/)


