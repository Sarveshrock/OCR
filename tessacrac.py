# Import the necessary libraries
import pytesseract
from PIL import Image

# Set the path to the Tesseract executable file
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Load the newspaper image to be recognized
img = Image.open('C:/Users/DjS\Desktop/Python projects/OCR/Test images/245.jpg')

# Resize the image to reduce processing time
#basewidth = 1200
#wpercent = (basewidth / float(img.size[0]))
#hsize = int((float(img.size[1]) * float(wpercent)))
#img = img.resize((basewidth, hsize), Image.ANTIALIAS)

# Perform OCR on the image
text = pytesseract.image_to_string(img)
print(text)

# Create a text file and write the recognized text to it
with open('newspaper_text.txt', mode ='w') as file:
    file.write(text)

# Print a message indicating the text has been saved to a file
print('Recognized text has been saved to newspaper_text.txt')
