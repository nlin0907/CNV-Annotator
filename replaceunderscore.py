#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/28/21

@author: Nicole Lin

Replace all spaces with underscores in phenotype description
and MIM borbid description
"""

import sys
f=open(sys.argv[1],"r")
lines=f.readlines()
chrom = ""
chromosome_name = ""
start = ""
stop = ""
gene = ""
phenotype = ""
mim = ""

f1 = open(sys.argv[2],"w")
x=0

while (x < len(lines)):
    chrom = lines[x].split('\t')[0]
    if (chrom[0] == "\""):
        chromosome_name = chrom.replace("\"", "")
    else:
        chromosome_name = chrom

    start = lines[x].split('\t')[1]
    stop = lines[x].split('\t')[2]
    gene = lines[x].split('\t')[3]
    phenotype = lines[x].split('\t')[4]
    mim = lines[x].split('\t')[5]
    gene_no_quotes = gene[1:-1]
    
    underscore_phenotype = phenotype.replace(" ", "_")
    if (underscore_phenotype[0] == "\""):
        pheno_no_quotes = underscore_phenotype.replace("\"", "")
    else:
        pheno_no_quotes = underscore_phenotype
        
    underscore_mim = mim.replace(" ", "_")
    if (underscore_mim[0] == "\""):
        mim_no_quotes = underscore_mim.replace("\"", "")
    else:
        mim_no_quotes = underscore_mim

    x+=1

    f1.write(chromosome_name + "\t" + start + "\t" + stop + "\t" + gene_no_quotes + "\t" + pheno_no_quotes + "\t" + mim_no_quotes)

f1.close()
        
