import os
import csv
import matplotlib.pyplot as plt
from operator import itemgetter

filenames = ['irzv_1', 'tv_2', 'azh_3', 'yzh_4', 'gs_5', 'kb_6']
twins = [('azh_3', 'yzh_4'), ('gs_5', 'kb_6'), ('irzv_1', 'tv_2')]

fileext = '.csv'

fig = plt.figure()
figuresFolder = os.path.join('out', 'figures')

dataFolder = os.path.join('data', 'comp', 'sorted')

def areTwins(f1, f2):
   return (f1, f2) in twins

def getFilename(f1,f2):
   return f1 + "-" + f2 + ('_twins' if areTwins(f1, f2) else '') + fileext

def sort(filename):
   rows = []
   with open(os.path.join(dataFolder, filename)) as file:
      reader = csv.reader(file, delimiter=' ')
      header = next(reader)
      for row in reader:
         rows.append(row)
   with open(os.path.join(dataFolder, 'sorted', filename), 'w') as file:
      file.write('\t'.join(header) + '\n')
      sorted(rows, key=itemgetter(4))
      for row in rows:
         file.write('\t'.join(row) + '\n')


for i in range(len(filenames)-1):
   for j in range(i, len(filenames)):
      if(i!=j):
         filename = getFilename(filenames[i], filenames[j])
         sort(filename)