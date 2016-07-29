library(Peptides)
n=100
data <- read.csv('data/azh_1.txt', sep='\t', nrows= n,
                 stringsAsFactors = FALSE)

getKideraFactors = function(seq){
    x = sapply(c("helix.bend.pref", "side.chain.size",
            "extended.str.pref", "hydrophobicity", 
            "double.bend.pref", "partial.spec.vol", 
            "flat.ext.pref", "occurrence.alpha.reg",
            "pK.C", "surrounding.hydrop"), kidera, seq = seq)
    x
}
seqs <- data$CDR3.amino.acid.sequence[1:n]
resMat <- sapply(seqs, getKideraFactors)
resMat <- t(resMat)
res <- data.frame(resMat)
res$seq <- as.character(seqs)
#write.table(res[,c(11,1:10)], file='data/kidera/azh_1.txt', sep="\t", quote=FALSE)

hc <- hclust(dist(resMat), "ave", labels = as.character(seqs))
plot(hc)