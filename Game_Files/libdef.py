import pygame
import time


class Background(pygame.sprite.Sprite):
    def __init__(self, image, location):
        # Call Sprite initializer
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(image)
        self.rect = self.image.get_rect()
        self.rect.left, self.rect.top = location


class DrawButton:
    def __init__(self, screen, b_color, t_color, text, b_width, b_height, position_x, position_y):
        self.screen = screen
        self.b_color = b_color
        self.t_color = t_color
        self.text = text
        self.b_width = b_width
        self.b_height = b_height
        self.position_x = position_x
        self.position_y = position_y
        self.clicked = False

        self.font = pygame.font.SysFont("Times", 40)

        self.draw()

    def draw(self, image=""):
        pygame.draw.rect(self.screen, self.b_color or image,
                         [self.position_x - self.b_width*0.5, self.position_y - self.b_height*0.5, self.b_width, self.b_height], 0)
        text = self.font.render(str(self.text), 1, self.t_color)
        self.screen.blit(text, (self.position_x - self.b_width*0.5 + self.b_width*0.5 - text.get_width()*0.5,
                                self.position_y - self.b_height * 0.5 + self.b_height*0.5 - text.get_height()*0.5))

    def collision(self, new_color=(0, 0, 0)):
        # Check for collision with mouse and change background color
        mouse = pygame.mouse.get_pos()
        if (mouse[0] in range(int(self.position_x - self.b_width*0.5), int(self.position_x - self.b_width*0.5 + self.b_width))) \
                and (mouse[1] in range(int(self.position_y - self.b_height * 0.5), int( self.position_y - self.b_height * 0.5 + self.b_height))):
            self.b_color = new_color
            self.draw()

            # If pressed on a button change state
            if pygame.mouse.get_pressed()[0]:
                time.sleep(0.3)
                return True

    def singleclick(self, new_color=(0,0,0)):
        if self.collision(new_color) and self.clicked == False:
            self.clicked = True
            return True
        else:
            return False



def checkCollision(mouse, posX, posY, width, height):
    return (mouse[0] in range(int(posX - width*0.5), int(posX - width*0.5 + width))) \
            and (mouse[1] in range(int(posY - height * 0.5), int(posY - height * 0.5 + height)))

class DrawText:
    def __init__(self, screen, text, color, position_x, position_y, transparent=1):
        self.screen = screen
        self.text = text
        self.color = color
        self.position_x = position_x
        self.position_y = position_y
        self.transparent = transparent

        self.font = pygame.font.SysFont("Times", 40)

        self.draw()

    def draw(self):
        self.text = self.font.render(self.text, self.transparent, self.color)
        self.screen.blit(self.text,
                         (self.position_x - self.text.get_width()*0.5, self.position_y - self.text.get_height()*0.5))



class DrawImage:
    def __init__(self, screen, image, position_x, position_y):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.position_x = position_x
        self.position_y = position_y

        self.draw()

    def draw(self):
        self.screen.blit(self.image, (self.position_x - self.image.get_rect().size[0]*0.5,
                                      self.position_y - self.image.get_rect().size[1]*0.5))

class BaseImage:
    def __init__(self, screen, image, position_x, position_y):
        self.screen = screen
        self.image = pygame.image.load(image)
        self.position_x = position_x
        self.position_y = position_y

    def draw(self):
        self.screen.blit(self.image, (self.position_x - self.image.get_rect().size[0]*0.5,
                                      self.position_y - self.image.get_rect().size[1]*0.5))

class DrawCard(BaseImage):
    def __init__(self, screen, image, posX, postY, cardId):
        super(DrawCard, self).__init__(screen, image, posX, postY)
        size = self.image.get_rect().size
        self.image = pygame.transform.scale(self.image, (int(size[0] / 3), int(size[1] / 3)))
        size = self.image.get_rect().size
        self.cardId =  cardId
        self.width = size[0]
        self.height = size[1]
        self.draw()

    def collision(self):
        mouse = pygame.mouse.get_pos()
        if checkCollision(mouse, self.position_x, self.position_y, self.width, self.height):
            if pygame.mouse.get_pressed()[0]:
                time.sleep(0.3)
                return True

class Player:
    def __init__(self, player_id, name, score, position, roll = 0):
        self.id = player_id
        self.name = name
        self.score = score
        self.position = position
        self.roll = roll
        self.category = 0
        self.x = -1
        self.y = -1
        self.rect = (self.x, self.y)
        #y = 10 because 0,10 is the left bottom of the screen

    def newcategory(self,x):
        self.category = x

    def relocate(self, x, y):
        self.x = x
        self.y = y
        self.location = (x,y)

class Point:
    def __init__(self, x, y, category):
        self.x = x
        self.y = y
        self.category = category
        self.highlight = 0


    def returnx(self):
        return self.x

    def returny(self):
        return self.y

    def returnc(self):
        return self.category

    def drawself(self, screen, width, height, grid_height):
        pygame.draw.rect(screen, (0,0,0), [width/20 + width/4*self.category + width/8*self.x, height/grid_height *self.y + height/50, 8*(1+self.highlight), 8*(1+self.highlight)], 2)

    def highlight(self):
        if self.highlight == 0:
            self.highlight = 1
        else:
            self.highlight = 0

class Sections:
    def __init__(self, screen, width, height, categories=4, grid_width=2, grid_heigth=10):
        self.listc = []
        self.listx = []
        self.listy = []
        self.screen = screen
        #colors are: red, blue, yellow, green
        self.colorlist = ((255,0,0), (0,0,255), (255, 255, 0), (0,255, 0))
        i = 1
        for counter in range(0, 4):
            pygame.draw.rect(self.screen, self.colorlist[counter], [i, 0, width / 4, height], 0)
            i += width / 4
        for category in range(0, categories):
            for x in range(0, grid_width):
                for y in range(0, grid_heigth):
                    Point(x, y, category).drawself(self.screen, width, height, grid_heigth)
                    self.listc.append(self.listx.append(self.listy.append(Point(x, y, category))))

    def drawplayer(self, player = Player()):
        if player.x >= 0 and player.y >= 0:
            self.getpoint(player.category, player.x, player.y)
        else:
            print("Player {} starts".format(player.name))


# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def drawTextInRect(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pygame.Rect(rect)
    y = rect.top
    lineSpacing = -2

    # get the height of the font
    fontHeight = font.size("Tg")[1]

    while text:
        i = 1

        # determine if the row of text will be outside our area
        if y + fontHeight > rect.bottom:
            break

        # determine maximum width of line
        while font.size(text[:i])[0] < rect.width and i < len(text):
            i += 1

        # if we've wrapped the text, then adjust the wrap to the last word
        if i < len(text):
            i = text.rfind(" ", 0, i) + 1

        # render the line and blit it to the surface
        if bkg:
            image = font.render(text[:i], 1, color, bkg)
            image.set_colorkey(bkg)
        else:
            image = font.render(text[:i], aa, color)

        surface.blit(image, (rect.left, y))
        y += fontHeight + lineSpacing

        # remove the text we just blitted
        text = text[i:]

    return text
