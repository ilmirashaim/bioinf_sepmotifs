import csv
import os
import pandas
import matplotlib.pyplot as plt

dataFolder = 'data'
outFolder = 'out'
keys = ['A', 'W', 'I', 'Y', 'G', 'H', 'D', 'F', 'C', 'P', 'Q', 'M', 'V', 'S', 'E', 'K', 'R', 'L', 'N', 'T']
aminoAcidFreqDicts = []

lengths = []
filenames = ['azh.txt', 'yzh.txt', 'gs.txt', 'kb.txt', 'tv.txt', 'irzv.txt']


def print_dict(dictionary, formatStr):
   for item in keys:
      stritem = ''
      for s in dictionary[item]:
         stritem += formatStr%(s) + '  '
      print(item, ": ", stritem)

def return_proc(dictionary, counter):
   dictionary_proc = {}
   for k in keys:
      dictionary_proc[k] = [dictionary[k][i]/float(counter[i]) for i in range(len(counter))]
   return dictionary_proc

def plot_nucleocounts(dictionary):
   plt.figure()
   df2 = pandas.DataFrame(dictionary)
   ax = df2.plot(kind='bar', stacked=True)
   ax.legend(bbox_to_anchor=(1.1, 1.05))


for filename in filenames:
   nucleoplaces = dict.fromkeys(keys,0)
   for nuc in nucleoplaces:
      nucleoplaces[nuc] = [0]*22

   nucleocounter = [0]*22

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

         if '*' in seq or '~' in seq:
            continue

         if prop < 100:
            props.append(prop)

         place = 0
         for s in seq:
            aminoAcidFreqDict[s] = aminoAcidFreqDict[s] + 1

            nucleoplaces[s][place] += 1
            nucleocounter[place] += 1
            place += 1

         lengths.append(len(seq))

         # plot of Umo.count
         # plt.figure()
         # plt.plot(props)

   aminoAcidFreqDicts.append(aminoAcidFreqDict)

   print(filename)
   print(nucleocounter)
   print_dict(nucleoplaces, "%7d")
   nucleoprocs = return_proc(nucleoplaces,nucleocounter)
   print_dict(nucleoprocs, "%.2f")

   plot_nucleocounts(nucleoprocs)
plt.show()

print(max(lengths))
print(min(lengths))

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
