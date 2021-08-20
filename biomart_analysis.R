library(biomaRt)
ensembl = useMart("ENSEMBL_MART_ENSEMBL", dataset="hsapiens_gene_ensembl", host="grch37.ensembl.org", path="/biomart/martservice")
attributes<-c("chromosome_name", "start_position", "end_position", "external_gene_name", "mim_morbid_description", "phenotype_description")
# gene
# attributes<-c("chromosome_name", "start_position", "end_position", "hgnc_symbol")
# phenotype
# attributes<-c("chromosome_name", "start_position", "end_position", "phenotype_description")
# mim
# attributes<-c("chromosome_name", "start_position", "end_position", "mim_morbid_description")
connection <- file("/Users/nicolelin/analysis3_calls.txt", open="r")
lines <- readLines(connection)

for (i in 2:length(lines)) {
  line = lines[i]
  line_elements <- scan(text=line, what = character(1), sep="\t")
  chrom = line_elements[2]
  chrom_in = sub(".*r", "", chrom)
  start_in = line_elements[3]
  stop_in = line_elements[4]
  results <- getBM(attributes=attributes, filters=c("chromosome_name","start","end"), values=list(chrom_in, start_in, stop_in), mart=ensembl)
  write.table(results, "/Users/nicolelin/ref-biomart_analysis3.txt", append = TRUE, sep = "\t", dec = ".", row.names = FALSE, col.names = FALSE)
}

close(connection)

