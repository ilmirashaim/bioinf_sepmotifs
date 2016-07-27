import csv
import matplotlib.pyplot as plt
from numpy import *
import pylab

input_1 = open('./twins-alpha/pair1/irzv_1.csv', 'rb')
input_2 = open('./twins-alpha/pair1/tv_2.csv', 'rb')
input_3 = open('./twins-alpha/pair2/azh_3.csv', 'rb')
input_4 = open('./twins-alpha/pair2/yzh_4.csv', 'rb')
input_5 = open('./twins-alpha/pair3/gs_5.csv', 'rb')
input_6 = open('./twins-alpha/pair3/kb_6.csv', 'rb')

rows_1 = csv.reader(input_1, delimiter='\t', quotechar='"')
rows_2 = csv.reader(input_2, delimiter='\t', quotechar='"')
rows_3 = csv.reader(input_3, delimiter='\t', quotechar='"')
rows_4 = csv.reader(input_4, delimiter='\t', quotechar='"')
rows_5 = csv.reader(input_5, delimiter='\t', quotechar='"')
rows_6 = csv.reader(input_6, delimiter='\t', quotechar='"')

class Info:
    def __init__(self, count, umi_arr):
        self.COUNT = count
        self.arr_info = {}
        self.arr_info['umi_count'] = umi_arr
    def Info_print(self):
        print 'Struct: COUNT=', self.COUNT
        for el in self.arr_info['umi_count']:
            str_el = str(el)
            print str_el.strip(), ','
        print '\n'

def print_arr(arr):
    print 'Arr:'
    for el in arr:
        str_el = str(el)
        print str_el.strip(), ','
    print '\n'

def print_map(p_map):
    i = 0
    for key in p_map:
        str_count = str(p_map[key].COUNT)
        print key, ': COUNT=', str_count.strip()
        print_arr(p_map[key].arr_info['umi_count'])
        if (i > 3):
            break

def fill_map(rows):
    info_map = {}
    idx = 0
    for row in rows:
        if (idx != 0):
            if (row[5] in info_map):
                info_struct = Info(info_map[row[5]].COUNT, info_map[row[5]].arr_info['umi_count'])
                info_struct.COUNT += 1
                info_struct.arr_info['umi_count'].append(row[0])
                info_map[row[5]] = info_struct
            elif (row[5].count('~') == 0 and row[5].count('*') == 0 and (not row[5] in info_map)):
                info_arr = []
                info_arr.append(row[0])
                info_struct = Info(1, info_arr)
                info_map[row[5]] = info_struct
        idx += 1
    return info_map

def fill_out_file(map, info_map_1, out_file):
    for key in map:
        arr_umi = ''
        for el in info_map_1[key]:
            arr_umi += str(el) + ';'
        out_file.write(str(key) + "=" + str(map[key]) + "; UMI=" + arr_umi + '\n')

map_1 = fill_map(rows_1)
print_map(map_1)

'''i = 0
for key in test_map:
    print key, test_map[key].COUNT
    print_arr(test_map[key].arr_info['umi_count'])
    if (i > 3):
        break'''

'''map_2, info_map_2 = fill_map(rows_2, map_2, info_map_2)
map_3, info_map_3 = fill_map(rows_3, map_3, info_map_3)
map_4, info_map_4 = fill_map(rows_4, map_4, info_map_4)
map_5, info_map_5 = fill_map(rows_5, map_5, info_map_5)
map_6, info_map_6 = fill_map(rows_6, map_6, info_map_6)
j = 0
for key in map_1:
    #print key, map_1[key].COUNT, map_1[key].arr_info['umi_count']
    if (j > 100):
        break
    j += 1

idx = 0
arr_x = []
while idx < len(info_map_1):
    arr_x.append(idx)
    idx += 1

pylab.plot(arr_x, info_map_1)
pylab.show()'''

out_1, out_2, out_3, out_4, out_5, out_6 = open('irzv_1', 'w'), open('tv_2', 'w'), open('azh_3', 'w'), open('yzh_4', 'w'), open('gs_5', 'w'), open('kb_6', 'w')
#fill_out_file(map_1, info_map_1, out_1)
'''fill_out_file(map_2, out_2)
fill_out_file(map_3, out_3)
fill_out_file(map_4, out_4)
fill_out_file(map_5, out_5)
fill_out_file(map_6, out_6)'''

out_1.close()
out_2.close()
out_3.close()
out_4.close()
out_5.close()
out_6.close()

input_1.close()
input_2.close()
input_3.close()
input_4.close()
input_5.close()
input_6.close()
