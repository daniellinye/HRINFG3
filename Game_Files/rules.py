
class Rules:
    def __init__(self):
        self.rules1 =  "Game Rules \nBefore the game: \n" \
                      "-	There are 2-4 players (age 14+)     \n" \
                      "-	There is a playing board (The Euromast)." \
                      "\n See instructions to know how to put the playing board together.\n \n " \
                      "-	There is an hourglass." \
                      "\n To measure the 50 seconds to answer a question (timer starts when a non-playing player reads the question out loud).\n \n " \
                      "-	There is one dice. The dice includes the numbers 1 to 6, and each number has its own type of question.\n" \
                      " Numbers: 1 – 3 – 5 = open question  (symbol open question  )\n Numbers: 2 – 4 – 6 = multiple choice question (symbol multiple choice question   )\n " \
                      "\n -	There are four different categories, each with its own color and questions:\n " \
                      "Blue = Sports\n " \
                      "Green = Geography\n " \
                      "Red = Entertainment\n " \
                      "Yellow = History\n \n " \
                      "-	Each player chooses a character.\n \n " \
                      "-	Each player rolls the dice and the player with the highest number chooses a category first.\n \n"\
                      "If two or more players throw the highest number, then they will throw the dice again until one of these players has the highest number.\n " \
                      " -	The remaining players choose a category from the remaining categories (only one player per category at the start of the game)\n " \
                      " -	The player who threw the highest number will start the game first. After the first player, the game continues clockwise with the next player.\n " \
                      " -	Players put their characters on the wooden part of the playing board in front of their chosen category.\n Don’t put your character in the first hole.\n \n " \
                      " During the game:\n " \
                      "-	Choose a direction first (left, right, up, down). After choosing a direction throw the dice to determine how many steps you take. (It is only possible to move the character in a horizontal or vertical direction.)\n " \
                      "-numbers 1 and 2 = 1 step in chosen direction\n " \
                      "-numbers 3 and 4 = 2 steps in chosen direction\n " \
                      "-numbers 5 and 6 = 3 steps in chosen direction\n \n " \

        self.rules2 =             "-	There is only one player allowed in a hole. If a player ends up on another players hole, the player who was already on that hole throws a dice. \n" \
                      "The number given after throwing the dice (numbers 1 to 6) is the number the player has to go down.\n \n" \
                      " -	A non-playing player will read the question out loud. Try not to show the answer given on the card. After a question is answered, the question is put aside.\n " \
                      "- If the player gives a wrong answer, doesn’t understand the question or doesn’t give an answer within 50 seconds it will be considered wrong and the turn goes to the next player.\n " \
                      "- If the player answers the question correctly, he/she must move the character the amount of steps in the chosen direction.\n \n " \
                      "-	If a category runs out of questions, move to the category on your right.\n \n \n How to win and what to do after you win:\n " \
                      "-	The character must pass the last hole to win the game. (Hole number 15 is not the end!)\n The game has only one winner.\n \n After you pass the final hole:\n " \
                      "-	Put your character on top of the Euromast and put the flag in your character’s hand.\n \n \n \n Voor het spelen van het spel:\n " \
                      "-	Er zijn 2-4 spelers (leeftijd 14+)\n \n " \
                      "-	Er is een speelbord (De Euromast)\n Zie de instructies om te weten hoe het speelbord in elkaar moet worden gezet.\n \n " \
                      "-	Er is een zandloper.\n Voor het meten van de 50 seconden om een vraag te beantwoorden (de tijd start wanneer een niet-spelende speler de vraag hardop voorleest).\n \n " \
                      "-	Er is één dobbelsteen. De dobbelsteen bevat de nummers 1 t/m 6. Elk nummer heeft zijn eigen soort vraag.\n " \
                      "Cijfers: 1 – 3 – 5 = open vraag  (symbool open vraag  )\n " \
                      "Cijfers: 2 – 4 – 6 = meerkeuze vraag (symbool meerkeuze vraag    )\n \n " \

        self.rules3 =               "-	Er zijn vier verschillende categorieën, elk met zijn eigen kleur en vragen:\n " \
                      "Blauw = Sport\n " \
                      "Groen = Geografie\n " \
                      "Rood = Entertainment\n " \
                      "Geel = Geschiedenis\n \n " \
                      "-	Elke speler kiest zijn poppetje.\n \n " \
                      "-	Elke speler rolt de dobbelsteen, de speler met het hoogste cijfer kiest als eerste zijn/haar categorie.\n " \
                      "Wanneer twee of meer spelers het hoogste cijfer gooien, zullen deze spelers de dobbelsteen nogmaals gooien totdat één van die spelers het hoogste cijfer gooit.\n \n " \
                      "-	De rest van de spelers kiezen een categorie van de overgebleven categorieën (er is maar 1 speler per categorie mogelijk aan het begin van het spel).\n \n " \
                      "-	De speler wie het hoogste cijfer heeft gegooid, zal als eerste beginnen met zijn/haar beurt. Nadat deze speler klaar is met zijn/haar beurt, vervolgt het spel zich met de klok mee.\n " \
                      "\n -	Spelers plaatsen hun poppetjes op het houten deel van het speelbord en voor de gekozen categorie.\n Plaats het poppetje niet in het eerst gaatje.\n \n \n " \
                      "Tijdens het spel:\n " \
                      "-	Kies een als eerst een richting (links, rechts, omhoog, omlaag). Nadat er een richting is gekozen word de dobbelsteen gegooid om te bepalen hoeveel stappen er genomen mogen worden.\n" \
                      " (Het is alleen toegestaan om een poppetje in horizontale of verticale richting te verplaatsen)\n " \
                      "- cijfers 1 en 2 = 1 stap in gekozen richting\n " \
                      "- cijfers 3 en 4 = 2 stappen in gekozen richting\n " \
                      "- cijfers 5 en 6 = 3 stappen in gekozen richting\n \n " \
                      "-	Er is 1 speler per gaatje toegestaan.\n " \

        self.rules4 =               "Als een speler op het gaatje komt waar al een andere speler in staat. Gooit de speler wie al in het gaatje stond een dobbelsteen.\n" \
                      " Het cijfer op de dobbelsteen na het gooien bepaalt het aantal stappen dat de speler omlaag moet.\n \n " \
                      "-	Een niet-spelende speler leest de vraag hardop voor.  Probeer het antwoord op het kaartje niet te laten zien. Nadat een vraag is beantwoord, leg je de vraag weg.\n " \
                      "- Wanneer een speler een fout antwoord geeft, de vraag niet begrijpt of geen antwoord binnen de 50 seconden geeft zal dit fout worden gerekend en gaat de beurt naar de volgende speler.\n " \
                      "- Wanneer een speler de vraag correct beantwoord, zal hij/zij het poppetje verplaatsen met het aantal stappen in de gekozen richting.\n \n " \
                      "-	Als de vragen van een categorie op zijn, verplaatst elke speler op de desbetreffende categorie zijn/haar poppetje naar de categorie rechts van hen.\n \n \n " \
                      "Hoe win je en wat doe je als je gewonnen hebt:\n " \
                      "-	Je poppetje moet het laatste gaatje passeren om het spel te winnen. (Gaatje 15 in niet het einde!)\n " \
                      "Het spel heeft maar één winnaar.\n \n" \
                      " Wanneer je het laatste gaatje passeert:\n " \
                      "-	Plaats je poppetje bovenop de Euromast en plaats de vlag in de hand van je poppetje.\n"

        self.ruleslist = (self.rules1.split("\n"), self.rules2.split("\n"), self.rules3.split("\n"), self.rules4.split("\n"))
