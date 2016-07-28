import csv
import os
import pandas
import matplotlib.pyplot as plt

dataFolder = 'data'
outFolder = 'out'
keys = ['A', 'W', 'I', 'Y', 'G', 'H', 'D', 'F', 'C', 'P', 'Q', 'M', 'V', 'S', 'E', 'K', 'R', 'L', 'N', 'T']
aminoAcidFreqDicts = []

lengths = []
filenames = ['azh_1.txt', 'yzh_2.txt', 'gs_3.txt', 'kb_4.txt', 'tv_5.txt', 'irzv_6.txt']

aminoplacesOutFolder = 'aminoplaces'

aminoplacesOut = {fname : open(os.path.join(outFolder, aminoplacesOutFolder, fname), 'w') for fname in filenames}

aminoprocsForAllFiles = []


def print_dict(dictionary, formatStr, file):
   for item in keys:
      stritem = ''
      for s in dictionary[item]:
         stritem += formatStr%(s) + '  '
      file.write(item + ": " + stritem + "\n")

def return_proc(dictionary, counter):
   dictionary_proc = {}
   print(counter)
   for k in keys:
      dictionary_proc[k] = [dictionary[k][i]/float(counter[i]) for i in range(len(counter))]
   return dictionary_proc

def plot_aminocounts(dictionary):
   # plt.figure()
   df2 = pandas.DataFrame(dictionary)
   ax = df2.plot(kind='bar', stacked=True)
   ax.legend(bbox_to_anchor=(1.1, 1.05))
   ax.set_ylim([0,1])


for filename in filenames:
   aminoplaces = dict.fromkeys(keys,0)
   for nuc in aminoplaces:
      aminoplaces[nuc] = [0]*15

   aminocounter = [0]*15

   aminoAcidFreqDict = dict.fromkeys(keys,0)

   with open(os.path.join(dataFolder, filename), 'r') as csvfile:
      reader = csv.reader(csvfile, delimiter='\t', )
      next(reader)
      sumOfUmicount=0.0

      lengths = []
      umiProps = []

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

         lengths.append(len(seq))
         umiProps.append(float(row[1]))

         place = 0
         for s in seq:
            aminoAcidFreqDict[s] = aminoAcidFreqDict[s] + 1
         if(len(seq)==15):
            for s in seq:
               aminoplaces[s][place] += 1
               aminocounter[place] += 1
               place += 1

      # plot of Umo.count
      plt.figure()
      plt.plot(lengths, umiProps)

   aminoAcidFreqDicts.append(aminoAcidFreqDict)

   # print(aminocounter)
   # print_dict(aminoplaces, "%7d", aminoplacesOut[filename])
   aminoprocs = return_proc(aminoplaces, aminocounter)
   print_dict(aminoprocs, "%.2f", aminoplacesOut[filename])

   aminoprocsForAllFiles.append(aminoprocs)

   plot_aminocounts(aminoprocs)
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

for f in aminoplacesOut:
   aminoplacesOut[f].close()
