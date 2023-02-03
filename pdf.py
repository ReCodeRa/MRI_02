# from tabula import read_pdf
# from tabulate import tabulate
import os
import camelot
 
# #reads table from pdf file
# print(os.getcwd())
# df = read_pdf("~/MRI_dasa/MRI_02/Loper/Loper/Actavis_Losiwuto_PAR_2662_2014_likeLosidaru.pdf", pages="all") #address of pdf file
# print(tabulate(df))

# print(os.getcwd())
# pth = '/home/recodera/MRI_dasa/MRI_02/Loper/Loper/'
# os.chdir(pth)
# print(os.listdir())
file = "/home/recodera/MRI_dasa/MRI_02/Loper/Loper/LosiActa.pdf"
 
tables = camelot.read_pdf(file)