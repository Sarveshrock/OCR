import os 
import cv2 
from PIL import Image 
import pytesseract as pt 

test_img_path = "C:/Users/DjS/Desktop/Python projects/OCR/Test images/"
create_path = lambda f : os.path.join(test_img_path, f)

test_image_files = os.listdir(test_img_path)

#for f in test_image_files:
    #print(f)

def show_image(img_path, size=(500, 500)):
    image = cv2.imread(img_path)
    image = cv2.resize(image, size)
    
    cv2.imshow("IMAGE", image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

pt.pytesseract.tesseract_cmd = r"C://Program Files//Tesseract-OCR//tesseract.exe" 


def show_image(img_path,size=(500,500)):
    Image=cv2.imread(img_path)
    Image=cv2.resize(Image,size)
    cv2.imshow("IMAGE",Image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


avb_langs=pt.get_languages(config='')
#for lang in avb_langs:
    #print(lang)0

image_path = test_image_files[12] # 2, 3, 12, 1, 13, 15
path = create_path(image_path)

image = Image.open(path)
text = pt.image_to_string(image)

print(text)
show_image(path)

path = create_path("portu-text-2.jpg")

image = Image.open(path)
text = pt.image_to_string(image, lang='por')

print(text)
show_image(path)



path = create_path("news-2.jpg")

image = Image.open(path)
text = 'NO TEXT TO BE APPEARED'

try:
    text = pt.image_to_string(image, lang='eng', timeout=5)
except RuntimeError as timeout_error:
    print("[TIMEOUT ERROR]")

print(text)
show_image(path)

path = create_path("jap-text-1.png")

image = Image.open(path)
bound_rects = pt.image_to_boxes(image, lang='jpn')

print(bound_rects)
show_image(path)


img = cv2.imread(path)
h, _, _ = img.shape

for b in bound_rects.splitlines():
    b = b.strip().split(' ')
    img = cv2.rectangle(img, (int(b[1]), h - int(b[2])), (int(b[3]), h - int(b[4])), (0, 255, 0), 2)

cv2.imshow("CHARACTERIZED IMAGE", img)
cv2.waitKey(0)
cv2.destroyAllWindows()

image_path = test_image_files[2]
path = create_path(image_path)

image = Image.open(path)
text = pt.image_to_data(image)

print(text)
show_image(path)

path = create_path("hindi-text-1.jpg")

image = Image.open(path)
text = pt.image_to_string(image, lang='hin')

print(text)
path = create_path("WhatsApp Image 2023-03-10 at 3.36.35 PM.jpg")

image = Image.open(path)
text = pt.image_to_string(image, lang='eng')

print(text)
show_image(path)
path = create_path("hindi-text-2.jpg")

image = Image.open(path)
text = pt.image_to_string(image, lang='hin')

print(text)
show_image(path) 

file_save_path = "C:/Users/DjS/Desktop/Python projects/OCR/Test images/"

# hocr: open standard of data representation for formatted text obtained from (OCR)
file = pt.image_to_string(Image.open())

file = file.replace("-\n", " ")
file.write(text)
file.close()

#text = str(((pytesseract.image_to_string(Image.open(image_file)))))
#text = text.replace("-\n", "")
#output_file.write(text)


