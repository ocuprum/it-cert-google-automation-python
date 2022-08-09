#!/usr/bin/env python3
import os
import requests

imgs_directory = '/home/student-03-f8fa30dee73b/supplier-data/images'
url = 'http://34.170.105.169/upload/'

os.chdir(imgs_directory)
for image in os.listdir(imgs_directory):
    if image.endswith('.jpeg'):
        with open(image, 'rb') as image:
            response = requests.post(url, files={'file': image})