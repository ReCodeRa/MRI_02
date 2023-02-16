# Extract images from pdf and text from images
# Install packages
python -m pip install --upgrade pip
python -m pip install --upgrade pymupdf

# STEP 1
# import libraries
import fitz
import io
from PIL import Image
 
# STEP 2
# file path you want to extract images from
file = "/workspaces/MRI_02/MRI/tab_img.pdf"
 
# open the file
pdf_file = fitz.open(file)
 
# STEP 3
# iterate over PDF pages
for page_index in range(len(pdf_file)):
 
    # get the page itself
    page = pdf_file[page_index]
    # image_list = page.getImageList()
    image_list = page.get_images()
  
 # CONTINUE HERE
 
    # printing number of images found in this page
    if image_list:
        print(
            f"[+] Found a total of {len(image_list)} images in page {page_index}")
    else:
        print("[!] No images found on page", page_index)
    for image_index, img in enumerate(page.get_images(), start=1):
 
        # get the XREF of the image
        xref = img[0]
 
        # extract the image bytes
        base_image = pdf_file.extract_image(xref)
        image_bytes = base_image["image"]
      
# Extract text from image
# Install tesseract into the Ubuntu container
# sudo apt update
# sudo apt-get install Tesseract-ocr
# pip install pytesseract

from PIL import Image
from pytesseract import pytesseract

# Find were installed:   find . -name "tesseract*"
# Defining paths to tesseract.exe
# and the image we would be using
path_to_tesseract = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
image_path = r"csv\sample_text.png"
  
# Opening the image & storing it in an image object
img = Image.open(image_path)
  
# Providing the tesseract executable
# location to pytesseract library
pytesseract.tesseract_cmd = path_to_tesseract
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
print(text[:-1])
 
        # get the image extension
        image_ext = base_image["ext"]
