import re
import csv
import tkinter as tk
from tkinter import filedialog
from datetime import datetime

#Asking the user for file
root = tk.Tk()
root.withdraw()

file_path = filedialog.askopenfilename()

print(file_path)

xfile = open(file_path)

#Main Program
fh = xfile
customers = list()
dte = list()
money = list()
data = list()
cash = list()
card = list()
i=1
for line in fh:
    words = line.split()
    data.append(re.findall("\AΠεριγραφή", line))
    dte.append(words)
    #if line == "Περιγραφή":
        #print(line)

    for word in words:
        if word == "Αριθμός":
            customers.append(words[2])
        if word == "Σύνολο":
            money.append(words[2])
        if word == "Μετρητά":
            cash.append(words[1])
        if word == "ΠΙΣΤΩΤΙΚΗ":
            card.append(words[1])
for line in data:

    if len(line) < 1:
        i=i+1
    else:
        break

x = dte[0]
print("Date:", x[0])

print("Customers:", customers[0])

print("income:", money[0])

print("expenses:", money[1])

cs = cash[0]
print("cash:", cs)

cc = card[0]
print("credit card:", cc)

xfile.close()
products = list()
quantities = list()
values = list()

with open(file_path, 'r') as current:
    content = current.readlines()
    c = content[i:]
    for line in c:
        words= line.strip().split()
        q = words
        temp = len(words)-3
        if len(words)-1 > 0:
            values.append(words[len(words)-1])
            quantities.append(words[len(words)-2])
            q.pop(len(words)-1)
            q.pop(len(words)-1)
            products.append(" ".join(q))
        else:
            continue
print("____________________________________")
zip(products, quantities, values)
for (i,g,k) in zip(products, quantities, values):
    print(i,g,k)


#----parse string to float number before insert the values in mysql DB----
#print(float(money[0].replace(',','.')))
datedtr = " ".join(x)
date_time = datetime.strptime(datedtr, '%d.%m.%Y %H:%M:%S')  # DATE
income = float(money[0].replace(',', '.')) # INCOME
expenses = float(money[1].replace(',', '.')) # EXPENSES
i_cash = float(cs.replace(',', '.')) # CASH
credit_card = float(cc.replace(',', '.')) # CREDIT CARD

quantities_num = list() # QUANTITY
for quantity in quantities:
    quantities_num.append(float(quantity.replace(',', '.')))

values_num = list() # VALUES
for value in values:
    values_num.append(float(value.replace(',', '.')))










input('press any key to exit ')
