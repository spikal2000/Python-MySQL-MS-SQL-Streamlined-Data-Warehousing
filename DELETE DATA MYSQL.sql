USE kalogeri_maindb;
-- DELETE FROM productDetails WHERE product_id IN (SELECT product_id FROM Dproduct_id) ;
-- DELETE FROM products WHERE id IN (SELECT product_id FROM Dproduct_id) ;
-- DELETE FROM sales WHERE id IN (SELECT sales_id FROM Dsales_id) ;
TRUNCATE TABLE Dproduct_id;
TRUNCATE TABLE Dsales_id;
TRUNCATE TABLE productDetails;
TRUNCATE TABLE products;
TRUNCATE TABLE sales;