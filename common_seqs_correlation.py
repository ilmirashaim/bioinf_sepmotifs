import os
import csv
import matplotlib.pyplot as plt
import scipy.stats as stats
import numpy as np

filenames = ['irzv_1', 'tv_2', 'azh_3', 'yzh_4', 'gs_5', 'kb_6']
twins = [('azh_3', 'yzh_4'), ('gs_5', 'kb_6'), ('irzv_1', 'tv_2')]

fileext = '.csv'

fig = plt.figure()
figuresFolder = os.path.join('out', 'figures')

dataFolder = os.path.join('data', 'comp')

def areTwins(f1, f2):
   return (f1, f2) in twins

def getFilename(f1,f2):
   return f1 + "-" + f2 + ('_twins' if areTwins(f1, f2) else '') + fileext

def getUmis(filename):
   with open(os.path.join(dataFolder, filename)) as file:
      reader = csv.reader(file, delimiter=' ')
      next(reader)
      sums1 = []
      sums2 = []
      for row in reader:
         sum1 = int(row[2])
         sum2 = int(row[3])
         sums1.append(sum1)
         sums2.append(sum2)

   return (sums1, sums2)

def plotUmis(umi1, umi2, k, f1, f2):
   print(f1 + ' ' + f2 + (' twins' if areTwins(f1, f2) else ''))
   ax = fig.add_subplot(3, 5, k, xmargin = 1, ymargin = 1)
   ax.plot(umi1, umi2, 'ro')
   ax.set_xscale('log')
   ax.set_yscale('log')
   ax.set_title('twins' if areTwins(f1, f2) else '')
   # print(stats.spearmanr(umi1, umi2))
   print(stats.pearsonr(umi1, umi2))
   # print(np.corr(umi1,umi2))

k=0
for i in range(len(filenames)-1):
   for j in range(i, len(filenames)):
      if(i!=j):
         k+=1
         filename = getFilename(filenames[i], filenames[j])
         umi1, umi2 = getUmis(filename)
         plotUmis(umi1, umi2, k, filenames[i], filenames[j])

fig.savefig(os.path.join(figuresFolder, 'umis.png'))
plt.close(fig)









