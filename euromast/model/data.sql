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
  -- category etnertainment - multiple_choice
  VALUES  (1, 'Welke bar in Rotterdam werd in 2009 de beste bar ter wereld benoemd?', 1, 'multiple_choice'),
          (2, 'Hoe heet de bekendste escape room in Rotterdam?', 1, 'multiple_choice'),
          (3, 'Voor welk vervoermiddel is er geen tour door Rotterdam beschikbaar?', 1, 'multiple_choice'),
          (4, 'Welk van de volgende winkels is niet rond de koopgoot?', 1, 'multiple_choice'),
          (5, 'In welke bioscoop vindt het Wildlife Film Festival plaats?', 1, 'multiple_choice'),
          -- category entertainment - open
          (6, 'Wat is de populairste straat in Rotterdam om uit te gaan?', 1, 'open'),
          (7, 'Bij welke brug in Rotterdam bind "Het nationale Vuurwerk" plaats?', 1, 'open'),
          (8, 'Hoe heet het grootste filmfestival in Rotterdam?', 1, 'open'),
          (9, 'Wat is de bekendste dierentuin in Rotterdam?', 1, 'open'),
          (10, 'Welke kunstwerk wordt ook wel de Nederlandse versie van de Sixtijnse Kapel genoemd?', 1, 'open'),
          -- category sports - multiple_choice
          (11, 'In welk jaar startte de Tour de France in Rotterdam?', 2, 'multiple_choice'),
          (12, 'Welke tennistoernooi word er elk jaar in Ahoy gehouden', 2, 'multiple_choice'),
          (13, 'Wat is een hockeyclub uit Rotterdam?', 2, 'multiple_choice'),
          (14, 'Welke manier van sport word het meest beoefend in Rotterdam?', 2, 'multiple_choice'),
          (15, 'Welke Olympiër groeide op in Rotterdam?', 2, 'multiple_choice'),
          (16, 'Wat zijn de drie professionele voetbalclubs uit Roterdam?', 2, 'open'),
          (17, 'Wat is noemt men een ace bij zowel tennis als volleybal?', 2, 'open'),
          (18, 'Welke voetbalclub uit Rotterdam heeft de Euroacup 1 gewonnen?', 2, 'open'),
          (19, 'Hoe noemt men het scoren bij basketbal, waarbij de speler een hoge sprong maakt en de bal in de backet "slaat"?', 2, 'open'),
          (20, 'Vanuit welke lijn moet een speler bij basketbal schieten om een drieputer te scoren?', 2, 'open'),
          -- category history - multiple_choice
          (21, 'Waar dankt Rotterdam zijn naam aan?', 3, 'multiple_choice'),
          (22, 'Wat is het enigste overgebleven middeleeuws gebouw in de binnenstad van Rotterdam', 3, 'multiple_choice'),
          (23, 'Wie is de nachtburgemeester van Rotterdam?', 3, 'multiple_choice'),
          (24, 'Was de eerste metrolijn in Nederland in Rotterdam geopend?', 3, 'multiple_choice'),
          (25, 'Waar stond vroeger de wijk Katendrecht om bekend?', 3, 'multiple_choice'),
          -- category history - open
          (26, 'Hoe heet het schip dat in dienst was van de Holland Amerika Lijn?', 3, 'open'),
          (27, 'Welke in 2002 vermoorde politicus kwam uit Rotterdam?', 3, 'open'),
          (28, 'Wat is de grootste politieke partij van Rotterdam?', 3, 'open'),
          (29, 'Hoe heette het de Loods in het havengebied dat in 1942 als verzamelpunt voor de deportatie van de Joodse inwoners?', 3, 'open'),
          (30, 'In welk voormalig hoofkantoor is Hotel New York gevestigd?', 3, 'open');

INSERT INTO answer (name, question_id, is_correct) VALUES
  -- category entertainment answers
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
  ('Pathé Schouwburgplein', 5, FALSE),
  ('De Witte de Withstraat', 6, TRUE),
  ('Erasmusbrug', 7, TRUE),
  ('Het internationaal Film Festival', 8, TRUE),
  ('Diergaarde Blijdorp', 9, TRUE),
  ('De Markthal', 10, TRUE),
  -- category sports answers
  ('200', 11, FALSE),
  ('2005', 11, FALSE),
  ('2010', 11, TRUE),
  ('ABN AMRO World Tennis Tournament', 12, TRUE),
  ('Ahoy Open', 12, FALSE),
  ('Heineken Open', 12, FALSE),
  ('HVGR', 13, FALSE),
  ('Focus', 13, FALSE),
  ('HC Rotterdam', 13, TRUE),
  ('Fitness', 14, TRUE),
  ('Voetbal', 14, FALSE),
  ('Basketbal', 14, FALSE),
  ('Dorian van Rijsselberghe', 15, FALSE),
  ('Marhinde Verkerk', 15, TRUE),
  ('Edith Bosch', 15, FALSE),
  ('Feyenoord, Sparta Rotterdam en Excelsior Rotterdam', 16, TRUE),
  ('Een niet door de tegenstander aangeraakt, correcte serveerslag', 17, TRUE),
  ('Feyenoord', 18, TRUE),
  ('Dunken', 19, TRUE),
  ('Driepuntslijn', 20, TRUE),
  -- category history answers
  ('Kooplieden hadden dit vroeger bedacht', 21, FALSE),
  ('Aan de rivier de rotte', 21, TRUE),
  ('Er was een dam aangelegd in de maas', 21, FALSE),
  ('De oude haven', 22, FALSE),
  ('VOC magazijn', 22, FALSE),
  ('St. Laurenskerk', 22, TRUE),
  ('Ahmed Aboutaleb', 23, FALSE),
  ('Jules Deelder', 23, TRUE),
  ('Willem Alexander', 23, FALSE),
  ('Waar, in 1968', 24, TRUE),
  ('Niet waar', 24, FALSE),
  ('De beste bakker van de stad was daar gevestigd', 25, FALSE),
  ('De prostituees', 25, TRUE),
  ('De oudste beschermde boom van de stad staat daar', 25, FALSE),
  ('SS Rotterdam, De Rotterdam, Rotterdam', 26, TRUE),
  ('Pim Fortuyn', 27, TRUE),
  ('Leefbaar Rotterdam', 28, TRUE),
  ('Loods24', 29, TRUE),
  ('Holland Amerika Lijn', 30, TRUE);
