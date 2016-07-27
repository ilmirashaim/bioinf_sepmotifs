#!/usr/bin/python2.7
# -*- coding: utf-8 -*-

from pickle import dump
import csv
import os
import pickle
from helpst import Info_st

#-----------------------------------CONF:
maps_dir = './Map'
data_dir = './Data'
compare_dir = './Comp'
if (not os.path.exists(maps_dir)):
    os.mkdir(maps_dir)
if (not os.path.exists(data_dir)):
    os.mkdir(data_dir)
if (not os.path.exists(compare_dir)):
    os.mkdir(compare_dir)

info_map_1, info_map_2, info_map_3, info_map_4, info_map_5, info_map_6 = {}, {}, {}, {}, {}, {}
are_exists = 0
'''if (not(os.path.exists(maps_dir + '/info_map_1') and os.path.exists(maps_dir + '/info_map_2') and
            os.path.exists(maps_dir + '/info_map_3') and os.path.exists(maps_dir + '/info_map_3') and
            os.path.exists(maps_dir + '/info_map_4') and os.path.exists(maps_dir + '/info_map_6'))):
    are_exists = 0
    print 'Creating files...'
else:
    f1, f2, f3 = pickle.load(open(str(maps_dir + '/info_map_1'),'rb')), pickle.load(open(str(maps_dir + '/info_map_2'),'rb')), pickle.load(open(str(maps_dir + '/info_map_3'),'rb'))
    f4, f5, f6 = pickle.load(open(str(maps_dir + '/info_map_4'),'rb')), pickle.load(open(str(maps_dir + '/info_map_5'),'rb')), pickle.load(open(str(maps_dir + '/info_map_6'),'rb'))
    info_map_1, info_map_2, info_map_3, info_map_4 = list(f1.values()), list(f2.values()), list(f3.values()), list(f4.values())
    info_map_5, info_map_6 = list(f5.values()), list(f6.values())
    print 'Comparison...'''

#-----------------------------------Functions

def fill_map(rows):
    info_map = {}
    idx = 0
    for row in rows:
        if (idx != 0):
            if (row[5] in info_map):
                info_struct = Info_st(info_map[row[5]].COUNT, info_map[row[5]].arr_info['umi_count'])
                info_struct.COUNT += 1
                info_struct.arr_info['umi_count'].append(row[0])
                info_map[row[5]] = info_struct
            elif (row[5].count('~') == 0 and row[5].count('*') == 0 and (not row[5] in info_map)):
                info_arr = []
                info_arr.append(row[0])
                info_struct = Info_st(1, info_arr)
                info_map[row[5]] = info_struct
        idx += 1
    return info_map

def fill_out_file(info_map, out_file):
    for key in info_map:
        str_count = str(info_map[key].COUNT)
        arr_umi = ''
        for el in info_map[key].arr_info['umi_count']:
            str_el = str(el)
            arr_umi += str_el.strip() + ';'
        out_file.write(str(key)  + ': COUNT=' + str_count.strip() + '\n' + 'Umi.count: ' + arr_umi + '\n\n')

def print_arr(arr):
    arr_str = 'Arr_info:' + '\n'
    arr_str += 'Umi.count: '
    for el in arr:
        str_el = str(el)
        arr_str += str_el.strip() + ';'
    print arr_str, '\n'

def print_map(p_map):
    i = 0
    for key in p_map:
        str_count = ''
        str_count += str(p_map[key].COUNT)
        str_key_count = ''
        str_key_count += key + ': COUNT=' + str_count.strip()
        print str_key_count
        print_arr(p_map[key].arr_info['umi_count'])
        if (i > 3):
            break

#-----------------------------------Creating_files:

print 'Creating files...'

if (are_exists == 0):

    input_1 = open('./twins-alpha/pair1/irzv_1.csv', 'rb')
    input_2 = open('./twins-alpha/pair1/tv_2.csv', 'rb')
    input_3 = open('./twins-alpha/pair2/azh_3.csv', 'rb')
    input_4 = open('./twins-alpha/pair2/yzh_4.csv', 'rb')
    input_5 = open('./twins-alpha/pair3/gs_5.csv', 'rb')
    input_6 = open('./twins-alpha/pair3/kb_6.csv', 'rb')

    info_map_1 = fill_map(csv.reader(input_1, delimiter='\t', quotechar='"'))
    result_dump = dump(info_map_1, open(maps_dir + '/info_map_1', "wb"))
    print result_dump

    info_map_2 = fill_map(csv.reader(input_2, delimiter='\t', quotechar='"'))
    result_dump = dump(info_map_2, open(maps_dir + '/info_map_2', "wb"))
    print result_dump

    info_map_3 = fill_map(csv.reader(input_3, delimiter='\t', quotechar='"'))
    result_dump = dump(info_map_3, open(maps_dir + '/info_map_3', "wb"))
    print result_dump

    info_map_4 = fill_map(csv.reader(input_4, delimiter='\t', quotechar='"'))
    result_dump = dump(info_map_4, open(maps_dir + '/info_map_4', "wb"))
    print result_dump

    info_map_5 = fill_map(csv.reader(input_5, delimiter='\t', quotechar='"'))
    result_dump = dump(info_map_5, open(maps_dir + '/info_map_5', "wb"))
    print result_dump

    info_map_6 = fill_map(csv.reader(input_6, delimiter='\t', quotechar='"'))
    result_dump = dump(info_map_6, open(maps_dir + '/info_map_6', "wb"))
    print result_dump

    out_1, out_2, out_3 = open(data_dir + '/irzv_1_data', 'w'), open(data_dir + '/tv_2_data', 'w'), open(data_dir + '/azh_3_data', 'w')
    out_4, out_5, out_6 = open(data_dir + '/yzh_4_data', 'w'), open(data_dir + '/gs_5_data', 'w'), open(data_dir + '/kb_6_data', 'w')
    fill_out_file(info_map_1, out_1)
    fill_out_file(info_map_2, out_2)
    fill_out_file(info_map_3, out_3)
    fill_out_file(info_map_4, out_4)
    fill_out_file(info_map_5, out_5)
    fill_out_file(info_map_6, out_6)

    out_1.close()
    out_2.close()
    out_3.close()
    out_4.close()
    out_5.close()
    out_6.close()

#-----------------------------------COMPARE:

print 'Comparison...'''

out_1_2, out_1_3 = open(compare_dir + '/compare_irzv_1-tv_2', 'w'), open(compare_dir + '/compare_irzv_1-azh_3', 'w')
out_1_4, out_1_5 = open(compare_dir + '/compare_irzv_1-yzh_4', 'w'), open(compare_dir + '/compare_irzv_1-gs_5', 'w')
out_1_6 = open(compare_dir + '/compare_irzv_1-kb_6', 'w')

out_2_3, out_2_4 = open(compare_dir + '/compare_tv_2-azh_3', 'w'), open(compare_dir + '/compare_tv_2-yzh_4', 'w')
out_2_5, out_2_6 = open(compare_dir + '/compare_tv_2-gs_5', 'w'), open(compare_dir + '/compare_tv_2-kb_6', 'w')

out_3_4, out_3_5 = open(compare_dir + '/compare_azh_3-yzh_4', 'w'), open(compare_dir + '/compare_azh_3-gs_5', 'w')
out_3_6 = open(compare_dir + '/compare_azh_3-kb_6', 'w')

out_4_5, out_4_6 = open(compare_dir + '/compare_yzh_4-gs_5', 'w'), open(compare_dir + '/compare_yzh_4-kb_6', 'w')

out_5_6 = open(compare_dir + '/compare_gs_5-kb_6', 'w')

def compare_maps(info_map_1, info_map_2, out_file):
    def create_str_arr_umi(info_map, key):
        arr_umi = ''
        for el in info_map[key].arr_info['umi_count']:
            str_el = str(el)
            arr_umi += str_el.strip() + ';'
        return arr_umi

    for key in info_map_1:
        if (key in info_map_2):
            str_umi_1 = create_str_arr_umi(info_map_1, key)
            str_umi_2 = create_str_arr_umi(info_map_2, key)
            out_file.write('KEY=' + str(key) + ':\n' + str_umi_1 + '\n' + str_umi_2 + '\n\n')

compare_maps(info_map_1, info_map_2, out_1_2)
compare_maps(info_map_1, info_map_3, out_1_3)
compare_maps(info_map_1, info_map_4, out_1_4)
compare_maps(info_map_1, info_map_5, out_1_5)
compare_maps(info_map_1, info_map_6, out_1_6)
compare_maps(info_map_2, info_map_3, out_2_3)
compare_maps(info_map_2, info_map_4, out_2_4)
compare_maps(info_map_2, info_map_5, out_2_5)
compare_maps(info_map_2, info_map_6, out_2_6)
compare_maps(info_map_3, info_map_4, out_3_4)
compare_maps(info_map_3, info_map_5, out_3_5)
compare_maps(info_map_3, info_map_6, out_3_6)
compare_maps(info_map_4, info_map_5, out_4_5)
compare_maps(info_map_4, info_map_6, out_4_6)
compare_maps(info_map_5, info_map_6, out_5_6)

out_1_2.close()
out_1_3.close()
out_1_4.close()
out_1_5.close()
out_1_6.close()
out_2_3.close()
out_2_4.close()
out_2_5.close()
out_2_6.close()
out_3_4.close()
out_3_5.close()
out_3_6.close()
out_4_5.close()
out_4_6.close()
out_5_6.close()

#------------------------------------------

input_1.close()
input_2.close()
input_3.close()
input_4.close()
input_5.close()
input_6.close()

'''idx = 0
arr_x = []
while idx < len(info_map_1):
    arr_x.append(idx)
    idx += 1

pylab.plot(arr_x, info_map_1)
pylab.show()'''
