library(Biobase)
exprs <- as.matrix(read.table(
  "HUGO_matrix.txt", header = TRUE, sep = "\t", check.names = FALSE,row.names=1
))
pData <-  read.table(
  "pData.txt", header = TRUE, sep = "\t", fill=TRUE,row.names=1
)

mySet <- ExpressionSet(assayData=exprs, phenoData=phenoData)
 

all(rownames(pData)==colnames(exprs))
