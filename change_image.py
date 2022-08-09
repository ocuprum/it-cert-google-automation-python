#!/usr/bin/env python3
import os
from PIL import Image
from typing import Tuple

def change_image(img_name: str, size: Tuple[int, int], img_format: str) -> None:
    with Image.open(img_name) as img:
        new_img = img.convert('RGB').resize(size)
        new_img_name = '{}{}'.format(img_name.rstrip('tiff'), img_format.lower())
        new_img.save(new_img_name, format=img_format)

# Working with supplier images
directory = '/home/student-03-f8fa30dee73b/supplier-data/images'
save_directory = '/home/student-03-f8fa30dee73b/supplier-data/images'

os.chdir(save_directory)
for img in os.listdir(directory):
    if img.endswith('.tiff'): 
        change_image(img, (600, 400), 'JPEG') 