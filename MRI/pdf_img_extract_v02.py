# Extract images from pdf and text from ehese images

# Install packages
# pip install --upgrade pip
# pip install --upgrade pymupdf
# Install tesseract into the Ubuntu container
# sudo apt update
# sudo apt install tesseract-ocr
# sudo apt install libtesseract-dev
# pip install pytesseract

# STEP 1
# run interactive Python interpreter
# import libraries
import fitz
import io
from PIL import Image
from pytesseract import pytesseract
 
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

    # printing number of images found in this page
    if image_list:
        print(f"[+] Found a total of {len(image_list)} images in page {page_index}")
    else:
        print("[!] No images found on page", page_index)

    for image_index, img in enumerate(page.get_images(), start=1):

        # get the XREF of the image
        xref = img[0]

        # extract the image bytes
        base_image = pdf_file.extract_image(xref)
        print(base_image)
        image_bytes = base_image["image"]
        # get the image extension
        image_ext = base_image["ext"]
        # load it to PIL
        image = Image.open(io.BytesIO(image_bytes))
        # save it to local disk
        image.save(open(f"image{page_index+1}_{image_index}.{image_ext}", "wb"))

image_path = "/workspaces/MRI_02/image10_3.png"
path_to_tessercat = "/usr/bin/tesseract"
  
# Opening the image & storing it in an image object
img = Image.open(image_path)
pytesseract.tesseract_cmd = path_to_tessercat
  
# Passing the image object to image_to_string() function
# This function will extract the text from the image
text = pytesseract.image_to_string(img)
  
# Displaying the extracted text
print(text[:-1])