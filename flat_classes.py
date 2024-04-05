
from fpdf import FPDF 
import webbrowser

class Bill():
    
    """object that contains data about the amount and period of the bill """
    
    def __init__(self, amount, period):
        self.amount = amount
        self.period = period
        

class Flatmates():
    
    """person who leaves in the flat and pays a share of the bill"""
    
    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house
        
    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = bill.amount * weight 
        return to_pay
    


class PdfReport():
    
    def __init__(self, filename):
        self.filename = filename
        
    def generate(self, flatmate1, flatmate2, bill):
        
        flatmate1_pay = str(round(flatmate1.pays(bill, flatmate2), 2))
        flatmate2_pay = str(round(flatmate2.pays(bill, flatmate1), 2))
        
        self.pdf = FPDF(orientation ='P', unit = 'pt', format = 'A4')
        self.pdf.add_page()
        
        #add title
        self.pdf.set_font(family ='Times', size = 24, style = 'B')
        
        #add icon
        self.pdf.image('house.png', w = 50, h = 50)
        
        #insert values
        self.pdf.cell(w = 0, h = 80, txt = 'Flatmates Bill', border = 1, align ='C', ln = 1)
        
        self.pdf.set_font(family ='Times', size = 14, style = 'B')
        self.pdf.cell(w = 100, h = 40, txt = 'Period:', border = 0)
        self.pdf.cell(w = 150, h = 40, txt = bill.period, border = 0, ln = 1)
        
        #name and due amount for first flatmate
        self.pdf.set_font(family ='Times', size = 14)
        self.pdf.cell(w = 100, h = 40, txt = flatmate1.name, border = 0)
        self.pdf.cell(w = 150, h = 40, txt =  flatmate1_pay, border = 0, ln = 1)
        
        #name and due amount for second flatmate
        self.pdf.cell(w = 100, h = 40, txt = flatmate2.name, border = 0)
        self.pdf.cell(w = 150, h = 40, txt =  flatmate2_pay, border = 0, ln = 1)
        
        self.pdf.output(self.filename)
        webbrowser.open(self.filename)
        