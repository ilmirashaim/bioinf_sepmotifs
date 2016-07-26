import csv
import os
dataFolder = 'data'
dict = {}
with open(os.path.join(dataFolder, 'irzv.txt'), 'r') as csvfile:
   reader = csv.reader(csvfile, delimiter='\t', )
   next(reader)
   sum_of_umicount=0.0
   for row in reader:
      sum_of_umicount =sum_of_umicount + float(row[1])
      seq = row[5]
      for s in seq:
         if not s in dict.keys():
            dict[s] = 0
         dict[s] = dict[s] + 1

print(sum_of_umicount)
print(dict.keys())
print(dict)