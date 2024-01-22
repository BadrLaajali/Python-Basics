from fpdf import FPDF
import pandas as pd
import glob
from pathlib import Path

def generate_sequence():
    num = 1
    while True:
        yield num
        num += 1

#Using glob to find a pattern and store the founded files into a list
filepaths = glob.glob("invoices/*.xlsx")
for file in filepaths:
    invoice_pd = pd.read_excel(file, sheet_name="Sheet 1")
    #Path(file) Renvoie le path complet du fichier, le stem va extraire le nom du fichier
    file_name = Path(file).stem
    invoice_pdf = FPDF(orientation="P", unit="mm", format="A4")
    invoice_pdf.add_page()
    #Set font and text size
    invoice_pdf.set_font(family="Times", style="B", size=14)
    invoice_pdf.set_text_color(0,50,254)
    #Add a cell, the {file_name.split('-')[0]} permet d'extraire la premiere partie du nom (qui est le numéro)
    invoice_pdf.cell(w=0, h=14, txt=f"Invoice Number :{file_name.split('-')[0]}", align="L", ln=1)
    #Add a line with date
    invoice_pdf.cell(w=0, h=14, txt=f"Date :{file_name.split('-')[1]}", align="L", ln=1)
    #---------Start building the table-------------#
    # Building the columns
    column_list = list(invoice_pd.columns) # Get the columns name
    invoice_pdf.set_font(family="Times", style="B", size=12)
    invoice_pdf.set_text_color(80,80,80)
    invoice_pdf.cell(w=30, h=8, txt=column_list[0].split('_')[1].title(), border=1)
    invoice_pdf.cell(w=70, h=8, txt=column_list[1].split('_')[1].title(), border=1)
    invoice_pdf.cell(w=30, h=8, txt=column_list[2].split('_')[1].title(), border=1)
    invoice_pdf.cell(w=30, h=8, txt=column_list[3].split('_')[0].title(), border=1)
    invoice_pdf.cell(w=30, h=8, txt=column_list[4].split('_')[1].title(), border=1, ln=1) 
    #Building the lines
    total_price = 0
    for index, row in invoice_pd.iterrows():
        invoice_pdf.set_font(family="Times", size=10)
        invoice_pdf.set_text_color(80,80,80)
        #When the row return an integer we need to convert it into a string
        invoice_pdf.cell(w=30, h=8, txt=str(row["product_id"]), border=1)
        invoice_pdf.cell(w=70, h=8, txt=row["product_name"], border=1)
        invoice_pdf.cell(w=30, h=8, txt=str(row["amount_purchased"]), border=1)
        invoice_pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)
        invoice_pdf.cell(w=30, h=8, txt=str(row["total_price"]), border=1, ln=1) #ln pour saut de ligne

    #Get the total of all total price in each file
    invoice_pdf.cell(w=30, h=8, txt=str(invoice_pd["total_price"].sum()), border=1, ln=1)
    invoice_pdf.output(f"pdfs/{file_name}.pdf")

