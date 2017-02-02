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
          (31, 'Voor welk museum staat het monument van Zadkine genaamd "De Verwoeste Stad"?', 1, 'multiple_choice'),
          (32, 'Waar geeft de Rotterdam Tours onder andere rondleidingen?', 1, 'multiple_choice'),
          (33, 'Welke van de volgende Pathe bioscopen is niet in Rotterdam?', 1, 'multiple_choice'),
          (34, 'Hoeveel bezoekers zijn er jaarlijks bij de Marathon Rotterdam?', 1, 'multiple_choice'),
          (35, 'Waar kan je niet terecht om te gaan zwemmen?', 1, 'multiple_choice'),
          (36, 'Welke landen kun je behalve Nederland ook in Miniworld Rotterdam zien?', 1, 'multiple_choice'),
          (37, 'Hoe heet de culturele en culinaire ontdekkingstocht door Rotterdam?', 1, 'multiple_choice'),
          (38, 'Welk van de volgende restaurantboten in Rotterdam bestaat niet?', 1, 'multiple_choice'),
          (39, 'Welk van de volgende bioscopen is het oudst?', 1, 'multiple_choice'),
          (40, 'Op welk plein vindt jaarlijks de Najaarskermis Rotterdam plaats?', 1, 'multiple_choice'),
          -- category entertainment - open
          (6, 'Wat is de populairste straat in Rotterdam om uit te gaan?', 1, 'open'),
          (7, 'Bij welke brug in Rotterdam bind "Het nationale Vuurwerk" plaats?', 1, 'open'),
          (8, 'Hoe heet het grootste filmfestival in Rotterdam?', 1, 'open'),
          (9, 'Wat is de bekendste dierentuin in Rotterdam?', 1, 'open'),
          (10, 'Welke kunstwerk wordt ook wel de Nederlandse versie van de Sixtijnse Kapel genoemd?', 1, 'open'),
          (41, 'Bij welke haven in Rotterdam bevindt zich het Drijvend Paviljoen?', 1, 'open'),
          (42, 'Hoe heet het event waarbij zombies door de binnenstad van Rotterdam lopen?', 1, 'open'),
          (43, 'Welk festival in Rotterdam viert seksuele diversiteit?', 1, 'open'),
          (44, 'Met welke boot kun je rondvaren bij de Erasmusbrug?', 1, 'open'),
          (45, 'Welke concertzaal bevindt zich bij Schouwburgplein?', 1, 'open'),
          (46, 'Wat is de bekendste plek in Rotterdam waar je terecht kan voor concerten en evenementen?', 1, 'open'),
          (47, 'In welke maand vinden de Wereldhavendagen plaats?', 1, 'open'),
          (48, 'Bij welk station is het startpunt van de Rotterdam Street Art Route?', 1, 'open'),
          (49, 'Hoe heet het theater dat zich naast Pathe Schouwburgplein bevindt?', 1, 'open'),
          -- category sports - multiple_choice
          (11, 'In welk jaar startte de Tour de France in Rotterdam?', 2, 'multiple_choice'),
          (12, 'Welke tennistoernooi word er elk jaar in Ahoy gehouden', 2, 'multiple_choice'),
          (13, 'Wat is een hockeyclub uit Rotterdam?', 2, 'multiple_choice'),
          (14, 'Welke manier van sport word het meest beoefend in Rotterdam?', 2, 'multiple_choice'),
          (15, 'Welke Olympier groeide op in Rotterdam?', 2, 'multiple_choice'),
          (50, 'Op welke baan vond het WK roeien in 2016 plaats?', 2, 'multiple_choice'),
          (51, 'Voor welke 3 sporten is de Willem Alexander baan het meest geschikt?', 2, 'multiple_choice'),
          (52, 'Op welke positie in het veld speelde Coen Moulijn voor zowel Feyenoord als het Nederlands elftal?', 2, 'multiple_choice'),
          (53, 'Een speler staat bij voetbal in buitenspelpositie als deze...?', 2, 'multiple_choice'),
          (54, 'Hoe heet het stadion van Sparta Rotterdam?', 2, 'multiple_choice'),
          (55, 'Hoelang is de NN Marathon van Rotterdam?', 2, 'multiple_choice'),
          (56, 'Hoeveel spelers staan er per team bij de lacrosse op het veld?', 2, 'multiple_choice'),
          (57, 'In welk jaar is de honkbalclub Neptunes opgericht?', 2, 'multiple_choice'),
          (58, 'Een honkbal is groter dan een softbal.', 2, 'multiple_choice'),
          (59, 'Hoeveel mensen staan er achter de slagman bij honkbal?', 2, 'multiple_choice'),
          -- category sports - open
          (16, 'Wat zijn de drie professionele voetbalclubs uit Roterdam?', 2, 'open'),
          (17, 'Wat is noemt men een ace bij zowel tennis als volleybal?', 2, 'open'),
          (18, 'Welke voetbalclub uit Rotterdam heeft de Euroacup 1 gewonnen?', 2, 'open'),
          (19, 'Hoe noemt men het scoren bij basketbal, waarbij de speler een hoge sprong maakt en de bal in de backet "slaat"?', 2, 'open'),
          (20, 'Vanuit welke lijn moet een speler bij basketbal schieten om een drieputer te scoren?', 2, 'open'),
          (60, 'Welke veldsport wordt in Rotterdam het meest gespeeld?', 2, 'open'),
          (61, 'Hoe heet het centrum voor sport naast de Kuip?', 2, 'open'),
          (62, 'Hoe heet de Formule 1 race in Rotterdam?', 2, 'open'),
          (63, 'Wat is het grootste eendaagse sportevenement in Rotterdam?', 2, 'open'),
          (64, 'Bij welke sport gebruik je een net om de bal in het doel te gooien?', 2, 'open'),
          (65, 'Hoe heet de hoogste Nederlandse basketbal competitie?', 2, 'open'),
          (66, 'Er is en Rotterdamse basketbalclub op het hoogste niveau, hoe heet deze club?', 2, 'open'),
          (67, 'Hoe heet het stadion van de honkbalclub Neptunes?', 2, 'open'),
          (68, 'Hoeveel punten levert een score op vanuit een vrije worp bij basketbal?', 2, 'open'),
          (69, 'Hoe heet de in Rotterdam geboren trainer van de Nederlandse waterpolo dames, die goud won in 2008 op de Olympische spelen?', 2, 'open'),
          -- category history - multiple_choice
          (215, 'Waar dankt Rotterdam zijn naam aan?', 3, 'multiple_choice'),
          (216, 'Wat is het enigste overgebleven middeleeuws gebouw in de binnenstad van Rotterdam?', 3, 'multiple_choice'),
          (217, 'Wie is de nachtburgemeester van Rotterdam?', 3, 'multiple_choice'),
          (218, 'Was de eerste metrolijn in Nederland in Rotterdam geopend?', 3, 'multiple_choice'),
          (219, 'Waar stond vroeger de wijk Katendrecht om bekend?', 3, 'multiple_choice'),
          (220, 'Wanneer is diergaarde Blijdorp geopend?', 3, 'multiple_choice'),
          (221, 'Wat is de officiele naam van de koopgoot?', 3, 'multiple_choice'),
          (222, 'Welk gebouw (gebouwd in 1957) stond symbool voor de wederopbouw van de stad?', 3, 'multiple_choice'),
          (223, 'Hoeveel joden woonden er in Rotterdam voor de Tweede Wereldoorlog?', 3, 'multiple_choice'),
          (224, 'Wat was tijdens de Tweede Wereldoorlog de enige weg naar het centrum die de Duitsers probeerden te bereiken?', 3, 'multiple_choice'),
          (225, 'Rotterdam was tot 1870 een opslag haven, welke producten werden er onder ander opgeslagen?', 3, 'multiple_choice'),
          (226, 'Na 1872 is de stad Rotterdam snel groot geworden, Pieter Caland had een plan om Rotterdam met de zee te verbinden. Hoe noemde hij die verbinding?', 3, 'multiple_choice'),
          (227, 'Door welke architect(en) is de Euromast ontworpen?', 3, 'multiple_choice'),
          (228, 'In welk jaar heeft Rotterdam stadsrechten gekregen?', 3, 'multiple_choice'),
          (229, 'Hoe heette de haven van Rotterdam oorspronkelijk tijdens zijn ontstaan?', 3, 'multiple_choice'),
          -- category history - open
          (200, 'Hoe heet het schip dat in dienst was van de Holland Amerika Lijn?', 3, 'open'),
          (201, 'Welke in 2002 vermoorde politicus kwam uit Rotterdam?', 3, 'open'),
          (202, 'Wat is de grootste politieke partij van Rotterdam?', 3, 'open'),
          (203, 'Hoe heette het de Loods in het havengebied dat in 1942 als verzamelpunt voor de deportatie van de Joodse inwoners?', 3, 'open'),
          (204, 'In welk voormalig hoofkantoor is Hotel New York gevestigd?', 3, 'open'),
          (205, 'Wat is de bekendste Rotterdamse krant?', 3, 'open'),
          (206, 'Waar staat de afkorting van de krant NRC voor?', 3, 'open'),
          (207, 'Welk hoogste kantoorgebouw was toen de eerste van Europa staat in Rotterdam?', 3, 'open'),
          (208, 'Hoe lang duurde de Tweede Wereldoorlog in Nederland?', 3, 'open'),
          (209, 'Welke openbaar vervoersmiddelen heb je in Rotterdam (noem er 5)?', 3, 'open'),
          (210, 'Welke gorilla ontsnapte er in 2007 uit Diergaarde Blijdorp?', 3, 'open'),
          (211, 'Hoe heette de trans-Atlantische verbinding die vertrok vanaf Rotterdam naar Amerika?', 3, 'open'),
          (212, 'Wat zijn de twee bekendste bruggen in Rotterdam?', 3, 'open'),
          (213, 'Hoe heet het beeld dat Ossip Zadkine ontwierp naar aanleiding van het bombardement in Rotterdam? Het is onthuld in 1953 en staat aan de Leuvenhaven naast het Maritiem Museum.', 3, 'open'),
          (214, 'Wat was Erasmus?', 3, 'open'),
          -- category geography - multiple_choice
          (400, 'Welke brug in Rotterdam heeft de volgende bijnaam: De zwaan?', 4, 'multiple_choice'),
          (401, 'Rotterdam is de hoofdstad van Nederland.', 4, 'multiple_choice'),
          (402, 'Rotterdam is de hoofdstad van Zuid-Holland.', 4, 'multiple_choice'),
          (403, 'Rotterdam is de grootste stad van Nederland.', 4, 'multiple_choice'),
          (404, 'De haven van Rotterdam is de grootste haven van Nederland.', 4, 'multiple_choice'),
          (405, 'Wat is het belangrijkste vervoersmiddel in Rotterdam?', 4, 'multiple_choice'),
          (406, 'Hoeveel millimeter regen valt er gemiddeld per jaar in Rotterdam?', 4, 'multiple_choice'),
          (407, 'Hoeveel woningen zijn er ongeveer in Rotterdam?', 4, 'multiple_choice'),
          (408, 'Wat is het oudste gebouw van Rotterdam?', 4, 'multiple_choice'),
          (409, 'Hoeveel mensen maken dagelijks gebruik van het openbaar vervoer in Rotterdam?', 4, 'multiple_choice'),
          (410, 'Wat is de oudste brug van Rotterdam?', 4, 'multiple_choice'),
          (411, 'Rotterdam word ook wel de … genoemd', 4, 'multiple_choice'),
          (412, 'In welke provincie ligt Rotterdam?', 4, 'multiple_choice'),
          (413, 'Hoe heet de grootste rivier waar Rotterdam aan grenst?', 4, 'multiple_choice'),
          (414, 'De afstand tussen Rotterdam is ongeveer?', 4, 'multiple_choice'),
          -- Category geography - open
          (415, 'Hoe groot is Rotterdam, inclusief wateren? (Schat op 50km2 nauwkeurig.)', 4, 'open'),
          (416, 'Hoe hoog is de Euromast? (Schat tot op 5 meter nauwkeurig.)', 4, 'open'),
          (417, 'Wat is het hoogste gebouw van Rotterdam?', 4, 'open'),
          (418, 'Hoe heten de bekendste huizen van Rotterdam?', 4, 'open'),
          (419, 'Hoe heet de berg die in Rotterdam ligt?', 4, 'open'),
          (420, 'Hoe heet het monument dat op een kerstboom had moeten lijken?', 4, 'open'),
          (421, 'Welke stad is groter dan Rotterdam?', 4, 'open'),
          (422, 'Welk klimaat heerst er in Rotterdam?', 4, 'open'),
          (423, 'Noem minimaal 3 deelgemeentes uit Rotterdam.', 4, 'open'),
          (424, 'Welke snel-of-autowegen liggen er langs of door Rotterdam?', 4, 'open'),
          (425, 'Wat is de hoogste brug van Rotterdam?', 4, 'open'),
          (426, 'Hoeveel winkels telt Rotterdam? (Schat tot op 500 winkels nauwkeurig)', 4, 'open'),
          (427, 'Hoeveel auto’s staan er ongeveer geregistreerd in Rotterdam? (Schat tot op 5000 auto’s nauwkeurig)', 4, 'open'),
          (428, 'Wat is de oudste deelgemeente van Rotterdam?', 4, 'open'),
          (429, 'Hoeveel mensen wonen er ongeveer in Rotterdam? (Schat tot op 5000 mensen nauwkeurig.)', 4, 'open');

INSERT INTO answer (name, question_id, is_correct) VALUES
  -- category entertainment answers
  ('De Witte Aap', 1, TRUE),
  ('Het NRC', 1, FALSE),
  ('Cafe de Beurs', 1, FALSE),
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
  ('Pathe de Kuip', 5, FALSE),
  ('Pathe Schouwburgplein', 5, FALSE),
  ('De Witte de Withstraat', 6, TRUE),
  ('Erasmusbrug', 7, TRUE),
  ('Het internationaal Film Festival', 8, TRUE),
  ('Diergaarde Blijdorp', 9, TRUE),
  ('De Markthal', 10, TRUE),
  ('Havenmuseum', 31, FALSE),
  ('Mariniersmuseum', 31, FALSE),
  ('Maritiem museum', 31, TRUE),
  ('De Euromast', 32, FALSE),
  ('Museumplein', 32, FALSE),
  ('De Markthal', 32, TRUE),
  ('Pathe de Kuip', 33, FALSE),
  ('Pathe de Kroon', 33, TRUE),
  ('Pathe Schouwburgplein', 33, FALSE),
  ('925.000 bezoekers', 34, TRUE),
  ('675.000 bezoekers', 34, FALSE),
  ('830.000 bezoekers', 34, FALSE),
  ('Hoek van Holland', 35, FALSE),
  ('Euromast Park', 35, TRUE),
  ('Plaswijckpark', 35, FALSE),
  ('Luxemburg en Belgie', 36, TRUE),
  ('Duitsland en Belgie', 36, FALSE),
  ('Duitsland en Frankrijk', 36, FALSE),
  ('Drive & Eat', 37, FALSE),
  ('Bicycle Diner', 37, FALSE),
  ('Bike & Bite', 37, TRUE),
  ('De Zwanenboot', 38, TRUE),
  ('De Pannenkoekenboot', 38, FALSE),
  ('De Berenboot', 38, FALSE),
  ('Cinerama', 39, FALSE),
  ('Pathe de Kuip', 39, FALSE),
  ('LantarenVenster', 39, TRUE),
  ('Mullerpier', 40, TRUE),
  ('Pier 80', 40, FALSE),
  ('Schouwburgplein', 40, FALSE),
  ('Rotterdamse Rijnhaven', 41, TRUE),
  ('Rotterdam Zombie Walk', 42, TRUE),
  ('Rotterdam Pride', 43, TRUE),
  ('De Spido', 44, TRUE),
  ('De Doelen', 45, TRUE),
  ('Rotterdam Ahoy', 46, TRUE),
  ('September', 47, TRUE),
  ('Centraal Station', 48, TRUE),
  ('Rotterdamse Schouwburg', 49, TRUE),
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
  ('Willem Alexander baan', 50, TRUE),
  ('Beatrix baan', 50, FALSE),
  ('Juliana baan', 50, FALSE),
  ('Watersporten, wielrennen en hardlopen', 51, TRUE),
  ('Voetbal, hockey en basketbal', 51, FALSE),
  ('Fitness, hardlopen en basketbal', 51, FALSE),
  ('Rechtsback', 52, FALSE),
  ('Linksback', 52, FALSE),
  ('Linksbuiten', 52, TRUE),
  ('Zich verder van het doel bevindt dan de keeper.', 53, FALSE),
  ('Zich dichter bij de doellijn van de tegenstander bevindt dan de bal en de vóórlaatste tegenstander.', 53, TRUE),
  ('Zich buiten de lijn van het veld bevindt en de bal in het spel is.', 53, FALSE),
  ('De Toren', 54, FALSE),
  ('Het Kasteel', 54, TRUE),
  ('De Arena', 54, FALSE),
  ('42,125 km', 55, TRUE),
  ('42,450 km', 55, FALSE),
  ('42,680 km', 55, FALSE),
  ('9', 56, FALSE),
  ('10', 56, TRUE),
  ('11', 56, FALSE),
  ('1850', 57, FALSE),
  ('1875', 57, FALSE),
  ('1900', 57, TRUE),
  ('Waar', 58, FALSE),
  ('Niet Waar', 58, TRUE),
  ('Even groot', 58, FALSE),
  ('1', 59, FALSE),
  ('2', 59, TRUE),
  ('3', 59, FALSE),
  ('Voetbal', 60, TRUE),
  ('Topsportcentrum Rotterdam', 61, TRUE),
  ('City racing Rotterdam', 62, TRUE),
  ('De marathon van Rotterdam', 63, TRUE),
  ('Lacrosse', 64, TRUE),
  ('Dutch Basketball League', 65, TRUE),
  ('Forward Lease Rotterdam', 66, TRUE),
  ('Neptunes Familiestadion', 67, TRUE),
  ('1 punt', 68, TRUE),
  ('Robin van Galen', 69, TRUE),
  -- category history answers
  ('SS Rotterdam, De Rotterdam, Rotterdam', 200, TRUE),
  ('Pim Fortuyn', 201, TRUE),
  ('Leefbaar Rotterdam', 202, TRUE),
  ('Loods24', 203, TRUE),
  ('Holland Amerika Lijn', 204, TRUE),
  ('NRC (Handelsblad)', 205, TRUE),
  ('Nieuwe Rotterdamsche Courant', 206, TRUE),
  ('5 jaar (1940-1945)', 207, TRUE),
  ('Het witte Huis', 208, TRUE),
  ('Bus, tram, metro, trein, waterbus', 209, TRUE),
  ('Bokito', 210, TRUE),
  ('Holland Amerika Lijn', 211, TRUE),
  ('Willemsbrug en Erasmusbrug', 212, TRUE),
  ('De verwoeste stad', 213, TRUE),
  ('Filosoof, humanist, auteur, priester', 214, TRUE),
  ('Kooplieden hadden dit vroeger bedacht ', 215, FALSE),
  ('Aan de rivier de rotte', 215, TRUE),
  ('Er was een dam aangelegd in de maas', 215, FALSE),
  ('De oude haven', 216, FALSE),
  ('VOC magazijn', 216, FALSE),
  ('St. Laurenskerk', 216, TRUE),
  ('Ahmed Aboutaleb ', 217, FALSE),
  ('Jules Deelder', 217, TRUE),
  ('Willem Alexander', 217, FALSE),
  ('Waar, in 1968 ', 218, TRUE),
  ('Niet waar', 218, FALSE),
  ('De beste bakker van de stad was daar gevestigd', 219, FALSE),
  ('De prostituees ', 219, TRUE),
  ('De oudste beschermde boom van de stad staat daar', 219, FALSE),
  ('1855', 220, TRUE),
  ('1975', 220, FALSE),
  ('1915', 220, FALSE),
  ('De ondergrondse winkelstraat', 221, FALSE),
  ('Beurstraverse', 221, TRUE),
  ('Gewoon de koopgoot', 221, FALSE),
  ('De Bijenkorf', 222, TRUE),
  ('De Kubuswoningen', 222, FALSE),
  ('The red apple', 222, FALSE),
  ('ca. 5000', 223, FALSE),
  ('ca. 8000', 223, FALSE),
  ('ca. 12000', 223, TRUE),
  ('De nieuwe Binnenweg', 224, FALSE),
  ('Maasbrug', 224, TRUE),
  ('Koninginnenbrug', 224, FALSE),
  ('Suiker', 225, TRUE),
  ('Wol', 225, TRUE),
  ('Cacao', 225, FALSE),
  ('De Nieuwe Waterweg', 226, TRUE),
  ('De Maas zeeverbinding', 226, FALSE),
  ('Het Nieuwe Water kanaal', 226, FALSE),
  ('Maaskant', 227, TRUE),
  ('Brinkman en van der Vlugt', 227, FALSE),
  ('c. Koolhaas', 227, FALSE),
  ('1250', 228, FALSE),
  ('1340 ', 228, TRUE),
  ('1590', 228, FALSE),
  ('Waalhaven', 229, TRUE),
  ('De Maashaven', 229, FALSE),
  ('Europoort', 229, FALSE),
  -- category geography answers
  ('De Willemsbrug', 400, FALSE),
  ('De Erasmusbrug', 400, TRUE),
  ('De van Briennenoordbrug', 400, FALSE),
  ('Waar', 401, FALSE),
  ('Niet waar', 401, TRUE),
  ('Waar', 402, FALSE),
  ('Niet waar', 402, TRUE),
  ('Waar', 403, TRUE),
  ('Niet waar', 403, FALSE),
  ('Waar', 404, TRUE),
  ('Niet waar', 404, FALSE),
  ('Metro', 405, TRUE),
  ('Auto', 405, FALSE),
  ('Fiets', 405, FALSE),
  ('760 tot 780mm', 406, FALSE),
  ('780 tot 800mm', 406, FALSE),
  ('800 tot 820mm', 406, TRUE),
  ('150.000', 407, FALSE),
  ('300.000', 407, TRUE),
  ('450.000', 407, FALSE),
  ('Kerktoren hillegondakerk', 408, TRUE),
  ('St. Laurenskerk.', 408, FALSE),
  ('Stadhuis van Rotterdam', 408, FALSE),
  ('800.000', 409, FALSE),
  ('900.000', 409, FALSE),
  ('1.000.000', 409, TRUE),
  ('De Willemsbrug', 410, FALSE),
  ('De Koninginnebrug', 410, TRUE),
  ('De van Briennenoordbrug', 410, FALSE),
  ('Stad der wonderen', 411, FALSE),
  ('Stad der steden', 411, FALSE),
  ('Haven stad', 411, TRUE),
  ('Noord-Holland', 412, FALSE),
  ('Zuid-Holland', 412, TRUE),
  ('Noord-Brabant', 412, FALSE),
  ('De Maas', 413, TRUE),
  ('De Rijn', 413, FALSE),
  ('De Waal', 413, FALSE),
  ('50 tot 60km', 414, FALSE),
  ('60 tot 70km', 414, FALSE),
  ('70 tot 80km', 414, TRUE),
  ('319,4', 415, TRUE),
  ('185', 416, TRUE),
  ('De Maastoren', 417, TRUE),
  ('De kubuswoningen', 418, TRUE),
  ('Rotterdam heeft geen bergen', 419, TRUE),
  ('Kabouter buttplug, Santa Claus', 420, TRUE),
  ('Geen, Rotterdam is de grootste stad van Nederland', 421, TRUE),
  ('Gematigd zeeklimaat', 422, TRUE),
  ('Rotterdam Centrum, Charlois, Delfshaven, Feijenoord, Hillegersberg, Schiebroek, Hoek van Holland, Hoogvliet, IJsselmonde, Kralingen-Crooswijk, Noord, Overschie, Pernis, Prins Alexander, Rozenburg', 423, TRUE),
  ('A13, A15, A16, A20.', 424, TRUE),
  ('De Erasmusbrug', 425, TRUE),
  ('9455', 426, TRUE),
  ('200.000', 427, TRUE),
  ('Rotterdam-Noord', 428, TRUE),
  ('610.000', 429, TRUE);

INSERT INTO highscore (id, name, score) VALUES
    (1, 'Monne', 100),
    (2, 'Oscar', 90),
    (3, 'Jasper', 80),
    (4, 'Daniel', 70),
    (5, 'Monne', 60),
    (6, 'Oscar', 50),
    (7, 'Jasper', 40),
    (8, 'Daniel', 30),
    (9, 'Monne', 20),
    (10, 'Oscar', 10);
