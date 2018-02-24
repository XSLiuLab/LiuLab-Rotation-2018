#! /usr/bin/python 2.7
#build_phenotype_matrix.py
# -*- coding: utf-8 -*-
"""
build phenotype matrix by TCGA phenotype matrix
need:TCGA phenotype matrix 
Usage:
python build_phenotype_matrix.py [TCGA phenotype matrix] [name_list] [output file]
"""
import sys
from itertools import islice 
if len(sys.argv)<4:
	print'Usage: python '+sys.argv[0]+' [TCGA phenotype matrix] [name_list] [output file]'
	
phenotype_file=open(sys.argv[1],'r')
name_file=open(sys.argv[2],'r')
result_file=open(sys.argv[3],'w')
assy_file=open('pData.txt','w')
id_list=[]
colName_list=[]
phenotype_matrix={}
id_dict={}
##build id list from name list
colName=name_file.readline().strip('\n')
id_list=colName.split('\t')[1:]		#delete the first col
##build phenotype directory from  TCGA phenotype matrix
alllines=phenotype_file.readlines()
colName=alllines[0].strip('\n')
colName_list=colName.split('\t')
phenotype_file.seek(0)
for line in islice(phenotype_file,1,None):
	line=line.strip('\n')
	line_list=line.split('\t')
	geneid=line_list[0]
	matrix={}
	num=0
	for col in colName_list:
		matrix[col]=line_list[num]
		num=num+1
	phenotype_matrix[geneid]=matrix
#
for gene in phenotype_matrix:
	sample_ID=phenotype_matrix[gene]['bcr_sample_barcode']
	id_dict[sample_ID]=gene
##write phenotype data
#write first line
result_file.write('Study_ID'+'\t'+'Sample_ID'+'\t'+'Platform'+'\t'+'Type'+'\t'+'Gender'+'\t'+
					'Age'+'\t'+'Tumor_stage'+'\t'+'Family_history'+'\t'+'Smoking_status'+'\t'+
					'Metastasis_status'+'\t'+'Tumor_feature'+'\t'+'Survival_status'+'\t'+
					'Survival_time'+'\t'+'Preprocessed_method'+'\t'+'Matched_CNV_ID'+'\t'+
					'Tumor_Normal_Matched_ID\n')
for gene in id_list:
	Study_ID="TCGA-LUAD"
	Sample_ID=gene[:15]
	Platform='Illumina'
	Type=phenotype_matrix[Sample_ID]['histological_type']
	Gender=phenotype_matrix[Sample_ID]['gender']
	Age=phenotype_matrix[Sample_ID]['age_at_initial_pathologic_diagnosis']
	Tumor_stage=phenotype_matrix[Sample_ID]['pathologic_stage']
	Family_history=""
	Smoking_status=phenotype_matrix[Sample_ID]['tobacco_smoking_history_indicator']
	Metastasis_status=phenotype_matrix[Sample_ID]['person_neoplasm_cancer_status']
	Tumor_feature=""
	Survival_status=phenotype_matrix[Sample_ID]['vital_status']
	Survival_time=phenotype_matrix[Sample_ID]['days_to_death']
	Preprocessed_method="log2(TPM+1)"
	Matched_CNV_ID=Sample_ID
	Tumor_Normal_Matched_ID=""
	result_file.write(Study_ID+'\t'+Sample_ID+'\t'+Platform+'\t'+Type+'\t'+Gender+'\t'+
					Age+'\t'+Tumor_stage+'\t'+Family_history+'\t'+Smoking_status+'\t'+
					Metastasis_status+'\t'+Tumor_feature+'\t'+Survival_status+'\t'+
					Survival_time+'\t'+Preprocessed_method+'\t'+Matched_CNV_ID+'\t'+
					Tumor_Normal_Matched_ID+'\n')
#
assy_file.write('ID'+'\t'+'Study_ID'+'\t'+'Sample_ID'+'\t'+'Platform'+'\t'+'Type'+'\t'+'Gender'+'\t'+
					'Age'+'\t'+'Tumor_stage'+'\t'+'Family_history'+'\t'+'Smoking_status'+'\t'+
					'Metastasis_status'+'\t'+'Tumor_feature'+'\t'+'Survival_status'+'\t'+
					'Survival_time'+'\t'+'Preprocessed_method'+'\t'+'Matched_CNV_ID'+'\t'+
					'Tumor_Normal_Matched_ID\n')
for gene in id_list:
	Study_ID="TCGA-LUAD"
	Sample_ID=gene[:15]
	Platform='Illumina'
	Type=phenotype_matrix[Sample_ID]['histological_type']
	Gender=phenotype_matrix[Sample_ID]['gender']
	Age=phenotype_matrix[Sample_ID]['age_at_initial_pathologic_diagnosis']
	Tumor_stage=phenotype_matrix[Sample_ID]['pathologic_stage']
	Family_history=""
	Smoking_status=phenotype_matrix[Sample_ID]['tobacco_smoking_history_indicator']
	Metastasis_status=phenotype_matrix[Sample_ID]['person_neoplasm_cancer_status']
	Tumor_feature=""
	Survival_status=phenotype_matrix[Sample_ID]['vital_status']
	Survival_time=phenotype_matrix[Sample_ID]['days_to_death']
	Preprocessed_method="log2(TPM+1)"
	Matched_CNV_ID=Sample_ID
	Tumor_Normal_Matched_ID=""
	assy_file.write(gene+'\t'+Sample_ID+'\t'+Platform+'\t'+Type+'\t'+Gender+'\t'+
					Age+'\t'+Tumor_stage+'\t'+Family_history+'\t'+Smoking_status+'\t'+
					Metastasis_status+'\t'+Tumor_feature+'\t'+Survival_status+'\t'+
					Survival_time+'\t'+Preprocessed_method+'\t'+Matched_CNV_ID+'\t'+
					Tumor_Normal_Matched_ID+'\n')

phenotype_file.close()
name_file.close()
result_file.close()
assy_file.close()