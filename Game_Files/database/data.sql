CREATE TABLE IF NOT EXISTS question (
  id serial NOT NULL primary key,
  name VARCHAR(255) NOT NULL,
  category_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS answer (
  id serial NOT NULL primary key,
  name VARCHAR(255) NOT NULL,
  question_id INT NOT NULL
);

CREATE TABLE IF NOT EXISTS category (
  id serial NOT NULL primary key,
  name VARCHAR(255) NOT NULL
);
