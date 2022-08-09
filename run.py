#!/usr/bin/env python3
import os
import requests

desc_directory = '/home/student-03-f8fa30dee73b/supplier-data/descriptions'
url = 'http://34.170.105.169/fruits/'

os.chdir(desc_directory)
for text in os.listdir(desc_directory):
    with open(text) as txt:
        desc = {}
        desc['name'], desc['weight'], desc['description'] = txt.read().strip('\n').split('\n')
        desc['weight'] = int(desc['weight'].rstrip(' lbs'))
        desc['image_name'] = text.rstrip('txt') + 'jpeg'
        response = requests.post(url, json=desc)
        if response.status_code >= 400: 
            raise 'Bad status code!'