#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/28/21

@author: Nicole Lin

Remove the first column (sampleID) and "chr" before chromosome in preparation
for bedmap which takes chromosome in lexicographic order
"""

#remove first column and "chr" before chromosome

import sys

f=open(sys.argv[1], "r")
lines=f.readlines()

f1 = open(sys.argv[2],"w")

#print(sys.argv[3])
value = sys.argv[3]

x=1

while (x < len(lines)):
    chrom = lines[x].split('\t')[1]
    chromosome = chrom.replace("chr", "")
    start = lines[x].split('\t')[2]
    stop = lines[x].split('\t')[3]
    state = lines[x].split('\t')[4]

    rest = ""
    for y in range(1,int(value)+1):
        rest += "\t" + lines[x].split('\t')[y+4]

    x+=1

    f1.write(chromosome + "\t" + start + "\t" + stop + "\t" + state + rest + "\n")

f1.close()
