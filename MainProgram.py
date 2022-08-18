import re
import csv
from tkinter import *
from tkinter import filedialog
from datetime import datetime
import mysql.connector


#Asking the user for file

root = Tk()
root.geometry("500x300")
root.title("DataEntry")

def branch_1():
    global branch
    branch = "branch_1"
    global file_path
    file_path = filedialog.askopenfilename()
    start(branch, file_path)
    root.config(bg = 'green')
    root.after(4000, lambda: root.config(bg = "white"))
    Button1.config(state=DISABLED)#ACTIVE

def branch_2():
    global branch
    branch = "branch_2"
    global file_path
    file_path = filedialog.askopenfilename()
    start(branch, file_path)
    root.config(bg = 'green')
    root.after(4000, lambda: root.config(bg = "white"))
    Button2.config(state=DISABLED)

def branch_3():
    global branch
    branch = "branch_3"
    global file_path
    file_path = filedialog.askopenfilename()
    start(branch, file_path)
    root.config(bg = 'green')
    root.after(4000, lambda: root.config(bg = "white"))
    Button3.config(state=DISABLED)

# Buttons and Button Style
Button1 = Button(root, text="Branch_1", command = branch_1)
Button1.config(font=('Ink Free', 20, 'bold'))
Button1.config(bg='#bf9000')
Button1.pack()

Button2 = Button(root, text="Branch_2", command = branch_2)
Button2.config(font=('Ink Free', 20, 'bold'))
Button2.config(bg='#bf9000')
Button2.pack()

Button3 = Button(root, text="Branch_3", command = branch_3)
Button3.config(font=('Ink Free', 20, 'bold'))
Button3.config(bg='#bf9000')
Button3.pack()

def start(branch, file_path):
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
            if (word == "ΠΙΣΤΩΤΙΚΗ" or word == "ΚΑΡΤΑ"):
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
    #print(len(card))
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


    #----parse strings to float numbers and date to DateTime before insert the values in mysql DB----
    #print(float(money[0].replace(',','.')))
    #branch = "Ελληνικό"
    # datedtr = " ".join(x)
    # print(x[0])
    date_time = datetime.strptime(x[0], '%d.%m.%Y')  # DATE %d.%m.%Y %H:%M:%S
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


    #_______________________DataBase Connection_______________________
    mydb = mysql.connector.connect(
      host="localhost",
      user="root",
      password=""
    )

    print(mydb)

    mycursor = mydb.cursor()


    mycursor.execute("""

        CREATE TABLE IF NOT EXISTS `main_db`.`products` (
      `id` INT NOT NULL AUTO_INCREMENT,
      `name` VARCHAR(500) NULL,
      `quantity` FLOAT NULL,
      `value` DECIMAL(16,2) NULL,
      PRIMARY KEY (`id`))
    ENGINE = InnoDB
    DEFAULT CHARACTER SET = greek;
    """)

    mycursor.execute("""

    CREATE TABLE IF NOT EXISTS `main_db`.`sales` (
      `id` INT NOT NULL AUTO_INCREMENT,
      `branch` VARCHAR(500) NULL,
      `date` DATE NULL,
      `income` DECIMAL(16,2) NULL,
      `expenses` DECIMAL(16,2) NULL,
      `cash` DECIMAL(16,2) NULL,
      `creditCard` DECIMAL(16,2) NULL,
      PRIMARY KEY (`id`))
      ENGINE = InnoDB
      DEFAULT CHARACTER SET = greek;


    """)

    mycursor.execute("""

    CREATE TABLE IF NOT EXISTS `main_db`.`productDetails` (
      `sales_id` INT NOT NULL,
      `product_id` INT NOT NULL,
      INDEX `FK_sales_id__productDeatils_sales_id_idx` (`sales_id` ASC),
      INDEX `FK_products_id__productDetails_products_id_idx` (`product_id` ASC),
      CONSTRAINT `FK_sales_id__productDeatils_sales_id`
        FOREIGN KEY (`sales_id`)
        REFERENCES `main_db`.`sales` (`id`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION,
      CONSTRAINT `FK_products_id__productDetails_products_id`
        FOREIGN KEY (`product_id`)
        REFERENCES `main_db`.`products` (`id`)
        ON DELETE NO ACTION
        ON UPDATE NO ACTION)
        ENGINE = InnoDB
        DEFAULT CHARACTER SET = greek;



    """)

    mycursor.execute("""

    CREATE TABLE IF NOT EXISTS `main_db`.`Dproduct_id` (
      `product_id` INT NOT NULL);

    """)

    mycursor.execute("""

    CREATE TABLE IF NOT EXISTS `main_db`.`Dsales_id` (
      `sales_id` INT NOT NULL);

    """)

    mycursor.execute("""
        INSERT INTO `main_db`.`sales`(`branch`, `Date`, `income`, `expenses`,
        `cash`, `creditCard`)
        VALUES(%s, %s, %s, %s, %s, %s)
    """, (branch, date_time, income, expenses, i_cash, credit_card))
    mydb.commit()

    sales_id = mycursor.lastrowid

    mycursor.execute("""

        INSERT INTO `main_db`.`Dsales_id`(`sales_id`)
        VALUES ( %s )

    """,(sales_id,))
    mydb.commit()
    for i in range(len(products)):
        #print(products[i], quantities_num[i], values_num[i])

        name1 = products[i]
        quantity1 = quantities_num[i]
        value1 = values_num[i]

        mycursor.execute("""
            INSERT INTO `main_db`.`products`(`name`, `quantity`, `value`)
            VALUES (%s, %s, %s); """, (name1, quantity1, value1) )

        mydb.commit()
        product_id = mycursor.lastrowid
        mycursor.execute("""

            INSERT INTO `main_db`.`productDetails`(`sales_id`, `product_id`)
            VALUES ( %s, %s )

            """, (sales_id, product_id))
        mydb.commit()

        mycursor.execute("""

            INSERT INTO `main_db`.`Dproduct_id`(`product_id`)
            VALUES ( %s )

        """,(product_id,))
        mydb.commit()
root.mainloop()
