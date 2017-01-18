import pygame

pygame.init()

#TODO init the menu
#TODO make the menu
#TODO have menu switch

class Menu():
    def __init__(self, screen, items, bg_color, font, font_color):
        self.screen = screen
        self.width = self.screen.get_rect().width
        self.height = self.screen.get_rect().height

        self.bg_color = bg_color
        self.fps = pygame.time.Clock()

        self.items = items
        self.font = pygame.font.Font(font, 40)
        self.font_color = font_color

        self.items = []

        for index, item in enumerate(items):
            label = self.font.render(item, 1, font_color)

            width = label.get_rect().width
            height = label.get_rect().width

            x = (self.width / 2) - (width / 2)
            y = (self.height * 0.2 * len(items) + (index * height))
            texth = len(items) * height
            self.items.append([item, label, (width, height, x, y)])

    def run(self):
        running = True
        while running:
            #fps
            self.clock.tick(60)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

            self.screen.fill(self.bg_color)

            for name, label, (width, height), (x, y) in self.items:
                self.screen.blit(label, (x ,y))

            pygame.display.flip()





