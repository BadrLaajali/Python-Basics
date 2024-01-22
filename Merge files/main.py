from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

#Using glob to find a pattern and store the founded files into a list
filepaths = glob.glob("Text+Files/*.txt")
#Initialize a pdf file
text_pdf = FPDF(orientation="P", unit="mm", format="A4")

for file in filepaths:
    text_file = pd.read_csv(file)
    #Path(file) Renvoie le path complet du fichier, le stem va extraire le nom du fichier
    file_name = Path(file).stem    
    text_pdf.add_page()
    #Set font and text size
    text_pdf.set_font(family="Times", style="B", size=14)
    text_pdf.set_text_color(0,50,254)
    text_pdf.cell(w=0, h=14, txt=f"{file_name.title()} :", align="L", ln=1)

text_pdf.output(f"pdfs/animals.pdf")