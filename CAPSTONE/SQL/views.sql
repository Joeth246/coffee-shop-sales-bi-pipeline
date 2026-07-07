DROP VIEW IF EXISTS vw_store_performance;

CREATE VIEW vw_store_performance AS

SELECT

    StoreLocation,

    COUNT(*) AS TotalTransactions,

    SUM(Quantity) AS UnitsSold,

    ROUND(SUM(SalesAmount),2) AS Revenue,

    ROUND(AVG(SalesAmount),2) AS AverageSale

FROM Sales

GROUP BY StoreLocation;