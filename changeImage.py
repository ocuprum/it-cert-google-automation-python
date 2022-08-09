#!/usr/bin/env python3
import os
from PIL import Image
from typing import Tuple

def change_image(img_name: str, size: Tuple[int, int], img_format: str, save_dir: str) -> None:
    with Image.open(img_name) as img:
        new_img = img.convert('RGB').resize(size)
        new_img.save(save_dir, format=img_format)

# Working with supplier images
directory = '/supplier-data/images'
save_directory = '/supplier-data/images'

os.chdir(directory)
for img in os.listdir(directory):
    change_image(img, (600, 400), 'JPEG') 