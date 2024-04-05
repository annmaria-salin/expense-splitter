import flat_classes

amount = float(input("Hey user, enter the bill amount: ")) 
period = input("What is the bill period? E.g. December 2020: ")

name1 = input("What is your name? ")
days_in_house1 = int(input(f"Howmany days did {name1} stayed in the house during the bill period? "))

name2 = input("What is your name of the other flatmate? ")
days_in_house2 = int(input(f"Howmany days did {name2} stayed in the house during the bill period? "))

the_bill = Bill(amount, period)
flatmate1 = Flatmates(name1, days_in_house1)
flatmate2 = Flatmates(name2, days_in_house2)

print(f'{flatmate1.name} pays:', flatmate1.pays(the_bill, flatmate2))
print(f'{flatmate2.name} pays:', flatmate2.pays(the_bill, flatmate1))

pdf_report = PdfReport(f'{the_bill.period}.pdf')
pdf_report.generate(flatmate1, flatmate2, the_bill)



