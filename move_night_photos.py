import os
import shutil
import sys
from PIL import Image
from astral.sun import sun
from astral import LocationInfo
from datetime import datetime

# Get the city and country from the command line arguments
city_name = sys.argv[1]
country_name = sys.argv[2]

# Set the city and timezone
city = LocationInfo(city_name, country_name)

# Directory containing the images
image_dir = sys.argv[3]

# Directory to move nighttime images
night_dir = sys.argv[4]

# Ensure the night_dir exists
os.makedirs(night_dir, exist_ok=True)

# Iterate over each image in the directory
for image_name in os.listdir(image_dir):
    if image_name.endswith('.jpg'):
        image_path = os.path.join(image_dir, image_name)
        
        # Open the image and get the EXIF data
        img = Image.open(image_path)
        exif_data = img._getexif()
        
        # Get the date and time the photo was taken (tag 36867)
        date_time_original = exif_data.get(36867, '')
        
        if date_time_original:
            # Convert the date and time to a datetime object
            dt = datetime.strptime(date_time_original, '%Y:%m:%d %H:%M:%S')
            
            # Get the sunrise and sunset times for the date the photo was taken
            s = sun(city.observer, date=dt.date())
            
            # If the photo was taken at night, move it to the night_dir
            if dt.time() < s['sunrise'].time() or dt.time() > s['sunset'].time():
                shutil.move(image_path, os.path.join(night_dir, image_name))
