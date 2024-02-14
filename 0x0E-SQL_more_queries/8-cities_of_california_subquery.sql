--  script that lists all the cities of California that can be found in the database hbtn_0d_usa.
-- The states table contains only one record where name = California (but the id can be different, as per the example) Results must be sorted in ascending order by cities.id
-- You are not allowed to use the JOIN keyword The database name will be passed as an argument of the mysql command

SELECT c.id, c.name FROM states s,cities c WHERE s.id = c.state_id AND s.name = 'California' ORDER BY c.id ASC;