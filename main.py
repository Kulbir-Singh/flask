from flask import Flask, render_template, send_file, request

import os
from PIL import Image  
from rembg import remove

app = Flask(__name__)

current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..' ))
# os.path.dirname(os.path.abspath(__file__))

input_file_path = current_dir + '/remove-bg/images/john.PNG'
print("Current script directory:", current_dir + '/images/terry-rozier.jpg')

def remove_background(input_path, output_path):
  input = Image.open(input_path)
  output = remove(input)
  output.save(output_path)
 
def process_image(input_path, output_path):
    image = Image.open(input_path)
    grayscale_image = image.convert("L")
    grayscale_image.save(output_path)
    print(f"Image processed and saved to {output_path}")

@app.route('/')
def index():
  remove_background(input_file_path, "output_grayscale.png")
  image_path = current_dir + '/remove-bg/output_grayscale.png'
  
  mime_type = 'image/png'
    
  return render_template('index.html')

@app.route('/upload', methods=['POST'])
def upload():
    # Check if the 'image' key is in the request.files dictionary
    if 'image' not in request.files:
        return 'No image part in the request', 400

    # Get the file from the request
    image_file = request.files['image']
    original_filename = image_file.filename
    # Check if the file is not empty
    if image_file.filename == '':
        return 'No selected file', 400
   
    # Convert the image to PNG format
    try:
        # Open the image using Pillow
        image = Image.open(image_file)

        # Convert to RGBA to ensure transparency support
        image = image.convert('RGBA')

        # Save the image in PNG format to a temporary file
        temp_input_path = 'temp_input.png'
        image.save(temp_input_path, format='PNG')
    except Exception as e:
        return f"Error converting image to PNG: {str(e)}", 500

    # Process the image file and remove the background
    try:
        with open(temp_input_path, 'rb') as input_file:
            output_data = remove(input_file.read())

        # Save the processed image to a temporary file
        temp_output_path = 'temp_output.png'
        with open(temp_output_path, 'wb') as temp_output:
            temp_output.write(output_data)
    except Exception as e:
        return f"Error processing image: {str(e)}", 500
    finally:
        # Remove temporary input file
        os.remove(temp_input_path)

    # Return the processed image to the user
    return send_file(temp_output_path, mimetype='image/png', as_attachment=True, download_name=original_filename.split('.')[0]+'.png')

if __name__ == '__main__':
  app.run(port=5000)
