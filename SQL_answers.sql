-- Question #1
-- Based on the ERD provided, write a SQL query to find the number of occurrences that an ingredient named “Lobster Ravioli” was sold at each store. Rank the stores by dishes sold with the highest occurrence first.
SELECT Sales.store_id,
    Store.store_name,
    Ingredient.ingredient_name,
    COUNT(Sales.ingredient_id) as num_of_sold
FROM Sales
    INNER JOIN Store ON Sales.store_id = Store.store_id
    INNER JOIN Ingredient ON Sales.ingredient_id = Ingredient.ingredient_id
WHERE Ingredient.ingredient_name = "Lobster Ravioli"
GROUP BY Sales.store_id
ORDER BY COUNT(Sales.ingredient_id) desc;

-- Question #2
-- Revise the query from Question #1 to limit the dataset queried between April 1st, 2021 to May 1st, 2021. Return only the stores that have sold more than 45 Lobster Ravioli dishes.
SELECT Sales.store_id,
    Store.store_name,
    Ingredient.ingredient_name,
    COUNT(Sales.ingredient_id) as num_of_sold
FROM Sales
    INNER JOIN Store ON Sales.store_id = Store.store_id
    INNER JOIN Ingredient ON Sales.ingredient_id = Ingredient.ingredient_id
WHERE Ingredient.ingredient_name = "Lobster Ravioli"
    AND Sales.business_date BETWEEN '2021-04-01' and '2021-05-01'
GROUP BY Sales.store_id
HAVING COUNT(Sales.ingredient_id) > 45
ORDER BY COUNT(Sales.ingredient_id) desc;

-- Question #3
-- Referencing the Sales table, write the corresponding `CREATE` SQL DDL statement. Include and provide justification for any improvements or add-ons as you see fit.
CREATE TABLE Sales (
    sale_id INT NOT NULL AUTO_INCREMENT,
    store_id INT NOT NULL,
    business_date DATE,
    ingredient_id INT NOT NULL,
    sold_price FLOAT,
    PRIMARY KEY (sale_id),
    FOREIGN KEY (store_id) REFERENCES Store(store_id),
    FOREIGN KEY (ingredient_id) REFERENCES Ingredient(ingredient_id)
);

-- No any improvements are needed as I think the tables are normalized, no repeating groups, no redundant data , and the denpendencies are consistent. 