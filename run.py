#!/usr/bin/env python3
import os
import requests

desc_directory = 'supplier-data/descriptions'
url = 'http://[linux-instance-external-IP]/fruits'

os.chdir(desc_directory)
descs = []
for text in os.listdir(desc_directory):
    with open(text) as txt:
        desc = {}
        desc['name'], desc['weight'], desc['description'] = txt.read().strip('\n').split('\n')
        desc['weight'] = int(desc['weight'].rstrip(' lbs'))
        desc['image_name'] = text.rstrip('txt') + 'jpeg'
        descs.append(desc)

responce = requests.post(url, json=descs)
if responce.status_code >= 400: 
    raise 'Bad status code!'