import csv
import os
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

keys = ['A', 'W', 'I', 'Y', 'G', 'H', 'D', 'F', 'C', 'P', 'Q', 'M', 'V', 'S', 'E', 'K', 'R', 'L', 'N', 'T']

filenames = ['azh_1.txt', 'yzh_2.txt', 'gs_3.txt', 'kb_4.txt', 'tv_5.txt', 'irzv_6.txt']

dataFolder = 'data'
outFolder = 'out'
figuresFolder = 'figures'
i=0
fig = plt.figure()

for filename in filenames:
   i+=1
   with open(os.path.join(dataFolder, filename), 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter='\t', )
      next(reader)

      lengths = []
      umiProps = []

      for row in reader:

         seq = row[5]

         prop = int(row[0])

         if prop == 0:
            continue

         if '*' in seq or '~' in seq:
            continue


         lengths.append(len(seq))
         umiProps.append(float(row[1]))

      ax = fig.add_subplot(320+i)
      ax.plot(lengths, umiProps, 'ro')
      ax.set_ylim([0,0.01])
      print(filename)
      print(stats.pearsonr(lengths, umiProps))

# plt.show()
fig.savefig(os.path.join(outFolder, figuresFolder, 'length_vs_umi.png'))
plt.close(fig)
