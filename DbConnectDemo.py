import mysql.connector


mydb = mysql.connector.connect(
  host="139.162.151.111",
  user="kalogeri_spyros",
  password="vaggosspyros1997"
)

print(mydb)

mycursor = mydb.cursor()

#mycursor.execute(" CREATE DATABASE IF NOT EXISTS `mainDB` ")
#mycursor.execute(" USE kalogeri_maindb; ")

mycursor.execute("""

    CREATE TABLE IF NOT EXISTS `kalogeri_maindb`.`products` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(500) NOT NULL,
    `quantity` FLOAT NOT NULL,
    `value` FLOAT NOT NULL,
    PRIMARY KEY (`id`));

""")
