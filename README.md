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

根据基因表达文件创建ExpressionSet对象（样例对象已添加，使用Rstudio打开之前安装好Biobase包），同时包含表型数据，表型数据[下载地址](https://xenabrowser.net/datapages/?dataset=TCGA.LUAD.sampleMap/LUAD_clinicalMatrix&host=https://tcga.xenahubs.net)

构建方法参考<http://bioconductor.org/packages/release/bioc/vignettes/Biobase/inst/doc/ExpressionSetIntroduction.pdf>

表型数据需要构建的一些变量：

```R
#       1. Study_ID, like GSEXXXXX     如果分析TCGA LUAD， 写为TCGA-LUAD
#       2. Sample_ID, like GSMXXXXX    TCGA可以写15位还是12位的Tumor_Sample_Barcode
#       3. Platform, like GPL96 or GPL570   找一些TCGA是什么平台测序的
#       4. Type, tell the tissue type, such as Normal, LUAD ..  # 癌症的组织学类型
#       5. Gender
#       6. Age
#       7. Tumor_stage       
#       8. Family_history     # 家族病史
#       9. Smoking_status      
#       10. Metastasis_status  # 癌症转移状态
#       11. Tumor_feature      # 癌症一些特征，存一些其它变量没有保存的信息
#       12. Survival_status    # 生存状态
#       13. Survival_time      # 生存时间
#       14. Preprocessed_method # 预处理方法，这里可以写为log(TPM+1)
#       15. Matched_CNV_ID     # 匹配的CNV数据ID，TCGA数据可直接可以写为Sample_ID
#       16. Tumor_Normal_Matched_ID # 如果是某病人癌症组织和癌旁组织，设定ID，TCGA少有，直接留空
```

参考构建函数建立表型数据框，没有的变量留空即可：

```R
construct_PhenoData <- function(Study_ID=NULL, Sample_ID=NULL, Platform=NULL, Type=NULL,
                                Gender=NA, Age=NA, Tumor_stage=NA, Family_history=NA,
                                Smoking_status=NA, Tumor_feature=NA, Mutation_status=NA, Survival_status=NA,
                                Survival_time=NA, Preprocessed_Method="RMA", Matched_CNV_ID=NA,
                                Tumor_Normal_Matched_ID=NA){
    dat <- data.frame(Study_ID=Study_ID, Sample_ID=Sample_ID, Platform=Platform, Type=Type,
                      Gender=Gender, Age=Age, Tumor_stage=Tumor_stage, Family_history=Family_history,
                      Smoking_status=Smoking_status, Tumor_feature=Tumor_feature,
                      Mutation_status=Mutation_status, Survival_status=Survival_status,
                      Survival_time=Survival_time, Preprocessed_Method=Preprocessed_Method,
                      Matched_CNV_ID=Matched_CNV_ID, Tumor_Normal_Matched_ID=Tumor_Normal_Matched_ID,
                      stringsAsFactors = FALSE)
    return(dat)
}
```



不像仓库里的样例数据的特征数据行名（以及第一列）是特征ID，这里你全设置为基因名（gene symbol)。同时需要注意，ExpressionSet对象assayData槽中表达矩阵的行名跟它必须是一致的，不然构建对象应该会出错。

这里统一设置为[HUGO gene symbol官网](https://www.genenames.org/cgi-bin/statistics)提供的数据，也就是先构建一个空矩阵，行名为Complete HGNC dataset里Hugo gene symbol的名称，文件我直接传到仓库，你克隆或者git pull下载即可。



**要求**：流程都尽量函数化，主要是FPKM到TPM转换，以及TPM表达值加临床数据构建ExpressionSet对象。参考函数标准<https://github.com/yihui/rmini/blob/master/R/roxygen.R>