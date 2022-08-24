# Lab 3: SQL Transactions

In this lab we will go side-by-side into executing a transactions example, for that we will create an inventory management
table for Old Navy, which is a store that sells clothing. 

![Transactions Diagram](documentation_images/transaction_diagram.png)

### Prerequisites
* [Install docker](https://docs.docker.com/engine/install/) 
* Install a db client (i.e. [DBeaver](https://dbeaver.io/download/)) 
* Install docker compose (only if you are on Linux)

### What You Will Learn


# Let's get started

The store so far has only products and their orders listed under their database, please look at how they are related in the following
diagram: 

![Lab 3 Diagram](documentation_images/lab3_diagram.png)


## Step 1
Create the `old_navy` database.

## Step 2
Create the `products` and `orders` tables in the `old_navy` database according to the following schema: 

```
CREATE TABLE products (
  id int unsigned NOT NULL AUTO_INCREMENT,
  product_name varchar(70) DEFAULT NULL,
  stock int unsigned DEFAULT NULL,
  PRIMARY KEY (id)
);

CREATE TABLE orders (
  id int unsigned NOT NULL AUTO_INCREMENT,
  product_id int unsigned NOT NULL,
  quantity int unsigned DEFAULT NULL,
  PRIMARY KEY (id),
  FOREIGN KEY (product_id) REFERENCES products (id)
);
```

## Step 3
Now that the tables are created, the manager asks you to update the product inventory with 5 pairs of jeans that arrived in the 
latest shipment: 

```
INSERT INTO products VALUES (NULL, "Jeans", 5);
```

## Step 4
A few hours later, you get an order from **Joey** to buy 10 pairs of jeans, which will be inserted into the `orders` table: 

```
INSERT INTO orders VALUES (NULL, 1, 10);
```

## Step 5
After saving the order into the `orders` table, we will need to update the **stock** for the pairs of jeans in 
the `products` table to reflect the actual number of jeans available: 

```
UPDATE products SET stock = stock - 10 WHERE id = 1;
```

But.. since we only had 5 pairs of jeans in **stock**, MySQL will throw an error saying that the column value is 
out of range: 

```
SQL Error [1690] [22001]: Data truncation: BIGINT UNSIGNED value is out of range in '(`old_navy`.`products`.`stock` - 10)'
```

## Step 6
We need will need to cancel **Joey's** order since we don't have enough jeans in stock to send him, so let's remove the order: 

```
DELETE FROM orders WHERE id = 1;
```

We canceled the order, but we had to run a few extra commands because we saved the new order into the `orders` table before 
the transaction was validated. 

This case is exactly where a transaction can help you...

# Rolling back changes
A `ROLLBACK` statement is used to undo all the changes made on the current transaction if any error occurred during
the execution of a transaction. 

This error can be many of the following: 
- System failure
- Power outage
- Incorrect execution of the transaction
- System crash
- Etc.. 

A `ROLLBACK` command can only be executed if the user has **NOT** performed the `COMMIT` command on the current transaction or statement.

To start a transaction, you need to run the `START TRANSACTION` statement first: 

```
START TRANSACTION; 
```

Now every single statement that you run after that command won't be saved permanently to the database.. yet. 

## Step 1
A few hours later, the store gets another order from **Angela** to buy 8 pairs of jeans, let's insert that order, 
but this time we will use a transaction.

```
START TRANSACTION;
INSERT INTO orders VALUES (NULL, 1, 8);
UPDATE products SET stock = stock - 8 WHERE id = 1;
```

The `UPDATE` statement above still fails because we don’t have 8 pairs of jeans in stock:

```
SQL Error [1690] [22001]: Data truncation: BIGINT UNSIGNED value is out of range in '(`old_navy`.`products`.`stock` - 8)'
```

## Step 2
If you query the `orders` table, you will have a **Angela's**  order record for the 8 pairs of jeans: 

```
mysql> SELECT * FROM orders;
+----+------------+----------+
| id | product_id | quantity |
+----+------------+----------+
|  1 |          1 |       10 |
|  2 |          1 |        8 |
+----+------------+----------+

```

## Step 3
Instead of running a `DELETE` statement, since we are already within a transaction, we can simply `ROLLBACK` the insertion: 

```
ROLLBACK; 
```


## Step 4
If we take a look at our past orders, **Angela's** order for the 8 pairs of jeans is no longer displayed because it was automatically
cancelled when we used the `ROLLBACK` statement. 

```
mysql> SELECT * FROM orders;
+----+------------+----------+
| id | product_id | quantity |
+----+------------+----------+
|  1 |          1 |       10 |
+----+------------+----------+
```

# Committing transaction changes

A `COMMIT` statement  is used to make the current transaction permanent. It shows the successful completion of a transaction. 
Once the `COMMIT` command is executed in the database, we cannot regain its previous states in which it was 
 earlier before the execution of the first statement.

Multiple SQL statements executed within a transaction won't be permanently saved to the database until you run 
a `COMMIT` statement. 


## Step 1: 
Let's think about another scenario, a few days later a third order comes from **Tony** to buy 4 pairs of jeans, this time 
you will add that order to our `orders` table and update the inventory using a transaction.  

```
START TRANSACTION;
INSERT INTO orders VALUES (NULL, 1, 4);
UPDATE products SET stock = stock - 4 WHERE id = 1;
```

The `UPDATE` statement did work this time because we still had 5 pairs of jeans in stock at the time of the order. 

## Step 2: 
Now we can save the changes permanently to the database using the `COMMIT` statement: 

```
COMMIT; 
```

## Step 3
Both changes to the `products` and `orders` table are now saved permanently and **Tony** will get his 4 pairs of jeans.  

```
mysql> SELECT * FROM orders;
+----+------------+----------+
| id | product_id | quantity |
+----+------------+----------+
|  1 |          1 |       10 |
|  3 |          1 |        4 |
+----+------------+----------+
```

```
mysql> SELECT * FROM products;
+----+------------+----------+
| id | product_name | stock  |
+----+--------------+--------+
|  1 |        Jeans |      1 |
+----+--------------+--------+
```
### Why are transactions useful? 

Databases are known for processing millions of concurrent requests per second. In many cases, these requests touch the 
same item within the database. Imagine, for instance, that you are trying to purchase a **limited** supply of your favorite game 
on an online e-commerce site. Suppose everyone in the online store puts the game in their carts at the same time and 
proceed to checkout. In that case, the remaining inventory needs to be calculated accurately (neither over nor under). 
Typically, a database transaction is used in such scenarios.


Now imagine you have many SQL statements that make changes to multiple related tables, let's say you have 10 
related SQL statements, and whenever you are executing them the 9th statement fails and you need to undo any change made
by the previous 8 statements **manually**.
Using a transaction feature will save you from manually doing it, you can leverage the `ROLLBACK` and `COMMIT` statements to 
either undo or save all related changes at once. 
