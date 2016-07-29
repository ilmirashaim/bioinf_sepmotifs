library(Peptides)
data <- read.csv('data/azh_1.txt', sep='\t')

getKideraFactors = function(seq){
    x = sapply(c("helix.bend.pref", "side.chain.size",
            "extended.str.pref", "hydrophobicity", 
            "double.bend.pref", "partial.spec.vol", 
            "flat.ext.pref", "occurrence.alpha.reg",
            "pK.C", "surrounding.hydrop"), kidera, seq = seq)
    x
}
    
res <- sapply(data$CDR3.amino.acid.sequence, getKideraFactors)
res <- t(res)
res <- data.frame(res)
res$seq <- as.character(data$CDR3.amino.acid.sequence)
write.table(res[,c(11,1:10)], file='data/kidera/azh_1.txt', sep="\t", quote=FALSE)