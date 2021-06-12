#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on 5/28/21

@author: Nicole Lin

Replaces all absolute value delimiters with tab delimeters
"""
import sys
f=open(sys.argv[1], "r")
lines=f.readlines()

f1 = open(sys.argv[2],"w")

for line in lines:
    info = line.replace("|", "\t")

    f1.write(info)

f1.close()


