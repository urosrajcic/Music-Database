CREATE USER 'music_nerd'@'localhost' IDENTIFIED BY 'music_nerd_pass';
GRANT CREATE, ALTER, DROP, INSERT, UPDATE, DELETE, SELECT, REFERENCES, RELOAD, INDEX, PROCESS, LOCK TABLES
on *.* TO 'music_nerd'@'localhost' WITH GRANT OPTION;

FLUSH PRIVILEGES;

CREATE DATABASE IF NOT EXISTS music_db;