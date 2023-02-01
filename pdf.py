from tabula import read_pdf
from tabulate import tabulate
import os
 
#reads table from pdf file
df = read_pdf("home/recodera/MRI_dasa/MRI-02/Loper/Loper/Actavis Losiwuto PAR_2662 2014 likeLosidaru.pdf",pages="all") #address of pdf file
print(tabulate(df))