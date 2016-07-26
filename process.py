import csv
import os
import matplotlib.pyplot as plt
dataFolder = 'data'
outFolder = 'out'
keys = ['A', 'W', 'I', 'Y', 'G', 'H', 'D', 'F', 'C', 'P', 'Q', 'M', 'V', 'S', 'E', 'K', 'R', 'L', 'N', 'T']
dicts = []



filenames = ['azh.txt', 'yzh.txt', 'gs.txt', 'kb.txt', 'tv.txt', 'irzv.txt']

for filename in filenames:
   d = dict.fromkeys(keys,0)

   with open(os.path.join(dataFolder, filename), 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter='\t', )
      next(reader)
      sum_of_umicount=0.0

      props = []
      for row in reader:
         sum_of_umicount += float(row[1])
         seq = row[5]

         prop = int(row[0])
         if prop == 0:
            continue
            
         if prop < 100:
            props.append(prop)

         if seq[0] != 'C':
            print('Achtung')
         if '*' in seq or '~' in seq:
            continue
         for s in seq:
            d[s] = d[s] + 1

      # plot of Umo.count
      plt.figure()
      plt.plot(props)

   dicts.append(d)
plt.show()


# ouput of frequences of each amino acid
freqOut = "freq.csv"
with open(os.path.join(outFolder, freqOut), 'w') as freqOutFile:
   freqOutFile.write(','.join(keys))
   for i in range(len(filenames)):
      freqsForFile = []
      freqOutFile.write("\n")
      for k in keys:
         freqsForFile.append(dicts[i][k])
      sumOfFreqs = sum(freqsForFile)
      freqOutFile.write(', '.join([str(round(x/float(sumOfFreqs),4)) for x in freqsForFile]))

