#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/28/21

@author: Nicole Lin

This script parses over the HG38 and/or HG39 GFF3 files and outputs a table
with chromosome, inner_start, inner_end, and frequency
"""

import sys

f=open(sys.argv[1], "r")
lines=f.readlines()

f1 = open(sys.argv[2],"w")
x=0

while (x < len(lines)):
    line = lines[x].rstrip()
    values = line.split("\t")
    #print(values)
    chromosome, info = values[0], values[8]
    chrom = chromosome.replace("chr", "")
    
    #variant_sub_index = info.find('variant_sub_type=')
    #if (variant_sub_index != -1):
        #variant_sub = info[(variant_sub_index + 17):(variant_sub_index + 21)]
        #if variant_sub == "Gain"

    start_index = info.find('inner_start=')
    end_index = info.find('inner_end=')
    outer_end_index = info.find(';outer_end')
    if (start_index != -1):
        inner_start = info[(start_index + 12):(end_index)-1]
    if (end_index != -1):
        inner_end = info[(end_index + 10):(outer_end_index)]
        
    frequency_index = info.find('Frequency=')
    percent_index = info.find('%')
    if (frequency_index != -1):
        frequency = info[(frequency_index + 10):(percent_index)]

    f1.write(chrom + "\t" + inner_start + "\t" + inner_end + "\t" + frequency + "\n")
    x+=1
    
f1.close()
