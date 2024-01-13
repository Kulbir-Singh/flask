
import os
from PIL import Image  
from rembg import remove


current_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), '..' ))
# os.path.dirname(os.path.abspath(__file__))
 

input_file_path = current_dir + '/public/images/john.PNG'
print("Current script directory:", current_dir + '/public/images/terry-rozier.jpg')

def remove_background(input_path, output_path):
  input = Image.open(input_path)
  output = remove(input)
  output.save(output_path)
 
def process_image(input_path, output_path):
    image = Image.open(input_path)
    grayscale_image = image.convert("L")
    grayscale_image.save(output_path)
    print(f"Image processed and saved to {output_path}")



if __name__ == "__main__":
    remove_background(input_file_path, "output_grayscale.png")