-- sql script that creates a table users
-- if the table exists, script should not fail
-- script can be executed on any database
-- make an attribute unique directly in schema
CREATE TABLE IF NOT EXISTS users(
id INT AUTO_INCREMENT PRIMARY KEY NOT NULL,
email VARCHAR(255) UNIQUE NOT NULL,
name VARCHAR(255)
);
