from firecloud import fiss
import firecloud.api as fapi
import os
import io
import pandas as pd
import re
import json
#import collections
#import sys
#import csv
#import logging
#import time

ws_namespace = ""
ws_name = ""
table_name = ""

pattern1 = re.compile(r'CA-CCPHL-\d+')
pattern2 = re.compile(r'EPI_ISL_\d+')

matches_dict = {}

with open('logfile2.txt', 'r') as logfile:
    for line in logfile:
        match1 = pattern1.search(line)
        match2 = pattern2.search(line)
        if match1 and match2:
            key = match1.group()
            value = match2.group()
            matches_dict[key] = value

#print(matches_dict)

matches_string = ' '.join(matches_dict.keys())

sampleinfo = fapi.get_entities_query(ws_namespace, ws_name, table_name, filter_terms=matches_string, filter_operator="or")
data=json.loads(sampleinfo.text)

temp_dict = {}

for result in data['results']:
    submission_id = result['attributes']['submission_id']
    name = result['name']
    
    if submission_id in matches_dict:
        temp_dict[name] = matches_dict[submission_id]
    else:
        # If there's no match, keep the original key-value pair
        temp_dict[submission_id] = matches_dict.get(submission_id, None)

matches_dict = temp_dict

print(matches_dict)

for i in range(len(matches_dict)):
    #print(matches_dict[i][0], matches_dict[i][1])
    ws_updates.append(fapi._attr_set(ws_attr[i][0], ws_attr[i][1]))

fapi._attr_set(matches_dict[])

ws_updates = []
for key, value in matches_dict.items():
  #print(key,value)
  ws_updates.append(fapi._attr_set('GISAID_ID', value))
  fapi.update_entity(ws_namespace, ws_name, table_name,key,ws_updates)

  for result in data['results']:
    submission_id = result['attributes']['submission_id']
    name = result['name']
    
    if submission_id in matches_dict:
        temp_dict[name] = matches_dict[submission_id]
    else:
        # If there's no match, keep the original key-value pair
        temp_dict[submission_id] = matches_dict.get(submission_id, None)

matches_dict = temp_dict

print(matches_dict)

for i in range(len(matches_dict)):
    #print(matches_dict[i][0], matches_dict[i][1])
    ws_updates.append(fapi._attr_set(ws_attr[i][0], ws_attr[i][1]))

fapi._attr_set(matches_dict[])

ws_updates = []
for key, value in matches_dict.items():
  #print(key,value)
  ws_updates.append(fapi._attr_set('GISAID_ID', value))
  fapi.update_entity(ws_namespace, ws_name, table_name,key,ws_updates)