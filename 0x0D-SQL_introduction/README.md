# Project 0x0D. SQL - Introduction

## Introduction

This project focuses on understanding and applying fundamental concepts of SQL using MySQL. The tasks cover various aspects, including database creation, table manipulation, data insertion, and querying. The learning objectives include mastering key SQL commands, database management, and comprehension of relational databases.

## Learning Objectives

Upon completing this project, you should be able to:

- Explain the concepts of databases and relational databases.
- Define SQL and MySQL.
- Create databases in MySQL.
- Understand and use DDL (Data Definition Language) and DML (Data Manipulation Language) statements.
- Execute commands to create, alter, select, insert, update, and delete data in tables.
- Work with subqueries and MySQL functions.

## Project Structure

The project directory contains the following files:

1. **0-list_databases.sql**
   - Task: List all databases on the MySQL server.
   - Usage: `cat 0-list_databases.sql | mysql -hlocalhost -uroot -p`

2. **1-create_database_if_missing.sql**
   - Task: Create a database named hbtn_0c_0 if it doesn't exist.
   - Usage: `cat 1-create_database_if_missing.sql | mysql -hlocalhost -uroot -p`

3. **2-remove_database.sql**
   - Task: Delete the database hbtn_0c_0 if it exists.
   - Usage: `cat 2-remove_database.sql | mysql -hlocalhost -uroot -p`

4. **3-list_tables.sql**
   - Task: List all tables in a specified database.
   - Usage: `cat 3-list_tables.sql | mysql -hlocalhost -uroot -p [database_name]`

5. **4-first_table.sql**
   - Task: Create a table named first_table with specified columns in the current database.
   - Usage: `cat 4-first_table.sql | mysql -hlocalhost -uroot -p [database_name]`

6. **5-full_table.sql**
   - Task: Print the full description of the table first_table.
   - Usage: `cat 5-full_table.sql | mysql -hlocalhost -uroot -p [database_name]`

7. **6-list_values.sql**
   - Task: List all rows of the table first_table.
   - Usage: `cat 6-list_values.sql | mysql -hlocalhost -uroot -p [database_name]`

8. **7-insert_value.sql**
   - Task: Insert a new row into the table first_table.
   - Usage: `cat 7-insert_value.sql | mysql -hlocalhost -uroot -p [database_name]`

9. **8-count_89.sql**
   - Task: Display the number of records with id = 89 in the table first_table.
   - Usage: `cat 8-count_89.sql | mysql -hlocalhost -uroot -p [database_name] | tail -1`

10. **9-full_creation.sql**
    - Task: Create a table second_table and add specified rows.
    - Usage: `cat 9-full_creation.sql | mysql -hlocalhost -uroot -p [database_name]`

11. **10-top_score.sql**
    - Task: List all records of the table second_table, ordered by score.
    - Usage: `cat 10-top_score.sql | mysql -hlocalhost -uroot -p [database_name]`

12. **11-best_score.sql**
    - Task: List records with a score >= 10 in the table second_table.
    - Usage: `cat 11-best_score.sql | mysql -hlocalhost -uroot -p [database_name]`

13. **12-no_cheating.sql**
    - Task: Update the score of Bob to 10 in the table second_table.
    - Usage: `cat 12-no_cheating.sql | mysql -hlocalhost -uroot -p [database_name]`

14. **13-change_class.sql**
    - Task: Remove all records with a score <= 5 in the table second_table.
    - Usage: `cat 13-change_class.sql | mysql -hlocalhost -uroot -p [database_name]`

15. **14-average.sql**
    - Task: Compute the score average of all records in the table second_table.
    - Usage: `cat 14-average.sql | mysql -hlocalhost -uroot -p [database_name]`

16. **15-groups.sql**
    - Task: List the number of records with the same score in the table second_table.
    - Usage: `cat 15-groups.sql | mysql -hlocalhost -uroot -p [database_name]`

17. **16-no_link.sql**
    - Task: List all records of the table second_table without rows without a name value.
    - Usage: `cat 16-no_link.sql | mysql -hlocalhost -uroot -p [database_name]`

## Instructions for Running the Scripts

1. Make sure you have MySQL 8.0 installed on Ubuntu 20.04 LTS.
2. Use the provided commands and replace `[database_name]` with the actual database name.

## Conclusion

This project provides hands-on experience with MySQL, allowing you to grasp fundamental SQL concepts and practice essential commands for database management. Ensure to understand each task and its associated script, and feel free to explore additional SQL functionalities to enhance your skills. Happy coding!
