from pathlib import Path
from PIL import Image

# Define the root folder of the script
ROOT_FOLDER = Path(__file__).parent

# Define the original image path and the new image path
ORIGINAL = ROOT_FOLDER / 'original.JPG'
NEW_IMAGE = ROOT_FOLDER / 'new.JPG'  # Removed extra space in filename

# Open the original image
pil_image = Image.open(ORIGINAL)

# Get the width and height of the original image
width, height = pil_image.size

# Get the EXIF metadata (if needed)
exif = pil_image.info['exif']

# Calculate new dimensions keeping the aspect ratio
new_width = 640
new_height = round(height * new_width / width)

# Resize the image to the new dimensions
new_image = pil_image.resize(size=(new_width, new_height))

# Save the resized image with optimization and reduced quality
new_image.save(
    NEW_IMAGE,
    optimize=True,
    quality=70,
    # exif=exif,  # Uncomment to preserve EXIF metadata
)
