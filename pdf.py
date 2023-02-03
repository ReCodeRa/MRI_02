from tabula import read_pdf
from tabulate import tabulate
import os
import camelot
 
# #reads table from pdf file
# print(os.getcwd())
# df = read_pdf("~/MRI_dasa/MRI_02/Loper/Loper/Actavis_Losiwuto_PAR_2662_2014_likeLosidaru.pdf", pages="all") #address of pdf file
# print(tabulate(df))

print(os.getcwd())
file = "home/MRI_dasa/MRI_02/Loper/Loper/Actavis_Losiwuto_PAR_2662_2014_likeLosidaru.pdf"
 
tables = camelot.read_pdf(file, pages = "1-end")
tables[0].df