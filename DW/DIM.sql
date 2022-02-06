-- PRODUCT NAME DIM
-- INSERT INTO [kalogerisDW].[dbo].[productName] (label_productName) SELECT DISTINCT [name] FROM [kalogerisDW].[dbo].[stagingProducts] 

-- FACT PRODUCTS 
--INSERT INTO [kalogerisDW].[dbo].[Fproducts] (id, name_id, quantity, [value]) 
--SELECT
--[stagingProducts].[id],
--[productName].[id_productName] AS [name],
--[stagingProducts].[quantity],
--[stagingProducts].[value]
--FROM [kalogerisDW].[dbo].[stagingProducts]
--INNER JOIN [dbo].[productName] ON [stagingProducts].[name] = [productName].[label_productName]

-- BRANCH

--INSERT INTO [kalogerisDW].[dbo].[branch](label_branch)
--SELECT DISTINCT branch FROM [dbo].stagingSales

--FACT SALES 

--INSERT INTO [dbo].[fact_sales](id, id_branch, [date], income, expenses, cash, creditCard)
--SELECT 
--[stagingSales].[id],
--[dbo].[branch].[id_branch] AS id_branch,
--[stagingSales].[date],
--[stagingSales].[income],
--[stagingSales].[expenses],
--[stagingSales].[cash],
--[stagingSales].[creditCard]
--FROM [dbo].[stagingSales]
--INNER JOIN [dbo].[branch] ON [branch].label_branch = [stagingSales].[branch]

--F PRODUCT DETAILS

INSERT INTO [dbo].[FproductDetails]( sales_id, product_id)
SELECT [stagingProductDetails].[sales_id], [stagingProductDetails].product_id
FROM [dbo].[stagingProductDetails]