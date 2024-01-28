'''
This script sorts JPEG images in a given directory and all its subdirectories by their timestamp and renames them with sequential numbers.

Usage: python sort_files_by_time.py directory start_value

Arguments:
- directory: The path to the directory that contains the JPEG images to be sorted and renamed. The script will also process any JPEG images in the subdirectories of the given directory.
- start_value: The starting number for the renaming process.

Example: python sort_files_by_time.py /home/user/Pictures 100

This will sort the JPEG images in /home/user/Pictures and its subdirectories by their timestamp and rename them as 100.jpg, 101.jpg, 102.jpg, etc.

Note: This script requires the PIL module to handle the EXIF data of the images. You can install it with pip install Pillow.

'''


import os
import sys
from PIL import Image
from PIL.ExifTags import TAGS

def handle_exif_data(exif_data):
    exif_data = {
        TAGS[key]: exif_data[key]
        for key in exif_data.keys()
        if key in TAGS and isinstance(exif_data[key], (bytes, str))
    }
    return exif_data

def sort_files(directory, start_value):
    images = []
    for root, dirs, files in os.walk(directory):
        for filename in files:
            if filename.lower().endswith((".jpg", ".jpeg")):
                image = Image.open(os.path.join(root, filename))
                exif_data = handle_exif_data(image._getexif())
                timestamp = exif_data.get('DateTime', None)
                if timestamp:
                    images.append((timestamp, root, filename))
                else:
                    print(f"{filename} has no timestamp")
            else:
                print(f"{filename} is not a JPEG image")

    images.sort() 

    counter = start_value
    for _, root, filename in images:
        old_path = os.path.join(root, filename)
        new_name = f"{counter}.jpg"
        new_path = os.path.join(root, new_name)
        os.rename(old_path, new_path)  
        print(f"Renamed {old_path} to {new_path}")
        counter += 1


directory = sys.argv[1]
start_value = int(sys.argv[2])


sort_files(directory, start_value)

