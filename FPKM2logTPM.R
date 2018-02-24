#scripte function : FPKM2TPM
#
#input: FPKM file and column number
#
#output: TPM file
#reference:https://haroldpimentel.wordpress.com/2014/05/08/what-the-fpkm-a-review-rna-seq-expression-units/
#
#sample num:585
#unit:log2(fpkm+1)

##function: convert FPKM to TPM
FPKM2TPM <- function(FPKMmatrix){
  TPMmatrix <- testmatrix
  colNum <-1
  while( colNum <= ncol(testmatrix)){
    sum_FPKM <- sum(testmatrix[,colNum])
    TPMmatrix[,colNum] <- testmatrix[,colNum]/sum_FPKM*10^6
    colNum <- colNum+1
  }
  return(TPMmatrix)
}


#---------section 1: load data ---------
FPKMmatrix <- read.table(
  "TCGA-LUAD.htseq_fpkm.tsv",header = TRUE, sep = "\t",check.names = FALSE
)
save.image("rawlogmatrix") 
#---------section 2: convert log2(fpkm+1) to fpkm-------
Ensembl_ID <- factor(FPKMmatrix[,1])
rawmatrix <- FPKMmatrix[,-1]
testmatrix <- 2^(rawmatrix)-1

#---------section 3:convert fpkm to tpm------------
TPMmatrix <- FPKM2TPM(testmatrix)

#write name
rematrix <- data.frame(Ensembl_ID,TPMmatrix)

save.image("TPMmatrix") 
#---------section 4:tpm2logtpm------------
write.table(rematrix, file = "TCGA-LUAD.htseq_tpm.txt", sep = "\t",
            row.names = FALSE, col.names = TRUE, quote = FALSE)

LOG_TPMmatrix <- log2(TPMmatrix+1)
rematrix <- cbind(Ensembl_ID,LOG_TPMmatrix)
save.image("logTPMmatrix") 
#---------section 5:save result------------
write.table(rematrix, file = "HUGO_TCGA-LUAD.htseq_tpm.txt", sep = "\t",
            row.names = FALSE, col.names = TRUE, quote = FALSE)

