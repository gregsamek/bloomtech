import sqlite3

conn = sqlite3.connect('northwind_small.sqlite3')
curs = conn.cursor()

expensive_items = "SELECT * FROM Product ORDER BY UnitPrice DESC LIMIT 10;"

avg_hire_age = "SELECT AVG(HireDate - BirthDate) FROM Employee"

ten_most_expensive = """
SELECT ProductName, UnitPrice, CompanyName
FROM Product JOIN Supplier
ON Product.SupplierID = Supplier.Id
ORDER BY UnitPrice DESC
LIMIT 10
"""

largest_category = """
SELECT CategoryName, COUNT(DISTINCT Product.Id)
FROM Product
JOIN Category
ON Product.CategoryID = Category.Id
GROUP BY CategoryID
ORDER BY COUNT(*) DESC
LIMIT 1
"""
