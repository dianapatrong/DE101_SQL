# Lab 8: Import and Export a DB

### Prerequisites
* Running MySQL engine binded with a client such as DBeaver
* Create a new database called **country_db**
* Create the following tables:

**1. Country**
```
CREATE TABLE country (id int primary key auto_increment, country_name varchar(128), country_name_eng varchar(128), country_code varchar(8));
```

**2.  City**
```
CREATE TABLE city (id int primary key auto_increment, name varchar(128), country_id int, population int, city_size varchar(10));

```

### What You Will Practice
- Import and Export a DB

# Exercises

## Exercise 1
As you know, the tables created are empty! Let's create some entries on them.

1. Create 3 entries for the table **country**

```
INSERT INTO country (country_name, country_name_eng, country_code) VALUES ('Mexico', 'Spanish', 'MEX');
INSERT INTO country (country_name, country_name_eng, country_code) VALUES ('Brasil', 'Portuguese', 'BRA');
INSERT INTO country (country_name, country_name_eng, country_code) VALUES ('United States', 'English', 'USA');
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
SELECT country.country_name_eng, sum(city.population) as people FROM country JOIN city ON country.id = city.country_id GROUP BY 1;
```

## Exercise 2
Now we are going to export the **country_db** into a dump file, to do so, first we have to connect to mysql container

1. Connect to MySQL container

```
docker-compose exec mysql bash
```

Now we are going to export the **country_db** into a dump file by using mysqldump

2. Export DB to a file
```
mysqldump -u root -p country_db > data-dump.sql
```
It will ask the password and use 'secret2'

Now we will see a data-dump.sql is created on the filesystem

3. See data-dump.sql file content

```
cat data-dump.sql
```


## Exercise 3
Now, we will create another database that will be the target database when importing the data

1. Login on mysql console as root user

```
mysql -u root -p
```

It will ask the password and use 'secret2'
 
Now let's create a new database that will be the target db to import the data

2. Create database command within mysql command prompt
```
CREATE DATABASE new_database;
```

3. After **new_database** is created, just exit mysql command prompt with:

```
exit;
```

## Exercise 4

Now, we will import the data by using the **data-dump.sql** into **new_database**

1. Import DB command
```
mysql -u root -p new_database < data-dump.sql
```

It will ask the password and use 'secret2'

Now let's connect to **new_database** and verify data is there

2. How many people speaks which in our **new_database**? 
```
SELECT country.country_name_eng, sum(city.population) as people FROM country JOIN city ON country.id = city.country_id GROUP BY 1;
```

As we can see, now **new_database** is having the records and tables from **country_db** that we exported.