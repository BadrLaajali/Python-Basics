from turtle import st
from fpdf import FPDF
import pandas as pd

#Create the pdf object
pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

#Load the csv with pandas and create the object that will contain the data
topics_df = pd.read_csv("topics.csv")

for index, row in topics_df.iterrows():
    # parcourir les valeurs de i de 0 à row[0] - 1 (car ca commence de 0)
    for i in range(row[2]): #we can also say row["Pages"]
        #Add a page to our pdf object
        pdf.add_page()
        #Set font and text size
        pdf.set_font(family="Times", style="B", size=14)
        pdf.set_text_color(0,50,254)
        #Add a cell
        pdf.cell(w=0, h=14, txt=f"{row[0]} - {row[1]}", align="L", ln=1)
        #Add the line after our Title
        pdf.line(10,21,200,21)
        #Add a footer
        pdf.ln(260)
        pdf.set_font(family="Times", style="I", size=8)
        pdf.set_text_color(180,180,180)
        pdf.cell(w=0,h=10, txt=row["Topic"], align="R")


pdf.output("newpdf.pdf")
