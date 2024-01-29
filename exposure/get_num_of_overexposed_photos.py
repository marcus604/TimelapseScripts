'''
This script prints the names of overexposed JPEG images in a given directory and its subdirectories.

Useful to run before 'move_overexposed_photos.py' to test amount of files that would be moved.

Usage: python get_num_of_overexposed_photos.py image_dir threshold

Arguments:

image_dir: The path to the directory that contains the JPEG images to be checked. The script will also process any JPEG images in the subdirectories of the given directory.
threshold: The numeric value for determining if an image is overexposed. The script will compare the average pixel value of each image with this threshold and print the image name if it is above the threshold.

Example: python get_num_of_overexposed_photos.py /home/user/Photos 200

This will check the JPEG images in /home/user/Photos and its subdirectories for overexposure and print the names of the images that have an average pixel value above 200.

Note: This script requires the PIL module to handle the image processing. You can install it with pip install Pillow.
'''


import os
import sys
from PIL import Image

# Directory containing the images
image_dir = sys.argv[1]

# Threshold for determining if an image is overexposed
threshold = int(sys.argv[2])

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
        
        # If the average pixel value is above the threshold, print the image name
        if avg_pixel_value > threshold:
            print(image_name)
            overexposed_count += 1

print(f"Total overexposed images: {overexposed_count}")

