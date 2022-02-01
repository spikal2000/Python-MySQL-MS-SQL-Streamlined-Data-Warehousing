import re
import csv
import tkinter as tk
from tkinter import filedialog

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
        #if word == "Μετρητά":

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



xfile.close()
products = list()
quantitys = list()
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
            quantitys.append(words[len(words)-2])
            q.pop(len(words)-1)
            q.pop(len(words)-1)
            products.append(" ".join(q))
        else:
            continue
print("____________________________________")
zip(products, quantitys, values)
for (i,g,k) in zip(products, quantitys, values):
    print(i,g,k)
input('press any key to exit ')
