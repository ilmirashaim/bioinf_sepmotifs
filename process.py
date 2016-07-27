import csv
import os

dataFolder = 'data'
outFolder = 'out'
keys = ['A', 'W', 'I', 'Y', 'G', 'H', 'D', 'F', 'C', 'P', 'Q', 'M', 'V', 'S', 'E', 'K', 'R', 'L', 'N', 'T']
aminoAcidFreqDicts = []

lengths = []
filenames = ['azh.txt', 'yzh.txt', 'gs.txt', 'kb.txt', 'tv.txt', 'irzv.txt']

for filename in filenames:
   aminoAcidFreqDict = dict.fromkeys(keys,0)

   with open(os.path.join(dataFolder, filename), 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter='\t', )
      next(reader)
      sumOfUmicount=0.0

      props = []
      for row in reader:
         sumOfUmicount += float(row[1])
         seq = row[5]

         prop = int(row[0])
         if prop == 0:
            continue

         if prop < 100:
            props.append(prop)

         if '*' in seq or '~' in seq:
            continue
         for s in seq:
            aminoAcidFreqDict[s] = aminoAcidFreqDict[s] + 1

         lengths.append(len(seq))

      # plot of Umo.count
      # plt.figure()
      # plt.plot(props)

   aminoAcidFreqDicts.append(aminoAcidFreqDict)
# plt.show()

print(min(lengths))
print(max(lengths))



# ouput of frequences of each amino acid
freqOut = "freq.csv"
with open(os.path.join(outFolder, freqOut), 'w') as freqOutFile:
   freqOutFile.write(','.join(keys))
   for i in range(len(filenames)):
      freqsForFile = []
      freqOutFile.write("\n")
      for k in keys:
         freqsForFile.append(aminoAcidFreqDicts[i][k])
      sumOfFreqs = sum(freqsForFile)
      freqOutFile.write(', '.join([str(round(x/float(sumOfFreqs),4)) for x in freqsForFile]))

