# Rotation Task

## Task1 

**下载TCGA-LUAD数据并转换为TPM格式，绘制histogram**

参考：

- 下载FPKM数据。[下载地址](https://xenabrowser.net/datapages/?dataset=TCGA-LUAD/Xena_Matrices/TCGA-LUAD.htseq_fpkm.tsv&host=https://gdc.xenahubs.net)
- 转换为TPM格式。参考工具<https://github.com/timoast/FPKM-TPM>，可以自己写，最好全部使用R代码。



## Task2

**RNAseq数据归一化，绘制histogram**，结果为矩阵文件，每一行为一个Gene symbol（可能存在转录本到Gene的转换，如果多个转录本映射一个Gene，构建映射方法参数（取最大，最小，中位数？？）），一列为一个样本

只需要做一个转换，TPM值转换为log2(TPM+1)



## Task3

根据基因表达文件创建ExpressionSet对象，同时包含表型数据，表型数据[下载地址](https://xenabrowser.net/datapages/?dataset=TCGA.LUAD.sampleMap/LUAD_clinicalMatrix&host=https://tcga.xenahubs.net)

构建方法参考<http://bioconductor.org/packages/release/bioc/vignettes/Biobase/inst/doc/ExpressionSetIntroduction.pdf>

需要的表型信息我后续补充~~

