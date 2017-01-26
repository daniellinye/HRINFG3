
    2dice_roll = toDraw.draw1_1(players[counter - 1])
    if 2dice_roll:
        2dice_click = toDraw.draw1_5()




else:
    dice_click = toDraw.draw1_5()
    if dice_click:
        rollbuttonscreen = True
        counter += 1
else:
order = toDraw.draw1_3(players)
if order:
    counter = 0
    state = 1.3