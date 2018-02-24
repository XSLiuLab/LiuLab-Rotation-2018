#! /usr/bin/python 2.7
#print_gene.py
# -*- coding: utf-8 -*-
"""
build HUGO matrix by normalized count matrix
need:HUGO gene symbol list 
Usage:
python print_gene.py [count matrix] [HUGO_gene_list] [output file]
"""

import sys
from itertools import islice 
if len(sys.argv)<4:
	print'Usage: python '+sys.argv[0]+' [count matrix] [HUGO_gene_list] [output file]'

count_matrix=open(sys.argv[1],'r')
HUGO_ID_list=open(sys.argv[2],'r')
result_file=open(sys.argv[3],'w')
tpm_count={}
all_row=count_matrix.readlines()
firstline=all_row[0]
count_matrix.seek(0)
for line in count_matrix:
	name=line.strip('\n').split()[0]
	tpm_count[name]=line.strip('\n').split()[1:]

row_Num=1
skip_row_Num=1
for row in islice(HUGO_ID_list,skip_row_Num,None):
	if row_Num>0:
		row_Num=row_Num-1
		result_file.write(firstline)		
	ID=row.strip('\n').split()[0]
	empty=['0']*585
	count_line=tpm_count.get(ID,empty)
	#result_file.write(ID+'\t'+'\t'.join(map(str, count_line))+'\n')
	result_file.write(ID+'\t'+'\t'.join(count_line)+'\n')

	
count_matrix.close()
HUGO_ID_list.close()
result_file.close()
