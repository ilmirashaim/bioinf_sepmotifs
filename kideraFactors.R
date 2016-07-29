library(Peptides)
n=100
data <- read.csv('data/comp/sorted/irzv_1-tv_2_twins.csv', sep='\t', nrows = n,
                 stringsAsFactors = FALSE)
seqs <- data$CDR3.amino.acid.sequence[1:n]

names <- c("helix.bend.pref", "side.chain.size",
           "extended.str.pref", "hydrophobicity", 
           "double.bend.pref", "partial.spec.vol", 
           "flat.ext.pref", "occurrence.alpha.reg",
           "pK.C", "surrounding.hydrop")

getKideraFactors = function(seq, excludes){
   
    x = sapply(names[!(names%in%excludes)], kidera, seq = seq)
    x
}

getCluster <- function(excludes){
    print(excludes)
    print(names[!(names%in%excludes)])
    excludes <- c(excludes)
    
    resMat <- sapply(seqs, getKideraFactors, excludes=excludes)
    resMat <- t(resMat)
    res <- data.frame(resMat)
    res$seq <- as.character(seqs)
    

    print('computed, now we write vectors to csv')
    
    #write.table(res[,c(11,1:10)], file='data/kidera/irzv_1-tv_2_twins.csv', sep="\t", quote=FALSE)
    
    print('written, now we clusterize')
    hc <- hclust(dist(resMat), "ave")
    plot(hc, labels = as.character(seqs))
    groups <- cutree(hc,5)
    groups
}
hcluserisations <- sapply(c("", "helix.bend.pref", "side.chain.size",
"extended.str.pref", "hydrophobicity", 
"double.bend.pref", "partial.spec.vol", 
"flat.ext.pref", "occurrence.alpha.reg",
"pK.C", "surrounding.hydrop"), getCluster)

