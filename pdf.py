from tabula import read_pdf
from tabulate import tabulate
import os
# import camelot

file = "/home/recodera/MRI_dasa/MRI_02/Loper/Loper/LosiActa.pdf"

#reads table from pdf file
print(os.getcwd())
df = read_pdf(file, pages="all") #address of pdf file
print(tabulate(df))

# print(os.getcwd())
# pth = '/home/recodera/MRI_dasa/MRI_02/Loper/Loper/'
# os.chdir(pth)
# print(os.listdir())

# tables = camelot.read_pdf(file)