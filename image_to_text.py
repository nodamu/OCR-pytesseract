from PIL import Image
import pytesseract
import os
import cv2

# install tesseract ocr "sudo apt-get install tesseract-ocr"
# install pytesseract "pip install pytesseract"

image = cv2.imread('sammy.jpeg')
# image = cv2.resize(image, (0,0), fx=0.5, fy=0.5) 

# Preprocessing steps
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

gray = cv2.threshold(gray, 0, 255,cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]

# Temporal files
filename = "{}.jpeg".format(os.getpid())
cv2.imwrite(filename, gray)

# OCR
text = pytesseract.image_to_string(Image.open(filename))
os.remove(filename)
print(text)
 
# show the output images
cv2.imshow("Image", image)
cv2.imshow("Output", gray)
cv2.waitKey(0)
