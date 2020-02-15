from PIL import Image
import pytesseract
import re
import json
 
# Include tesseract executable in your path
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
 
# Create an image object of PIL library
image = Image.open('C:/l.jpg')
 
# pass image into pytesseract module
# pytesseract is trained in many languages
image_to_text = pytesseract.image_to_string(image, lang='eng')
 
# Print the text
print(image_to_text)
print("\n")
res1=image_to_text.find('Consumption')
res2=image_to_text.find(' ',res1+14,res1+23)
res3=image_to_text[res1:len(image_to_text)]
for i in res3.split():
	if(i.isdigit()):
		k=i
		break;
print(k)
with open("data_file.json", "w") as write_file:
    json.dump(k, write_file)
with open("data_file.json", "r") as read_file:
    data = json.load(read_file)
print(data)
