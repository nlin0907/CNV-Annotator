#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 6/11/21

@author: Nicole Lin

Reads in calls.txt and outputs file with chromosome, start, stop, and
sampleID as last column (used for bedmap comparison)
"""

import sys
f=open(sys.argv[1], "r")
lines=f.readlines()

f1 = open(sys.argv[2],"w")
x=1

while (x < len(lines)):
    line = lines[x].rstrip()
    values = line.split("\t")
    #print(values)
    sampleID, chromosome, start, stop, state = values[0], values[1], values[2], values[3], values[4]
    chrom = chromosome.replace("chr", "")

    f1.write(chrom + "\t" + start + "\t" + stop + "\t" + sampleID + "\n")
    x+=1
    
f1.close()
