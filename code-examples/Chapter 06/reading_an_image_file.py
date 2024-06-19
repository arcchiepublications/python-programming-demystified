# Read an image file
with open('input_image.jpg', 'rb') as file:
    image_data = file.read()

# Write the image data to a new file
with open('output_image.jpg', 'wb') as file:
    file.write(image_data)
