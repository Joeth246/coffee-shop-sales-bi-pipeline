-- ==========================================
-- Bean & Brew Coffee Co.
-- Business Analysis Queries
-- ==========================================

------------------------------------------------
-- 1. View Sample Data
------------------------------------------------

SELECT *
FROM Sales
LIMIT 10;


------------------------------------------------
-- 2. Total Transactions
------------------------------------------------

SELECT COUNT(*) AS TotalTransactions
FROM Sales;


------------------------------------------------
-- 3. Total Revenue
------------------------------------------------

SELECT ROUND(SUM(SalesAmount),2) AS TotalRevenue
FROM Sales;


------------------------------------------------
-- 4. Average Transaction Value
------------------------------------------------

SELECT ROUND(AVG(SalesAmount),2) AS AverageTransaction
FROM Sales;


------------------------------------------------
-- 5. Revenue by Store
------------------------------------------------

SELECT
    StoreLocation,
    ROUND(SUM(SalesAmount),2) AS Revenue
FROM Sales
GROUP BY StoreLocation
ORDER BY Revenue DESC;


------------------------------------------------
-- 6. Transactions by Store
------------------------------------------------

SELECT
    StoreLocation,
    COUNT(*) AS Transactions
FROM Sales
GROUP BY StoreLocation
ORDER BY Transactions DESC;


------------------------------------------------
-- 7. Revenue by Product Category
------------------------------------------------

SELECT
    ProductCategory,
    ROUND(SUM(SalesAmount),2) AS Revenue
FROM Sales
GROUP BY ProductCategory
ORDER BY Revenue DESC;


------------------------------------------------
-- 8. Top 10 Products
------------------------------------------------

SELECT
    ProductName,
    ROUND(SUM(SalesAmount),2) AS Revenue
FROM Sales
GROUP BY ProductName
ORDER BY Revenue DESC
LIMIT 10;


------------------------------------------------
-- 9. Quantity Sold by Product
------------------------------------------------

SELECT
    ProductName,
    SUM(Quantity) AS UnitsSold
FROM Sales
GROUP BY ProductName
ORDER BY UnitsSold DESC;


------------------------------------------------
-- 10. Sales by Customer Type
------------------------------------------------

SELECT
    CustomerType,
    ROUND(SUM(SalesAmount),2) AS Revenue
FROM Sales
GROUP BY CustomerType;


------------------------------------------------
-- 11. Payment Method Usage
------------------------------------------------

SELECT
    PaymentMethod,
    COUNT(*) AS Transactions
FROM Sales
GROUP BY PaymentMethod
ORDER BY Transactions DESC;


------------------------------------------------
-- 12. Monthly Revenue
------------------------------------------------

SELECT
    Month,
    ROUND(SUM(SalesAmount),2) AS Revenue
FROM Sales
GROUP BY Month
ORDER BY Month;


------------------------------------------------
-- 13. Revenue by Weekday
------------------------------------------------

SELECT
    Weekday,
    ROUND(SUM(SalesAmount),2) AS Revenue
FROM Sales
GROUP BY Weekday
ORDER BY Revenue DESC;


------------------------------------------------
-- 14. Peak Sales Hours
------------------------------------------------

SELECT
    Hour,
    COUNT(*) AS Transactions
FROM Sales
GROUP BY Hour
ORDER BY Transactions DESC;


------------------------------------------------
-- 15. Average Discount
------------------------------------------------

SELECT
    ROUND(AVG(DiscountPercent),2) AS AverageDiscount
FROM Sales;


------------------------------------------------
-- 16. Highest Value Transactions
------------------------------------------------

SELECT
    TransactionID,
    StoreLocation,
    ProductName,
    SalesAmount
FROM Sales
ORDER BY SalesAmount DESC
LIMIT 10;


------------------------------------------------
-- 17. Revenue by Payment Method
------------------------------------------------

SELECT
    PaymentMethod,
    ROUND(SUM(SalesAmount),2) AS Revenue
FROM Sales
GROUP BY PaymentMethod
ORDER BY Revenue DESC;


------------------------------------------------
-- 18. Store Performance Summary
------------------------------------------------

SELECT
    StoreLocation,
    COUNT(*) AS Transactions,
    ROUND(SUM(SalesAmount),2) AS Revenue,
    ROUND(AVG(SalesAmount),2) AS AverageSale
FROM Sales
GROUP BY StoreLocation
ORDER BY Revenue DESC;