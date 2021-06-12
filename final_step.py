#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 6/11/21

@author: Nicole Lin

1) Parse combined.txt and sampleID_calls.bed
2) Delete sampleID from combined.txt that matches with the
sampleID in sampleID_analysis1_calls.bed in every row
3) Subtract 1 Number of Sample Overlap
4) Displays highest frequency
5) Replaces all blank spaces with "NA"
"""

import sys
f=open(sys.argv[1], "r")
lines=f.readlines()

f1=open(sys.argv[2], "r")
lines1 = f1.readlines()

f2 = open(sys.argv[3],"w")
x=0
y=0

f2.write("sampleID" + "\t" + "chromosome" + "\t" + "start" + "\t" + "stop" + "\t" + "genes" + "\t" + "phenotype_description" + "\t" +
         "mim_morbid_description" + "\t" + "highest_frequency" + "\t" + "number_of_sample_overlap" + "\t" + "sample_overlap" + "\n")

while (x < len(lines)):
    line = lines[x].rstrip()
    line1 = lines1[x].rstrip()
    values = line.split("\t")
    values1 = line1.split("\t")

    chrom, start, stop, state, genes, pheno, mim = values[0], values[1], values[2], values[3], values[4], values[5], values[6]
    frequency, sample_overlap, num_sample_overlap = values[7], values[8], int(values[9])
    sampleID = values1[3]
    
    if (genes == ""):
        genes = "NA"
    if (pheno == ""):
        pheno = "NA"
    if (mim == ""):
        mim = "NA"
        
    if (frequency == ""):
        frequency = "NA"
    else:
        freq = frequency.split(";")
        #print(freq)
        int_frequency = list(map(float, freq))
        int_frequency.sort()
        frequency = str(int_frequency[-1])
        #print(frequency)

    if (num_sample_overlap == 1):
        num_sample_overlap = "0";
        sample_overlap = "NA"
    else:
        num_sample_overlap -=1
        num_sample_overlap = str(num_sample_overlap)
        overlap = sample_overlap.split(";")
        #print(overlap)
        #print(sampleID)
        overlap.remove(sampleID)
        sample_overlap = ';'.join(overlap)
        #print(sample_overlap)

    f2.write(sampleID + "\t" + chrom + "\t" + start + "\t" + stop + "\t" + genes + "\t" + pheno + "\t" + mim + "\t" + frequency + "\t" + num_sample_overlap + "\t" + sample_overlap + "\n")
    x+=1
    
f2.close()
