# 0x0E-SQL_more_queries

This repository contains SQL scripts that demonstrate various queries and operations on a MySQL database. The scripts are designed to be executed on Ubuntu 20.04 LTS using MySQL 8.0 (version 8.0.25). Each script focuses on specific tasks related to database management and query operations.

## Project Overview

The project covers the following topics and tasks:

- Managing MySQL users and privileges
- Creating databases and tables
- Working with constraints (PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE)
- Retrieving data from multiple tables using JOIN and subqueries
- Using various SQL techniques (UNION, DISTINCT)
- Importing SQL dumps
- Performing advanced queries on a TV shows database

## Project Structure

1. **0-privileges.sql**: Lists all privileges of MySQL users `user_0d_1` and `user_0d_2` on the localhost.

    ```bash
    cat 0-privileges.sql | mysql -hlocalhost -uroot -p
    ```

2. **1-create_user.sql**: Creates a MySQL server user `user_0d_1` with all privileges.

    ```bash
    cat 1-create_user.sql | mysql -hlocalhost -uroot -p
    ```

3. **2-create_read_user.sql**: Creates a database `hbtn_0d_2` and a user `user_0d_2` with SELECT privilege on the database.

    ```bash
    cat 2-create_read_user.sql | mysql -hlocalhost -uroot -p
    ```

4. **3-force_name.sql**: Creates a table `force_name` with specified columns and constraints.

    ```bash
    cat 3-force_name.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
    ```

5. **4-never_empty.sql**: Creates a table `id_not_null` with a default value for the `id` column.

    ```bash
    cat 4-never_empty.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
    ```

6. **5-unique_id.sql**: Creates a table `unique_id` with a unique constraint on the `id` column.

    ```bash
    cat 5-unique_id.sql | mysql -hlocalhost -uroot -p hbtn_0d_2
    ```

7. **6-states.sql**: Creates a database `hbtn_0d_usa` and a table `states` with specified columns and constraints.

    ```bash
    cat 6-states.sql | mysql -hlocalhost -uroot -p
    ```

8. **7-cities.sql**: Creates a table `cities` with specified columns and a foreign key constraint.

    ```bash
    cat 7-cities.sql | mysql -hlocalhost -uroot -p
    ```

9. **8-cities_of_california_subquery.sql**: Lists all cities of California without using the JOIN keyword.

    ```bash
    cat 8-cities_of_california_subquery.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
    ```

10. **9-cities_by_state_join.sql**: Lists all cities and their respective states using the JOIN keyword.

    ```bash
    cat 9-cities_by_state_join.sql | mysql -hlocalhost -uroot -p hbtn_0d_usa
    ```

11. **10-genre_id_by_show.sql**: Lists shows and their genre IDs from the `hbtn_0d_tvshows` database.

    ```bash
    cat 10-genre_id_by_show.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
    ```

12. **11-genre_id_all_shows.sql**: Lists all shows with their genre IDs or NULL if no genre is linked.

    ```bash
    cat 11-genre_id_all_shows.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
    ```

13. **12-no_genre.sql**: Lists shows without a linked genre.

    ```bash
    cat 12-no_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
    ```

14. **13-count_shows_by_genre.sql**: Displays the number of shows linked to each genre.

    ```bash
    cat 13-count_shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
    ```

15. **14-my_genres.sql**: Lists all genres of the show "Dexter".

    ```bash
    cat 14-my_genres.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
    ```

16. **15-comedy_only.sql**: Lists all Comedy shows.

    ```bash
    cat 15-comedy_only.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
    ```

17. **16-shows_by_genre.sql**: Lists all shows and their linked genres.

    ```bash
    cat 16-shows_by_genre.sql | mysql -hlocalhost -uroot -p hbtn_0d_tvshows
    ```

## Usage

1. Clone the repository:

    ```bash
    git clone https://github.com/waltertaya/alx-higher_level_programming/0x0E-SQL_more_queries.git
    ```

2. Navigate to the project directory:

    ```bash
    cd 0x0E-SQL_more_queries
    ```

3. Execute the desired SQL script using the provided commands.

Note: Ensure that MySQL 8.0 is installed on your system, and you have the necessary privileges to create users, databases, and tables.

## Author

This project was created by Guillaume for the ALX Higher Level Programming program.
