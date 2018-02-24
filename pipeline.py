step1:	generate genename.list
	>awk 'BEGIN { OFS=","} {if(!/^#/) print $10,$14}' Homo_sapiens.GRCh38.80.gtf|uniq -w 18 |awk '{ gsub(/\"||\;/, ""); print }'  >GRCh38.80.csv
step2:	get id list
	>awk '{print $2 }' HUGO_GENES_ALL_20180101.txt >HUGO_id.txt
step3:	annotation ensembl id 
	>awk '{print $1 }' TCGA-LUAD.htseq_fpkm.tsv >LUAD_ID.txt
	#annotation_ensembl.py : annotation gene symbol for TCGA TPM matrix by gtf file(filter from UCSC)
	>python annotation_ensembl.py LUAD_ID.txt GRCh38.80.csv TCGA_id_annotation.txt
	##output: TCGA_id_annotation.txt
step4: convert FPKM to logTPM matrix
	>Rscript tpm2logtpm.R
	##output: HUGO_TCGA-LUAD.htseq_tpm.txt
step5: filter logTPM matrix
	>python print_gene.py HUGO_TCGA-LUAD.htseq_tpm.txt HUGO_id.txt HUGO_matrix.txt
	##output: HUGO_matrix.txt
step6:	build phenotype matrix
	>python build_phenotype_matrix.py LUAD_clinicalMatrix TCGA-LUAD.htseq_fpkm.tsv HUGO_phenotype.txt
	##output: HUGO_phenotype.txt (the first col is TCGA-LUAD)
	##		pData.txt (the first col is patients' id )
step7:	buid expressionSet
	>Rscript expressionset.r