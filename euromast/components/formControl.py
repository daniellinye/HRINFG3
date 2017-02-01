import pygame as pg
import string
import uuid

class Text:
    def __init__(self, position, text, font, color, transparent=1):
        self.text = text
        self.color = color
        self.position_x = position[0]
        self.position_y = position[1]
        self.transparent = transparent
        self.font = font
        self.textRendered = None

    def update_text(self, text):
        self.text = text

    def draw(self, surface):
        self.textRendered = self.font.render(self.text, self.transparent, self.color)
        surface.blit(self.textRendered,
                         (self.position_x - self.textRendered.get_width()*0.5, self.position_y - self.textRendered.get_height()*0.5))


class Image:
    def __init__(self, position, image=None, callback=None):
        self.image = image
        self.callback = callback
        self.rect = self.image.get_rect() if image else None
        self.position_x = position[0]
        self.position_y = position[1]
        self.clicked = False
        self.call_on_release = True

    def scale(self):
        size = self.image.get_rect().size

        self.image = pg.transform.scale(self.image, (int(size[0] / 3), int(size[1] / 3)))
        self.rect = self.image.get_rect()
        self.rect.move_ip(
            self.position_x - self.image.get_rect().size[0]*0.5,
            self.position_y - self.image.get_rect().size[1]*0.5
        )
        return self

    def check_event(self,event):
        """The button needs to be passed events from your program event loop."""
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.on_release(event)

    def on_click(self,event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True
            if not self.call_on_release:
                self.callback()

    def on_release(self,event):
        if self.clicked and self.call_on_release:
            self.callback()
        self.clicked = False

    def draw(self, surface, image=None):
        if image:
            self.image = image
        surface.blit(self.image, (self.position_x - self.image.get_rect().size[0]*0.5,
                                      self.position_y - self.image.get_rect().size[1]*0.5))
class Button(object):
    """A fairly straight forward button class."""
    def __init__(self, rect, color, callback, **kwargs):
        self.rect = pg.Rect(rect)
        self.color = color
        # self.button_id = uuid.uuid4()
        self.callback = callback
        self.clicked = False
        self.hovered = False
        self.hover_text = None
        self.clicked_text = None
        self.process_kwargs(kwargs)
        self.render_text()

    def process_kwargs(self,kwargs):
        """Various optional customization you can change by passing kwargs."""
        settings = {"text" : None,
                    "outline_color": pg.Color('black'),
                    "button_id": uuid.uuid4(),
                    "original_text": None,
                    "font" : pg.font.SysFont("Arial",16),
                    "call_on_release" : True,
                    "hover_color" : None,
                    "clicked_color" : None,
                    "font_color" : pg.Color("white"),
                    "hover_font_color" : None,
                    "clicked_font_color" : None,
                    "click_sound" : pg.mixer.Sound("./assets/sounds/click.wav"),
                    "hover_sound" : None}
        for kwarg in kwargs:
            if kwarg in settings:
                settings[kwarg] = kwargs[kwarg]
            else:
                raise AttributeError("Button has no keyword: {}".format(kwarg))
        if settings['text']:
            settings['original_text'] = settings['text']

        self.__dict__.update(settings)

    def render_text(self):
        """Pre render the button text."""
        if self.text:
            if self.hover_font_color:
                color = self.hover_font_color
                self.hover_text = self.font.render(self.text,True,color)
            if self.clicked_font_color:
                color = self.clicked_font_color
                self.clicked_text = self.font.render(self.text,True,color)
            self.text = self.font.render(self.text,True,self.font_color)
    def update_color(self, color):
        self.color = color
        
    def update_text(self, text):
        self.text = text
        self.render_text()

    def update_font_color(self, color):
        self.font_color = color
        self.text = self.original_text
        self.render_text()

    def update_callback(self, callback):
        self.callback = callback

    def check_event(self,event):
        """The button needs to be passed events from your program event loop."""
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.on_click(event)
        elif event.type == pg.MOUSEBUTTONUP and event.button == 1:
            self.on_release(event)

    def on_click(self,event):
        if self.rect.collidepoint(event.pos):
            self.clicked = True
            if self.click_sound:
                self.click_sound.play()
            if not self.call_on_release:
                self.callback(self.button_id)

    def on_release(self,event):
        if self.clicked and self.call_on_release:
            self.callback(self.button_id)
        self.clicked = False

    def check_hover(self):
        if self.rect.collidepoint(pg.mouse.get_pos()):
            if not self.hovered:
                self.hovered = True
                if self.hover_sound:
                    self.hover_sound.play()
        else:
            self.hovered = False

    def update(self,surface):
        """Update needs to be called every frame in the main loop."""
        color = self.color
        text = self.text
        self.check_hover()
        if self.clicked and self.clicked_color:
            color = self.clicked_color
            if self.clicked_font_color:
                text = self.clicked_text
        elif self.hovered and self.hover_color:
            color = self.hover_color
            if self.hover_font_color:
                text = self.hover_text
        surface.fill(self.outline_color,self.rect)
        surface.fill(color,self.rect.inflate(-4,-4))
        if self.text:
            text_rect = text.get_rect(center=self.rect.center)
            surface.blit(text,text_rect)



ACCEPTED = string.ascii_letters+string.digits+string.punctuation+" "


class TextBox(object):
    def __init__(self,rect,**kwargs):
        self.rect = pg.Rect(rect)
        self.buffer = []
        self.final = None
        self.rendered = None
        self.render_rect = None
        self.render_area = None
        self.blink = True
        self.blink_timer = 0.0
        self.process_kwargs(kwargs)

    def process_kwargs(self,kwargs):
        defaults = {"id" : None,
                    "command" : None,
                    "active" : True,
                    "color" : pg.Color("white"),
                    "font_color" : pg.Color("black"),
                    "outline_color" : pg.Color("black"),
                    "outline_width" : 2,
                    "active_color" : pg.Color("blue"),
                    "font" : pg.font.SysFont("Arial", self.rect.height+4),
                    "clear_on_enter" : False,
                    "inactive_on_enter" : True}
        for kwarg in kwargs:
            if kwarg in defaults:
                defaults[kwarg] = kwargs[kwarg]
            else:
                raise KeyError("InputBox accepts no keyword {}.".format(kwarg))
        self.__dict__.update(defaults)

    def get_event(self,event):
        if event.type == pg.KEYDOWN and self.active:
            if event.key in (pg.K_RETURN,pg.K_KP_ENTER):
                self.execute()
            elif event.key == pg.K_BACKSPACE:
                if self.buffer:
                    self.buffer.pop()
            elif event.unicode in ACCEPTED:
                self.buffer.append(event.unicode)
        elif event.type == pg.MOUSEBUTTONDOWN and event.button == 1:
            self.active = self.rect.collidepoint(event.pos)

    def execute(self):
        if self.command:
            self.command(self.id,self.final)
        self.active = not self.inactive_on_enter
        if self.clear_on_enter:
            self.buffer = []

    def update(self):
        new = "".join(self.buffer)
        if new != self.final:
            self.final = new
            self.rendered = self.font.render(self.final, True, self.font_color)
            self.render_rect = self.rendered.get_rect(x=self.rect.x+2,
                                                      centery=self.rect.centery)
            if self.render_rect.width > self.rect.width-6:
                offset = self.render_rect.width-(self.rect.width-6)
                self.render_area = pg.Rect(offset,0,self.rect.width-6,
                                           self.render_rect.height)
            else:
                self.render_area = self.rendered.get_rect(topleft=(0,0))
        if pg.time.get_ticks()-self.blink_timer > 200:
            self.blink = not self.blink
            self.blink_timer = pg.time.get_ticks()

    def draw(self,surface):
        outline_color = self.active_color if self.active else self.outline_color
        outline = self.rect.inflate(self.outline_width*2,self.outline_width*2)
        surface.fill(outline_color,outline)
        surface.fill(self.color,self.rect)
        if self.rendered:
            surface.blit(self.rendered,self.render_rect,self.render_area)
        if self.blink and self.active:
            curse = self.render_area.copy()
            curse.topleft = self.render_rect.topleft
            surface.fill(self.font_color,(curse.right+1,curse.y,2,curse.h))

# draw some text into an area of a surface
# automatically wraps words
# returns any text that didn't get blitted
def TextInRect(surface, text, color, rect, font, aa=False, bkg=None):
    rect = pg.Rect(rect)
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
