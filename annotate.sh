#!/bin/bash

SDIR=/Users/nicolelin/biomart/analysis3
DIR=/Users/nicolelin/biomart

python $DIR/replaceunderscore.py $SDIR/ref-biomart.txt $SDIR/u_ref-biomart.txt

python $DIR/calls_txt_to_bed.py $SDIR/calls.txt $SDIR/calls.bed 15
sort-bed $SDIR/calls.bed > $SDIR/sorted_calls.bed

cut -f 1-4 $SDIR/u_ref-biomart.txt > $SDIR/ref-biomart_gene.bed
sort-bed $SDIR/ref-biomart_gene.bed > $SDIR/sorted_ref-biomart_gene.bed

cut -f 1-3,5 $SDIR/u_ref-biomart.txt > $SDIR/ref-biomart_phenotype.bed
sort-bed $SDIR/ref-biomart_phenotype.bed > $SDIR/sorted_ref-biomart_phenotype.bed

cut -f 1-3,6 $SDIR/u_ref-biomart.txt > $SDIR/ref-biomart_mim.bed
sort-bed $SDIR/ref-biomart_mim.bed > $SDIR/sorted_ref-biomart_mim.bed

python $DIR/gff_parsing.py $DIR/DGV.GS.hg38.gff3 $DIR/DGVHG38.bed
sort-bed $DIR/DGVHG38.bed > $DIR/sorted_DGVHG38.bed

bedmap --echo --echo-map-id-uniq $SDIR/sorted_calls.bed $SDIR/sorted_ref-biomart_gene.bed > $SDIR/anno_calls1.bed
bedmap --echo --echo-map-id-uniq $SDIR/anno_calls1.bed $SDIR/sorted_ref-biomart_phenotype.bed > $SDIR/anno_calls2.bed
bedmap --echo --echo-map-id-uniq $SDIR/anno_calls2.bed $SDIR/sorted_ref-biomart_mim.bed > $SDIR/anno_calls3.bed
bedmap --echo --echo-map-id-uniq --fraction-both 0.75 $SDIR/anno_calls3.bed $DIR/sorted_DGVHG38.bed > $SDIR/annotated_calls.bed

python $DIR/get_sampleID.py $SDIR/calls.txt $SDIR/sampleID_calls.bed
sort-bed $SDIR/sampleID_calls.bed > $SDIR/sorted_sampleID_calls.bed

bedmap --echo --echo-map-id-uniq --fraction-both 0.90 --count $SDIR/annotated_calls.bed $SDIR/sorted_sampleID_calls.bed > $SDIR/combined.bed

python $DIR/replace_absolute_value.py $SDIR/combined.bed $SDIR/combined.txt

python $DIR/final_step.py $SDIR/combined.txt $SDIR/sorted_sampleID_calls.bed $SDIR/calls.txt $SDIR/FINAL_ANNOTATED_CALLS.txt
