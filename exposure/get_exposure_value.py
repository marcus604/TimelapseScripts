'''
This script calculates the average pixel value of an image and prints the threshold required for considering the image as overexposed.

To be used to generate threshold settings of a known overexposed photo before using 'move_overexposed_photos'

Usage: python get_exposure_value.py image_path

Arguments:

image_path: The path to the image file that you want to analyze. The image must be in JPEG format.

Example: python get_exposure_value.py /home/user/Photos/sunrise.jpg

This will open the image file /home/user/Photos/sunrise.jpg, convert it to grayscale, calculate the average pixel value, and print the threshold for overexposure.

Note: This script requires the PIL module to handle the image processing. You can install it with pip install Pillow.
'''


import sys
from PIL import Image

# Path to the image
image_path = sys.argv[1]

# Open the image
img = Image.open(image_path).convert('L')  # convert image to grayscale

# Calculate the average pixel value
avg_pixel_value = img.resize((1, 1)).getpixel((0, 0))

print(f"The threshold for considering the image as overexposed would be: {avg_pixel_value}")

