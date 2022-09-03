# Lab 4: SQL Clauses [Joins, Group by & Union]

In this lab we will practice joins, group by and union clauses by using the mysql `world` sample database. 

### Prerequisites
* [Install docker](https://docs.docker.com/engine/install/) 
* Install a db client (i.e. [DBeaver](https://dbeaver.io/download/)) 
* Install docker compose (only if you are on Linux)

### What You Will Practice
- Joins
- Group by
- Union

# Let's get started
For this lab we will use mysql's `world` sample database, in this folder there's a `docker-compose.yml` file 
and a `world.sql` file, when doing a `docker-compose up -d` it will automatically load the `world.sql` data. 

![World Database ERD](documentation_images/world_erd.png)

## Cheatsheet

You can take a look at the SQL Joins cheat sheet here -> [SQL Joins Cheatsheet](documentation_images/joins-cheat-sheet-a4.pdf)

## Designing a query 

Figure out how to write your SQL queries, the following questions will help you out: 

* Which tables contain the critical data? `**(FROM)**`
* Which columns do I need in the result set? `**(SELECT)**`
* Are there any tables that should be connected? If so, how are they connected `**(JOIN and/or WHERE)**`?
* Do I need to filter any values `**(WHERE)**`?
* Do I need to return only `**DISTINCT**` records?
* Do I care about the order of records returned? If so, which columns do I need to sort by and in what precedence?

# Exercises

## Exercise 1
List the full names of all countries where English is spoken as an official language. Do this as a single query.

> NOTE: Use an inner join

Expected results: 
```commandline
+--------------------------------------+
| name                                 |
+--------------------------------------+
| Anguilla                             |
| American Samoa                       |
| Antigua and Barbuda                  |
| Australia                            |
| Belize                               |
| Bermuda                              |
| Barbados                             |
| Canada                               |
| Cocos (Keeling) Islands              |
...
+--------------------------------------+
44 rows in set (0.00 sec)
```
 
## Exercise 2

Find the list of the countries that do not have any language information in the `countrylanguage` table. 

> NOTE: Use a left join 

Expected results: 
```commandline
+----------------------------------------------+
| name                                         |
+----------------------------------------------+
| Antarctica                                   |
| French Southern territories                  |
| Bouvet Island                                |
| Heard Island and McDonald Islands            |
| British Indian Ocean Territory               |
| South Georgia and the South Sandwich Islands |
+----------------------------------------------+
6 rows in set (0.00 sec)
```

## Exercise 3

Find the name of the countries that do not have information of any city in the `city` table.

> NOTE: Use a right join 

Expected result: 

```commandline
+----------------------------------------------+
| Name                                         |
+----------------------------------------------+
| Antarctica                                   |
| French Southern territories                  |
| Bouvet Island                                |
| Heard Island and McDonald Islands            |
| British Indian Ocean Territory               |
| South Georgia and the South Sandwich Islands |
| United States Minor Outlying Islands         |
+----------------------------------------------+
7 rows in set (0.01 sec)
```

## Exercise 4

Find how many countries does each continent has, list the result in descending order.

Expected result: 
```commandline
+---------------+-------+
| continent     | count |
+---------------+-------+
| Africa        |    58 |
| Asia          |    51 |
| Europe        |    46 |
| North America |    37 |
| Oceania       |    28 |
| South America |    14 |
| Antarctica    |     5 |
+---------------+-------+
7 rows in set (0.00 sec)
```

## Exercise 5

Find the name of the top 10 countries with most official languages. 

Expected result: 
```commandline
+----------------------+---------------+
| name                 | LanguageCount |
+----------------------+---------------+
| Switzerland          |             4 |
| South Africa         |             4 |
| Luxembourg           |             3 |
| Singapore            |             3 |
| Bolivia              |             3 |
| Peru                 |             3 |
| Belgium              |             3 |
| Vanuatu              |             3 |
| Cyprus               |             2 |
| Netherlands Antilles |             2 |
+----------------------+---------------+
10 rows in set (0.00 sec)
```

## Exercise 6

Find the total number of people for each district in Mexico, order your results in descending order. 

Expected results: 
```commandline
+----------------------+------------+
| District             | Population |
+----------------------+------------+
| M�xico               |   10181634 |
| Distrito Federal     |    8591309 |
| Jalisco              |    4015398 |
| Guanajuato           |    3492701 |
| Nuevo Le�n           |    3141441 |
| Veracruz             |    2747405 |
| Baja California      |    2346707 |
...
+----------------------+------------+
33 rows in set (0.00 sec)
```

## Exercise 7

Find the name and surface area of:

* All countries in **Antarctica** 
* Countries which speak Spanish

Order your results in descending order by surface area 

> NOTE: Use the union clause 

Expected result: 
``` commandline
+----------------------------------------------+-------------+
| name                                         | SurfaceArea |
+----------------------------------------------+-------------+
| Antarctica                                   | 13120000.00 |
| Canada                                       |  9970610.00 |
| United States                                |  9363520.00 |
| Argentina                                    |  2780400.00 |
| Mexico                                       |  1958201.00 |
| Peru                                         |  1285216.00 |
| Colombia                                     |  1138914.00 |
...
+----------------------------------------------+-------------+
33 rows in set (0.00 sec)

```