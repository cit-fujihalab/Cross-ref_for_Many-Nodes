#!/usr/bin/env python3
# coding: utf-8
import json

import os
infilenames_list = []
for file in os.listdir():
    base, ext = os.path.splitext(file)
    if ext == '.json':
        infilenames_list.append(file)
        infilenames_list.sort()

"""
infilenames_list = [
  'Current_Blockchain50051.json', 
  'Current_Blockchain50053.json',
  'Current_Blockchain50055.json',
  'Current_Blockchain50057.json',
  'Current_Blockchain50059.json',
  'Current_Blockchain50061.json', 
  'Current_Blockchain50063.json',
  'Current_Blockchain50065.json',
  'Current_Blockchain50067.json',
  'Current_Blockchain50069.json',
  'Current_Blockchain50071.json', 
  'Current_Blockchain50073.json',
  'Current_Blockchain50075.json',
  'Current_Blockchain50077.json',
  'Current_Blockchain50079.json',
  'Current_Blockchain50081.json', 
  'Current_Blockchain50083.json',
  'Current_Blockchain50085.json',
  'Current_Blockchain50087.json',
  'Current_Blockchain50089.json',
  'Current_Blockchain50091.json', 
  'Current_Blockchain50093.json',
  'Current_Blockchain50095.json',
  'Current_Blockchain50097.json',
  'Current_Blockchain50099.json',
  'Current_Blockchain50101.json', 
  'Current_Blockchain50103.json',
  'Current_Blockchain50105.json',
  'Current_Blockchain50109.json',
  'Current_Blockchain50111.json',
  'Current_Blockchain50113.json', 
  'Current_Blockchain50115.json',
  'Current_Blockchain50117.json',
  'Current_Blockchain50119.json',
  'Current_Blockchain50121.json',
  'Current_Blockchain50123.json', 
  'Current_Blockchain50125.json',
  'Current_Blockchain50127.json',
  'Current_Blockchain50129.json',
  'Current_Blockchain50131.json',
  'Current_Blockchain50133.json', 
  'Current_Blockchain50135.json',
  'Current_Blockchain50137.json',
  'Current_Blockchain50139.json',
  'Current_Blockchain50141.json',
  'Current_Blockchain50143.json', 
  'Current_Blockchain50145.json',
  'Current_Blockchain50147.json',
  'Current_Blockchain50149.json',
  'Current_Blockchain50151.json'
]
"""
count_dict = {}


for infilename in infilenames_list:
  signature_count = 0
  with open(infilename, 'r') as infile:
    for line in infile:
      data_list = json.loads(line)
      for data in data_list:
        if data['cross-ref'] != []:
          signature_count += 1
          block_hashes_list = data['cross-ref'].replace('[', '').replace('"', '').replace(' ', '').split(",")[:len(infilenames_list)]
          #print(infilename, block_hashes_list)
          #print(infilename, data)
          #print("---")
          for block_hash in block_hashes_list:
            if block_hash not in count_dict:
              count_dict[block_hash] = 1
            else:
              count_dict[block_hash] += 1
  print("---")
  print(infilename, signature_count)

print("-----")
sorted_count_dict = dict(sorted(count_dict.items(), key=lambda x:x[1], reverse=True))
success_count = 0
for k, v in sorted_count_dict.items():
  #print(k, v)
  if v==len(infilenames_list):
    success_count += 1
print("-----")
print("Success count:", success_count/len(infilenames_list))
print("Success rate:", success_count/len(sorted_count_dict))
