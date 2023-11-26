from PIL import Image
import os

# Path to the input images folder and output folder
input_folder = 'images'
output_folder = 'output'

# Ensure the output folder exists, if not, create it
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Dimensions of the canvas
canvas_width = 1000
canvas_height = 700

# Reduction percentage
reduction_percent = 0.20  # 20%

# Iterate through each image in the input folder
for filename in os.listdir(input_folder):
    # Ensure the file is an image (you might want to add more checks here)
    if filename.endswith(('.jpg', '.png', '.jpeg')):
        # Open the image
        image_path = os.path.join(input_folder, filename)
        img = Image.open(image_path)

        # Resize the image to fit within the canvas while maintaining aspect ratio
        img.thumbnail((canvas_width, canvas_height))

        # Create a transparent canvas
        canvas = Image.new('RGBA', (canvas_width, canvas_height), (255, 255, 255, 0))

        x = (canvas_width - img.width) // 2
        y = (canvas_height - img.height) // 2

        # Extract the alpha channel from the image
        try:
            r, g, b, a = img.split()
        except ValueError:
            r, g, b = img.split()
            a = Image.new("L", img.size, 255)  # Default to fully opaque

        # Paste the resized image onto the canvas with the alpha channel as mask
        canvas.paste(img, (x, y), mask=a)

        # Convert the image to RGB mode (if necessary) and save
        canvas = canvas.convert('RGB')

        # Save the resulting image to the output folder
        output_path = os.path.join(output_folder, f"processed_{filename}")
        canvas.save(output_path)
