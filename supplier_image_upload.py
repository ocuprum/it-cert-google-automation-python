#!/usr/bin/env python3
import os
import requests

imgs_directory = '/supplier-data/images'
url = '/upload/'

os.chdir(imgs_directory)
for image in os.listdir(imgs_directory):
    with open(image, 'rb') as image:
        response = requests.post(url, files={'file': image})