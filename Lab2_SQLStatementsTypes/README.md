# Lab 2: SQL Statement Types [DDL & DML]

In this lab, your main goal is to create a cinema database within a docker container, create the table to hold information
regarding the movies and manipulate the data within it. 

### Prerequisites
* [Install docker](https://docs.docker.com/engine/install/) 
* [Install pgAdmin](https://www.pgadmin.org/download/)
* Install docker compose (only if you are on Linux)

### What You Will Learn
* 
*

## Let's get started

1. Create a `cinema` database

2. Write the DDL command to create the table `movie` using the following schema: 

| COLUMN_NAME      | DATA_TYPE(SIZE) |
| :--------------: | :-------------: |
| id               | int(10)         |
| title            | varchar(50)     |
| genre            | varchar(20)     |
| year             | int(4)          |


3. Now let's insert some data into our table according to the following information: 

| id  | title                                    | genre     | year |
|:---:|:----------------------------------------:|:---------:|:----:|
| 1   | Harry Potter and the Philosopher's Stone | fantasy   | 2001 |
| 2   | Top Gun                                  | action    | 1986 |
| 3   | One Piece Film: Red                      | adventure | 2022 |
| 4   | Harry Potter and the Chamber of Secrets  | fantasy   | 2002 |
| 5   | Harry Potter and the Prisoner of Azkaban | fantasy   | 2004 |
| 6   | Harry Potter and the Goblet of Fire      | fantasy   | 2005 |
| 7   | Thor: Ragnarok                           | action    | 2017 |
| 8   | The Perks of Being a Wallflower          | drama     | 2012 |
| 9   | Beauty and the Beast                     | romance   | 2017 |
| 10  | The Greatest Showman                     | musical   | 2017 |


4. Get all the Harry Potter movies and their released year. 

5. Add a new column of a suitable data type named `is_based_on_book` with a suitable default value. 

6. Update the value of the new column `is_based_on_book` to reflect that all the Harry Potter movies are based on books. 

7. Delete all movies that were released between 2002 and 2005 (inclusive)

8. Get all the movies titles which genre is action

9. Remove the `genre` column from the table

10. Get all the titles that contain the letter `K` (case-insensitive) in the title.
