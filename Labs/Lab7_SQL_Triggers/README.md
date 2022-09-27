# Lab 6: Triggers

![Sakila Diagram](documentation_images/sakila_diagram.png)

### Prerequisites
* Running MySQL engine binded with a client such as DBeaver
* Create a new database called **triggers_lab**
* Create the following tables:

**1. Country**
```
CREATE TABLE country (id int, country_name varchar(128), country_name_eng varchar(128), country_code varchar(8));
```

**2.  City**
```
CREATE TABLE city (id int primary key auto_increment, name varchar(128), country_id int, population int, city_size varchar(10));

```

**3. User log**
```
CREATE TABLE user_log (id int, user_id int ,user_name varchar(100), table_affected varchar(100), operation_type varchar(20), operation_time timestamp);
```

**4. DDL operations per user**
```
CREATE TABLE ddl_operations_per_user (id int, user_id int, tables_created int, tables_droped int, tables_altered int);
```

### What You Will Practice
- SQL Triggers

# Exercises

## Exercise 1
As you know, the tables created are empty! Let's create some entries on them.

1. Create 3 entries for the table **country**

```
INSERT INTO country (country_name, lang, country_code) VALUES ('Mexico', 'Spanish', 'MEX');
INSERT INTO country (country_name, lang, country_code) VALUES ('Brasil', 'Portuguese', 'BRA');
INSERT INTO country (country_name, lang, country_code) VALUES ('United States', 'English', 'USA');
```

2. Create 5 entries for the table **city**

```
INSERT INTO city (name, country_id, population, city_size) VALUES ('Puebla', 1, 1692000, 'medium');
INSERT INTO city (name, country_id, population, city_size) VALUES ('Monterrey', 1, 1109000, 'medium');
INSERT INTO city (name, country_id, population, city_size) VALUES ('Rio', 2, 6748000, 'huge');
INSERT INTO city (name, country_id, population, city_size) VALUES ('Los Angeles', 1, 3973000, 'large');
INSERT INTO city (name, country_id, population, city_size) VALUES ('New York', 1, 8380000, 'huge');
```

3. How many people speaks which in our database? 
```
SELECT country.lang, sum(city.population) as people FROM country JOIN city ON country.id = city.country_id GROUP BY 1;
```

The trigger modified the behavior of the insert operation over the table specified.


## Exercise 2
Now we are going to insert a new city. Can you tell what is the problem with this new record?

1. Insert a new city

```
INSERT INTO city (name, country_id, population, city_size) VALUES ('Albuquerque', 3, 560447, 'large');
```

The problem is that Albuquerque is a city with a population of 560,447, but is cataogued as a large city!! something is not ok with the criteria for this last city, right?

To fix this, we'll create a trigger that executes each time an insert operation happens in **city** table. This trigger will implement an standarized criteria for evaluating the cities.

2. Create the trigger
```
CREATE TRIGGER t_city_insert_city_size_standarization BEFORE INSERT ON city
FOR EACH ROW
BEGIN
    IF NEW.population < 100000 THEN SET NEW.city_size = 'small';
    ELSEIF NEW.population BETWEEN 100001 AND 1000000 THEN SET NEW.city_size = 'medium';
    ELSEIF NEW.population BETWEEN 1000001 AND 5000000 THEN SET NEW.city_size = 'large';
    ELSEIF NEW.population > 5000001 THEN SET NEW.city_size = 'huge';
   	END IF;
END;
```
3. Try inserting the same city (albuquerque)

```
INSERT INTO city (name, country_id, population, city_size) VALUES ('Albuquerque', 3, 560447, 'large');
```

4. Select the table
```
SELECT * FROM city;
```

RESULT
```
id|name       |country_id|population|city_size|
--+-----------+----------+----------+---------+
 1|Puebla     |         1|   1692000|medium   |
 2|Monterrey  |         1|   1109000|medium   |
 3|Rio        |         2|   6748000|huge     |
 4|Los Angeles|         1|   3973000|large    |
 5|New York   |         1|   8380000|huge     |
 6|Albuquerque|         3|    560447|large    |
 8|Albuquerque|         3|    560447|medium   |
```

## Exercise 3
Now, we will create another trigger, to validate the reference integrity between tables **country** and **city** in such a way that we cannot add a new city if the provided country id is null or doesn´t exist in the **country** table.

1. Currently, we can add new cities, no matter the country id specified.

```
INSERT INTO city (name, country_id, population, city_size) VALUES ('Paris', null, 2161000, 'small');
```
 
 The database will allow this insertion since we did not create the contraint **not null** when we created the table (on purpose). 

 Now, if we select the table cities, we get the following:

 ```
id|name       |country_id|population|city_size|
--+-----------+----------+----------+---------+
 1|Puebla     |         1|   1692000|medium   |
 2|Monterrey  |         1|   1109000|medium   |
 3|Rio        |         2|   6748000|huge     |
 4|Los Angeles|         1|   3973000|large    |
 5|New York   |         1|   8380000|huge     |
 6|Albuquerque|         3|    560447|large    |
 8|Albuquerque|         3|    560447|medium   |
 9|Paris      |          |   2161000|large    |
 ```

 As we can see, Paris has no country id assigned, which is undesired.

 2. Let's try to assign a value to that id
```
INSERT INTO city (name, country_id, population, city_size) VALUES ('Paris', 4, 2161000, 'small');
```

Now, Paris has assigned a country id
```
id|name       |country_id|population|city_size|
--+-----------+----------+----------+---------+
 1|Puebla     |         1|   1692000|medium   |
 2|Monterrey  |         1|   1109000|medium   |
 3|Rio        |         2|   6748000|huge     |
 4|Los Angeles|         1|   3973000|large    |
 5|New York   |         1|   8380000|huge     |
 6|Albuquerque|         3|    560447|large    |
 8|Albuquerque|         3|    560447|medium   |
 9|Paris      |          |   2161000|large    |
10|Paris      |         4|   2161000|large    |
```

But the problem is that in the country table, country with id 4 does not exist!

```
id|country_name |lang      |country_code|
--+-------------+----------+------------+
 1|Mexico       |Spanish   |MEX         |
 2|Brasil       |Portuguese|BRA         |
 3|United States|English   |USA         |
```
3. We will create a trigger that validates these two scenarios when an insertion happens on **city**

```
CREATE TRIGGER t_city_insert_country_validation BEFORE INSERT ON city
FOR EACH ROW
BEGIN
	DECLARE country_exist int;
    IF new.country_id IS NULL THEN
        signal sqlstate '45000' SET message_text = 'CityInsertTriggerError: No country_id specified';
    ELSEIF new.country_id NOT IN (select id FROM country) THEN
   		signal sqlstate '45000' SET message_text = 'CityInsertTriggerError: country_id specified doesnt exist in country table';
    END IF;
END;
```

4. Now if country_id is **NULL** or it does not exist in **country** table, the insert will fail and MySQL will throw the error that we configured.

```
INSERT INTO city (name, country_id, population, city_size) VALUES ('Paris', null, 2161000, 'small');
```
OUTPUT
```
SQL Error [1644] [45000]: CityInsertTriggerError: No country_id specified
```
```
INSERT INTO city (name, country_id, population, city_size) VALUES ('Paris', 4, 2161000, 'small');
```
OUTPUT
```
SQL Error [1644] [45000]: CityInsertTriggerError: country_id specified doesnt exist in country table
```
5. Let's create the country France

```
INSERT INTO country (country_name, lang, country_code) VALUES ('France', 'French', 'FRA'); 
```

The **country** table looks like this:
```
id|country_name |lang      |country_code|
--+-------------+----------+------------+
 1|Mexico       |Spanish   |MEX         |
 2|Brasil       |Portuguese|BRA         |
 3|United States|English   |USA         |
 4|France       |French    |FRA         |
```
6. Let's try to insert Paris with id 4 once again

```
INSERT INTO city (name, country_id, population, city_size) VALUES ('Paris', 4, 2161000, 'small');
```

Now no errors were thrown, and the city table looks like this:
```
id|name       |country_id|population|city_size|
--+-----------+----------+----------+---------+
 1|Puebla     |         1|   1692000|medium   |
 2|Monterrey  |         1|   1109000|medium   |
 3|Rio        |         2|   6748000|huge     |
 4|Los Angeles|         1|   3973000|large    |
 5|New York   |         1|   8380000|huge     |
 6|Albuquerque|         3|    560447|large    |
 8|Albuquerque|         3|    560447|medium   |
 9|Paris      |          |   2161000|large    |
10|Paris      |         4|   2161000|large    |
11|Paris      |         4|   2161000|large    |
```

## Exercise 4

Now, we will create another trigger, because we want to know who an when deleted records from both, **country** and **city** tables.

For **city**
```
CREATE TRIGGER t_city_log_operations_per_user AFTER DELETE ON city
FOR EACH ROW
BEGIN
    INSERT INTO user_log (user_name, table_affected, operation_type, operation_time) VALUES (current_user(), 'city', 'delete', now());
END;
```

For **country**
```
CREATE TRIGGER t_country_log_operations_per_user AFTER DELETE ON country
FOR EACH ROW
BEGIN
    INSERT INTO user_log (user_name, table_affected, operation_type, operation_time) VALUES (current_user(), 'country', 'delete', now());
END;
```

Let's verify that when we delete some records from **city** it's reflected in **user_log** table.

```
DELETE FROM city WHERE name = 'Paris';
DELETE FROM city WHERE name = 'Albuquerque';
```

```
SELECT * FROM user_log;
```

OUTPUT
```
id|user_name|table_affected|operation_type|operation_time     |
--+---------+--------------+--------------+-------------------+
 1|root@%   |city          |delete        |2022-09-27 05:10:47|
 2|root@%   |city          |delete        |2022-09-27 05:10:47|
 3|root@%   |city          |delete        |2022-09-27 05:10:47|
 4|root@%   |city          |delete        |2022-09-27 05:11:12|
 5|root@%   |city          |delete        |2022-09-27 05:11:12|
```

As we can see, after the records in the city table were deleted, a record for each of those were created in the **user_log** table.