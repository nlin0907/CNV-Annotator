# CNV Annotator

CNV Annotator is a compilation of programs and scripts used to annotate CNVs from CoNIFER calls.txt output

## Usage
Steps:
1) Set up directory and install BEDOPS
```python
mkdir annotator
``` 
This directory should contain biomart_analysis.R, annotate.sh, calls_txt_to_bed.py, final_step.py, get_sampleID.py, gff_parsing.py, replace_absolute_value.py, and replaceunderscore.py

2) Within directory, 
for GFF3 file in HG38:
```console
 foo@bar:~$ wget http://dgv.tcag.ca/dgv/docs/DGV.GS.hg38.gff3
```
for GFF3 file in HG37:
```console
 foo@bar:~$ wget http://dgv.tcag.ca/dgv/docs/DGV.GS.March2016.50percent.GainLossSep.Final.hg19.gff3
```
3) Make sub-directories in the annotator directory for different analyses (i.e. analysis1, analysis2) and place calls.txt from CoNIFER in respective sub-directories
4) Run biomart_analysis.R on each calls.txt for gene, phenotype description, and MIM morbid description and place ref-biomart.txt (biomart_analysis.R output file) in respective sub-directories. Depending on how your calls.txt file is formatted, you might have to change chrom = line_elements[2] to chrom = line_elements[1], start_in = line_elements[3] to start_in = line_elements[2], and stop_in = line_elements[3] to stop_in = line_elements[2]
IMPORTANT NOTE:
To use HG38 ensembl genes, replace the following line
```python
ensembl = useMart("ENSEMBL_MART_ENSEMBL", dataset="hsapiens_gene_ensembl", host="grch37.ensembl.org", path="/biomart/martservice")
```
with
```python
ensembl = useMart("ENSEMBL_MART_ENSEMBL", dataset="hsapiens_gene_ensembl", host="www.ensembl.org")
```
5) Modify annotate.sh:
Replace lines 3 and 4 
```bash 
SDIR=/Users/nicolelin/annotator/analysis3
DIR=/Users/nicolelin/annotator
```
with your own paths. SDIR is path to sub-directory (aka your different analyses). DIR is path to annotator directory.

If your calls.txt file is not in the format of sampleID, chromosome, start, end, type and has extra columns, replace the number on line 8 with the number of extra columns you have. i.e. If you have a calls.txt file with the columns sampleID, chromosome, start, end, type, variant_type, unique, ID, then change 
```bash
python $DIR/calls_txt_to_bed.py $SDIR/calls.txt $SDIR/calls.bed 15
```
to
```bash
python $DIR/calls_txt_to_bed.py $SDIR/calls.txt $SDIR/calls.bed 3
```

If you want to use HG38 GFF3 file, replace lines 20, 21, and 26 with
```bash
python $DIR/gff_parsing.py $DIR/DGV.GS.hg38.gff3 $DIR/DGVHG38.bed
sort-bed $DIR/DGVHG38.bed > $DIR/sorted_DGVHG38.bed

bedmap --echo --echo-map-id-uniq --fraction-both 0.75 $SDIR/anno_calls3.bed $DIR/sorted_DGVHG38.bed > $SDIR/annotated_calls.bed
```

Now, you're ready to activate the bash script.

6) Give permissions to bash script:
```console
foo@bar:~$ chmod u+x annotate.sh
```
7) Run annotate.sh:
```console
./annotate.sh
```
8) The final calls should be located in your sub-directory called FINAL_ANNOTATED_CALLS.txt


