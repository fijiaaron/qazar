--SQLITE SPECIFIC
CREATE DATABASE prototype.sqlite

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS comments;
DROP TABLE IF EXISTS topics;
DROP TABLE IF EXISTS links;
DROP TABLE IF EXISTS comment_topics;
DROP TABLE IF EXISTS comment_links;

create table users (
	id INTEGER PRIMARY KEY AUTOINCREMENT,	
	name varchar(100),
	email varchar(100)
);

CREATE TABLE comments (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	comment text,
	author_id INT REFERENCES users(id),
	created TIMESTAMP,
	updated TIMESTAMP
);

CREATE TABLE topics (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	name VARCHAR(255)
);

create table links (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	description varchar(255),
	url varchar(255)
);

CREATE TABLE comment_topics (
	comment_id INTEGER NOT NULL REFERENCES comments(id),
	topic_id INTEGER NOT NULL REFERENCES topics(id)
);

CREATE TABLE comment_links (
	comment_id INTEGER NOT NULL REFERENCES comments(id),
	link_id INTEGER NOT NULL REFERENCES links(id)
);
