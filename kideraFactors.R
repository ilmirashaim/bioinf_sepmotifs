library(Peptides)
#n=100
data <- read.csv('data/comp/irzv_1-tv_2_twins.csv', sep='\t',
                 stringsAsFactors = FALSE)

getKideraFactors = function(seq){
    x = sapply(c("helix.bend.pref", "side.chain.size",
            "extended.str.pref", "hydrophobicity", 
            "double.bend.pref", "partial.spec.vol", 
            "flat.ext.pref", "occurrence.alpha.reg",
            "pK.C", "surrounding.hydrop"), kidera, seq = seq)
    x
}
seqs <- data$CDR3.amino.acid.sequence
resMat <- sapply(seqs, getKideraFactors)
resMat <- t(resMat)
res <- data.frame(resMat)
res$seq <- as.character(seqs)
write.table(res[,c(11,1:10)], file='data/kidera/irzv_1-tv_2_twins.csv', sep="\t", quote=FALSE)

hc <- hclust(dist(resMat), "ave")
plot(hc, labels = as.character(seqs))
groups <- cutree(hc,3)
