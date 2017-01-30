DROP TABLE IF EXISTS answer;
DROP TABLE IF EXISTS question;
DROP TABLE IF EXISTS category;
DROP TABLE IF EXISTS highscore;

CREATE TABLE IF NOT EXISTS category (
  id serial NOT NULL primary key,
  color VARCHAR(20) NOT NULL,
  name VARCHAR(255) NOT NULL
);

CREATE TABLE IF NOT EXISTS question (
  id serial NOT NULL primary key,
  name VARCHAR(255) NOT NULL,
  category_id INT NOT NULL,
  type VARCHAR(255) NOT NULL,
  constraint fk_question_category
    foreign key (category_id)
    references category(id)
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS answer (
  id serial NOT NULL primary key,
  name VARCHAR(255) NOT NULL,
  question_id INT NOT NULL,
  is_correct BOOLEAN DEFAULT FALSE,
  constraint fk_answer_question
    foreign key (question_id)
    references question(id)
    ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS highscore (
  id serial NOT NULL PRIMARY KEY,
  name VARCHAR(255),
  score INT NOT NULL
);

-- insert categories
INSERT INTO category (id, name, color)
  VALUES (1, 'entertainment', 'tomato'),
         (2, 'sport', 'lightsteelblue'),
         (3, 'historie', 'yellow'),
         (4, 'geografie', 'yellowgreen');

INSERT INTO question (id, name, category_id, type)
  -- category sports - multiple_choice
  VALUES  (1, 'Welke bar in Rotterdam werd in 2009 de beste bar ter wereld benoemd?', 1, 'multiple_choice'),
          (2, 'Hoe heet de bekendste escape room in Rotterdam?', 1, 'multiple_choice'),
          (3, 'Voor welk vervoermiddel is er geen tour door Rotterdam beschikbaar?', 1, 'multiple_choice'),
          (4, 'Welk van de volgende winkels is niet rond de koopgoot?', 1, 'multiple_choice'),
          (5, 'In welke bioscoop vindt het Wildlife Film Festival plaats?', 1, 'multiple_choice');
          -- category sports - open

INSERT INTO answer (name, question_id, is_correct) VALUES
  ('De Witte Aap', 1, TRUE),
  ('Het NRC', 1, FALSE),
  ('Café de Beurs', 1, FALSE),
  ('R’dam Escape', 2, FALSE),
  ('Escape010', 2, TRUE),
  ('Room Escape', 2, FALSE),
  ('Segway', 3, FALSE),
  ('Boot', 3, FALSE),
  ('Auto', 3, TRUE),
  ('H&M', 4, FALSE),
  ('Media Markt', 4, TRUE),
  ('The Sting', 4, FALSE),
  ('Cinerama', 5, True),
  ('Pathé de Kuip', 5, FALSE),
  ('Pathé Schouwburgplein', 5, FALSE);
