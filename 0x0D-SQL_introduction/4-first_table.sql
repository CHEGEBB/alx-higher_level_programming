-- a script that creates a table called first_table in the current database in your MySQL server.
-- The table will have two columns: id and name.
-- The database name will be passed as an argument of the mysql command

CREATE TABLE IF NOT EXISTS first_table (
    id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(256) NOT NULL
);
