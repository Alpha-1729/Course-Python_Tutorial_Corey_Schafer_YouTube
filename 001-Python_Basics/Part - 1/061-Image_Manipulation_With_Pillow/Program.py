#!/usr/bin/python3
# Image Manipulation With Pillow

"""
>>>> Pillow alow us to work with and manipulate images using python.
>>>> Install pillow
        pipenv install Pillow
        OR
        pip install Pillow
>>>>
>>>>
"""

from PIL import Image, ImageFilter

image_1 = Image.open("./Resources/dog_1.jpeg")
image_1.show()

# Saving an image.
image_1.save("./Resources/dog_1_copy.png")

# Resize image.
image_1.thumbnail((300, 300))
image_1.save("./Resources/dog_1_300.png")

# Rotate image left by 90.
image_1.rotate(90).save("./Resources/dog_1_rot_90.png")

# Convert image to Black and White.
image_1.convert(mode="L").save("./Resources/dog_1_BW.png")

# Blur and image.
image_1.filter(ImageFilter.GaussianBlur(15)).save("./Resources/dog_1_Blur.png")
