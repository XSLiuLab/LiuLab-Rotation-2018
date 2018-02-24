#! /usr/bin/python 2.7
#annotation_ensembl.py
# -*- coding: utf-8 -*-
"""
add annotation for ensembl ID
need:gene symbol list /ensembl_ID gene_symbol/
Usage:
python annotation_ensembl.py [TCGA_ensembl_ID file.csv] [gtf_name list] [output file]
python annotation_ensembl.py LUAD_ID.txt GRCh38.80.csv result.tsv
"""

import sys,csv,re,itertools

if len(sys.argv)<4:
	print'Usage: python '+sys.argv[0]+' [TCGA_ensembl_ID file] [ID_name list.csv] [output file]'
TCGA_file=open(sys.argv[1])
#TCGA_file=open('LUAD_ID.txt')
ID2name_index_file=open(sys.argv[2],'rb')
#ID2name_index_file=open('GRCh38.80.csv','rb')
ID2name_index_lines=ID2name_index_file.readlines()
gene_list={}
outfile=open(sys.argv[3],'w')
skip_row_Num=1
row_Num=0
#build gene_list directory
for line in ID2name_index_lines:
	line=line.strip('\n')
	ensembl_ID=line.split(',')[0]
	gene_name=line.split(',')[1]
	gene_list[ensembl_ID]=gene_name
	row_Num=row_Num+1

print row_Num
for row in itertools.islice(TCGA_file,skip_row_Num,None):
	rowID=row.strip('\n').split()
	ID=rowID[0].split('.')[0]
	gene_name=str(gene_list.get(ID,'NA'))
	if gene_name=='NA':
		gene_name=ID
	outfile.write(ID+'\t'+gene_name+'\n')
	#outfile.close()
TCGA_file.close()
outfile.close()
ID2name_index_file.close()