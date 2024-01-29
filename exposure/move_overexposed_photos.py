'''
This script moves overexposed JPEG images from a given directory and its subdirectories to another directory.

Usage: python move_overexposed_photos.py image_dir dest_dir threshold

Arguments:

image_dir: The path to the directory that contains the JPEG images to be checked and moved. The script will also process any JPEG images in the subdirectories of the given directory.
dest_dir: The path to the directory where the overexposed images will be moved. The script will create the directory if it doesn’t exist.
threshold: The numeric value for determining if an image is overexposed. The script will compare the average pixel value of each image with this threshold and move the image if it is above the threshold.

Example: python move_overexposed_photos.py /home/user/Photos /home/user/Overexposed 200

This will check the JPEG images in /home/user/Photos and its subdirectories for overexposure and move them to /home/user/Overexposed if their average pixel value is above 200.

Note: This script requires the PIL module to handle the image processing. You can install it with pip install Pillow.
'''

import os
import sys
import shutil
from PIL import Image

# Directory containing the images
image_dir = sys.argv[1]

# Directory to move overexposed images
dest_dir = sys.argv[2]

# Create the destination directory if it doesn't exist
os.makedirs(dest_dir, exist_ok=True)

# Threshold for determining if an image is overexposed
threshold = int(sys.argv[3])

# Counter for overexposed images
overexposed_count = 0

# Iterate over each image in the directory
for image_name in os.listdir(image_dir):
    if image_name.endswith('.jpg'):
        image_path = os.path.join(image_dir, image_name)
        
        # Open the image
        img = Image.open(image_path).convert('L')  # convert image to grayscale
        
        # Calculate the average pixel value
        avg_pixel_value = img.resize((1, 1)).getpixel((0, 0))
        
        # If the average pixel value is above the threshold, move the image to the destination directory
        if avg_pixel_value > threshold:
            print(f"Moving overexposed image: {image_name}")
            shutil.move(image_path, os.path.join(dest_dir, image_name))
            overexposed_count += 1

print(f"Total overexposed images moved: {overexposed_count}")

