import re
import csv


xfile = open("data\DC20220114215917.txt")

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

with open('data\DC20220114215917.txt', 'r') as current:
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
