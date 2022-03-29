--UPDATE branch_dim
--INSERT INTO [dbo].[branch_dim](branch_label) SELECT DISTINCT branch FROM [dbo].[staging_Sales];

--UPDATE productName_dim
--INSERT INTO [dbo].[productName_dim] (productName_label) 
--SELECT DISTINCT name FROM [dbo].[staging_products];

--UPDATE date_dim
--INSERT INTO [dbo].[date_dim](date_label)
--SELECT DISTINCT date FROM [dbo].[staging_Sales];


--UPDATE sales_fact
--INSERT INTO [dbo].[sales_fact](id,branch_id,date_id,income,expenses,cash,creditCard)
--SELECT 
--[staging_Sales].[id], 
--[branch_dim].[branch_id], 
--[date_dim].[date_id],
--[staging_Sales].[income],
--[staging_Sales].[expenses],
--[staging_Sales].[cash],
--[staging_Sales].[creditCard]
--FROM staging_Sales
--INNER JOIN [branch_dim] ON [branch_dim].[branch_label] = [staging_Sales].[branch]
--INNER JOIN [date_dim] ON [date_dim].[date_label] = [staging_Sales].[date];

--UPADET product_dim
--INSERT INTO [dbo].[product_dim](id,productName_id,quantity,value)
--SELECT 
--[dbo].[staging_products].[id],
--[dbo].[productName_dim].[productName_id],
--[dbo].[staging_products].[quantity],
--[dbo].[staging_products].[value]
--FROM [dbo].[staging_products]
--INNER JOIN [dbo].[productName_dim] ON [dbo].[productName_dim].[productName_label] = [dbo].[staging_products].[name];

--UPDATE productDetails_dim
--INSERT INTO [dbo].[productDetails_dim](sales_id,product_id)
--SELECT 
--[dbo].[staging_productDetails].[sales_id],
--[dbo].[staging_productDetails].[product_id]
--FROM [dbo].[staging_productDetails];

--TRUNCATE staging tables
--TRUNCATE TABLE [dbo].[staging_products];
--TRUNCATE TABLE [dbo].[staging_Sales];
--TRUNCATE TABLE [dbo].[staging_productDetails];