import mysql.connector


mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="dev123"
)

print(mydb)

mycursor = mydb.cursor()

mycursor.execute(" CREATE DATABASE IF NOT EXISTS `mainDB` ")

mycursor.execute("""

    CREATE TABLE IF NOT EXISTS `mainDB`.`products` (
    `id` INT NOT NULL AUTO_INCREMENT,
    `name` VARCHAR(500) NOT NULL,
    `quantity` FLOAT NOT NULL,
    `value` FLOAT NOT NULL,
    PRIMARY KEY (`id`));

""")

mycursor.execute("""

CREATE TABLE IF NOT EXISTS `mainDB`.`sales` (
  `id` INT NOT NULL AUTO_INCREMENT,
  `branch` VARCHAR(500) NOT NULL,
  `Date` DATETIME NOT NULL,
  `income` FLOAT NOT NULL,
  `expenses` FLOAT NOT NULL,
  `cash` FLOAT NOT NULL,
  `creditCard` FLOAT NOT NULL,
  `product_id` INT NOT NULL,
  PRIMARY KEY (`id`),
  INDEX `FK_sales_products_id__products_id_idx` (`product_id` ASC) VISIBLE,
  CONSTRAINT `FK_sales_products_id__products_id`
    FOREIGN KEY (`product_id`)
    REFERENCES `test`.`products` (`id`)
    ON DELETE NO ACTION
    ON UPDATE NO ACTION);

""")
