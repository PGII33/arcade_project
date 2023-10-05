''' A module about Button, Text and others - PGII '''
import pygame

class ButtonText:
    ''' This class is about showing button whith text '''

    def __init__(self, coords: tuple, dim: tuple, color: tuple, text: str = None,
                 font_size: int = 10, font_type: str = 'Arial',
                 text_color: tuple = (0, 0, 0), offset: int = 10) -> None:
        ''' The colors are in RGB '''
        assert isinstance(coords, tuple), 'coords needs to be a tuple'
        assert isinstance(dim, tuple), 'dim needs to be a tuple'
        assert isinstance(coords[0], int), 'pos_x needs to be an int'
        assert isinstance(coords[1], int), 'pos_y needs to be an int'
        assert isinstance(dim[0], int), 'width needs to be an int'
        assert isinstance(dim[1], int), 'height needs to be an int'
        assert isinstance(
            text, str) or text is None, 'Text needs to be an str or None'
        assert isinstance(text_color, tuple), 'Text_color needs to be a tuple'
        assert isinstance(
            text_color[0], int), 'text_color[0] needs to be an int'
        assert isinstance(
            text_color[1], int), 'text_color[1] needs to be an int'
        assert isinstance(
            text_color[2], int), 'text_color[2] needs to be an int'
        assert isinstance(font_size, int), 'font_size needs to be an int'
        assert isinstance(offset, int), 'offset needs to be an int'

        self.pos_x, self.pos_y = coords
        self.width = dim[0]
        self.height = dim[1]
        self.font_size = font_size
        self.font = pygame.font.SysFont(font_type, font_size)
        self.text_color = text_color
        self.text = text
        self.color = color
        self.offset = offset
        self.button = self.__create_button(self.color)
        self.hoverlight_button = self.__transparence(self.color)
        self.rect = self.button.get_rect()
        self.rect[0], self.rect[1] = self.pos_x, self.pos_y
        self.clicked = False

    def __transparence(self, color) -> pygame.surface.Surface:
        ''' Make trancparency '''
        surface = self.__create_button(color)
        surface.set_alpha(200)
        return surface

    def __create_button(self, color: tuple) -> pygame.surface.Surface:
        ''' Create a surface '''
        surface = pygame.Surface((self.width, self.height))
        surface.fill(color)
        return surface

    def is_hover(self) -> bool:
        ''' Return a boolean that answer the question is mouse hover surface ?'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def is_click(self) -> bool:
        ''' Return a boolean that answer the question is there a click ?'''
        if pygame.mouse.get_pressed()[0] and not self.clicked:
            self.clicked = True
            return True
        elif not pygame.mouse.get_pressed()[0]:
            self.clicked = False
            return False

    def draw(self, surface) -> bool:
        ''' Show the button '''
        if self.is_hover():
            surface.blit(self.hoverlight_button, (self.pos_x, self.pos_y))
        else:
            surface.blit(self.button, (self.pos_x, self.pos_y))
        if self.text is not None:
            surface.blit(self.font.render(
                self.text, True, self.text_color), (self.pos_x + self.offset, self.pos_y))
        if self.is_click() and self.is_hover():
            return True
        return False

class TextInteract:
    ''' A class about Text with Interaction '''

    def __init__(self, pos_x, pos_y, text, text_color, text_height, text_font) -> None:
        ''' Init '''
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.text = str(text)
        self.text_color = text_color
        self.text_height = text_height
        self.text_font = text_font
        self.font = pygame.font.SysFont(self.text_font, self.text_height)
        self.width = len(self.text) * 15
        self.rect = pygame.Rect(self.pos_x, self.pos_y,
                                self.width, self.text_height)
        self.clicked = False

    def draw(self, surface)-> bool:
        ''' Draw the text '''
        action = False
        pos = pygame.mouse.get_pos()
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked :
                self.clicked = True
                action = True
            if not pygame.mouse.get_pressed()[0] :
                self.clicked = False
        surface.blit(self.font.render(self.text, True, self.text_color), (self.pos_x,self.pos_y))
        return action

class Text:
    ''' A class about Text '''

    def __init__(self, pos_x, pos_y, text, text_color, text_height, text_font) -> None:
        ''' Init '''
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.text = str(text)
        self.text_color = text_color
        self.text_height = text_height
        self.text_font = text_font
        self.font = pygame.font.SysFont(self.text_font, self.text_height)
        self.width = len(str(text)) * 15
        self.rect = pygame.Rect(self.pos_x, self.pos_y,
                                self.width, self.text_height)

    def draw(self, surface) -> None:
        ''' Draw the text '''
        surface.blit(self.font.render(self.text, True,
                     self.text_color), (self.pos_x, self.pos_y))

class Button:
    ''' This class is about showing button '''

    def __init__(self, coords: tuple, dim: tuple, color: tuple) -> None:
        ''' The colors are in RGB '''
        assert isinstance(coords, tuple), 'coords needs to be a tuple'
        assert isinstance(dim, tuple), 'dim needs to be a tuple'
        assert isinstance(coords[0], int), 'pos_x needs to be an int'
        assert isinstance(coords[1], int), 'pos_y needs to be an int'
        assert isinstance(dim[0], int), 'width needs to be an int'
        assert isinstance(dim[1], int), 'height needs to be an int'

        self.pos_x, self.pos_y = coords
        self.width = dim[0]
        self.height = dim[1]
        self.color = color
        self.button = self.__create_button(self.color)
        self.hoverlight_button = self.__transparence(self.color)
        self.rect = self.button.get_rect()
        self.clicked = False

    def __transparence(self, color) -> pygame.surface.Surface:
        ''' Make trancparency '''
        surface = self.__create_button(color)
        surface.set_alpha(200)
        return surface

    def __create_button(self, color: tuple) -> pygame.surface.Surface:
        ''' Create a surface '''
        surface = pygame.Surface((self.width, self.height))
        surface.fill(color)
        return surface

    def is_hover(self) -> bool:
        ''' Return a boolean that answer the question is mouse hover surface ?'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def is_click(self) -> bool:
        ''' Return a boolean that answer the question is there a click ?'''
        if pygame.mouse.get_pressed()[0] and not self.clicked:
            self.clicked = True
            return True
        elif not pygame.mouse.get_pressed()[0]:
            self.clicked = False
            return False

    def draw(self, surface) -> bool:
        ''' Show the button '''
        if self.is_hover():
            surface.blit(self.hoverlight_button, (self.pos_x, self.pos_y))
        else:
            surface.blit(self.button, (self.pos_x, self.pos_y))
        if self.is_click() and self.is_hover():
            return True
        return False

class Bar:
    ''' A class to create some Bar '''

    def __init__(self, coords: tuple, dim: tuple, value: float, max_value: float,
                 main_color: tuple = (255, 0, 0), bg_color: tuple = (0, 0, 0),
                 border_color: tuple = (122, 122, 122)) -> None:

        assert isinstance(coords, tuple), 'coords needs to be a tuple'
        assert isinstance(dim, tuple), 'dim needs to be a tuple'
        assert isinstance(coords[0], int), 'pos_x needs to be an int'
        assert isinstance(coords[1], int), 'pos_y needs to be an int'
        assert isinstance(dim[0], int), 'width needs to be an int'
        assert isinstance(dim[1], int), 'height needs to be an int'
        assert isinstance(value, int) or isinstance(
            value, float), 'value needs to be an int or a float'
        assert isinstance(max_value, int) or isinstance(
            max_value, float), 'max_value needs to be an int or a float'
        assert isinstance(main_color, tuple), 'main_color needs to be a tuple'
        assert isinstance(
            main_color[0], int) and 0 <= main_color[0] <= 255, 'main_color[0] needs to be a int between 0 and 255'
        assert isinstance(
            main_color[1], int) and 0 <= main_color[1] <= 255, 'main_color[1] needs to be a int between 0 and 255'
        assert isinstance(
            main_color[2], int) and 0 <= main_color[2] <= 255, 'main_color[2] needs to be a int between 0 and 255'
        assert isinstance(bg_color, tuple), 'bg_color needs to be a tuple'
        assert isinstance(
            bg_color[0], int) and 0 <= bg_color[0] <= 255, 'bg_color[0] needs to be a int between 0 and 255'
        assert isinstance(
            bg_color[1], int) and 0 <= bg_color[1] <= 255, 'bg_color[1] needs to be a int between 0 and 255'
        assert isinstance(
            bg_color[2], int) and 0 <= bg_color[2] <= 255, 'bg_color[2] needs to be a int between 0 and 255'
        assert isinstance(
            border_color, tuple), 'border_color needs to be a tuple'
        assert isinstance(
            border_color[0], int) and 0 <= border_color[0] <= 255, 'border_color[0] needs to be a int between 0 and 255'
        assert isinstance(
            border_color[1], int) and 0 <= border_color[1] <= 255, 'border_color[1] needs to be a int between 0 and 255'
        assert isinstance(
            border_color[2], int) and 0 <= border_color[2] <= 255, 'border_color[2] needs to be a int between 0 and 255'

        self.pos_x, self.pos_y = coords
        self.width, self.height = dim
        self.main_color = main_color
        self.bg_color = bg_color
        self.border_color = border_color
        self.value = value
        self.max_value = max_value

    def draw(self, surface):
        ''' Show the bar '''
        actual_value = round(self.width * self.value / self.max_value, 90)
        if self.value > self.max_value:
            actual_value = self.width
        elif self.value < 0:
            actual_value = 0
        pygame.draw.rect(surface, self.bg_color, pygame.Rect(self.pos_x,
                                                             self.pos_y, self.width, self.height))
        pygame.draw.rect(surface, self.border_color,
                         pygame.Rect(self.pos_x, self.pos_y,
                                     self.width, self.height, border_radius=3))
        pygame.draw.rect(surface, self.main_color, pygame.Rect(self.pos_x,
                                                               self.pos_y,
                                                               actual_value, self.height))

class ImageButton:
    ''' This class is about showing Image button '''

    def __init__(self, coords: tuple, dim: tuple, path: str) -> None:
        ''' path -> to the image'''
        assert isinstance(coords, tuple), 'coords needs to be a tuple'
        assert isinstance(coords[0], int), 'coords[0] needs to be a int'
        assert isinstance(coords[1], int), 'coords[1] needs to be a int'
        assert isinstance(dim, tuple), 'dim needs to be a tuple'
        assert isinstance(dim[0], int), 'dim[0] needs to be a int'
        assert isinstance(dim[1], int), 'dim[1] needs to be a int'
        assert isinstance(path, str), 'path needs to be a int'

        self.pos_x, self.pos_y = coords
        self.path = path
        self.width = dim[0]
        self.height = dim[1]
        self.image = self.__image()
        self.image_transp = self.__transparence(self.image)
        self.rect = self.image.get_rect()
        self.rect[0] = self.pos_x
        self.rect[1] = self.pos_y
        self.rect[2] = self.pos_x + self.width
        self.rect[3] = self.pos_y + self.height
        self.clicked = False

    def __transparence(self, image) -> pygame.surface.Surface:
        ''' Make trancparency '''
        surface = image
        surface.set_alpha(200)
        return surface

    def __image(self) -> pygame.surface.Surface:
        image = pygame.image.load(self.path).convert_alpha()
        image = pygame.transform.scale(image, (self.width, self.height))
        return image

    def is_hover(self) -> bool:
        ''' Return a boolean that answer the question is mouse hover surface ?'''
        if self.rect.collidepoint(pygame.mouse.get_pos()):
            return True
        return False

    def is_click(self) -> bool:
        ''' Return a boolean that answer the question is there a click ?'''
        if pygame.mouse.get_pressed()[0] and not self.clicked:
            self.clicked = True
            return True
        elif not pygame.mouse.get_pressed()[0]:
            self.clicked = False
            return False

    def draw(self, surface) -> bool:
        ''' Show the button '''
        if self.is_hover():
            surface.blit(self.image_transp, (self.pos_x, self.pos_y))
        else:
            surface.blit(self.image, (self.pos_x, self.pos_y))
        if self.is_click() and self.is_hover():
            return True
        return False

class Entry:
    ''' A class about entry '''
    def __init__(self, pos:tuple, dim:list = (100,50) , text:str = '', text_color:tuple = (125,125,255), text_height:int = None, text_font = 'segoeuisemibold' )-> None :
        self.pos = pos
        self.text = text
        self.dim = list(dim)
        if len(self.text) * 15 > self.dim[0]:
            self.dim[0] = len(self.text) * 15
        self.text_color = text_color
        if text_height is not None:
            self.dim[1] = text_height
        self.text_font = text_font
        self.font = pygame.font.SysFont(self.text_font, self.dim[1])
        self.rect = pygame.Rect(self.pos[0], self.pos[1],
                        self.dim[0], self.dim[1])
        self.clicked = False

    def actualise(self, surface, event) -> None:
        ' actualise the text '
        new_text = self.text
        print(self.text, new_text)
        if event.key == pygame.K_BACKSPACE and len(new_text) >0:
            new_text = new_text[:-1]
            surface.blit(self.font.render(new_text, True, self.text_color), (self.pos[0],self.pos[1]))
        elif event.key is not pygame.K_ESCAPE and event.key is not pygame.K_RETURN :
            new_text += event.unicode
        else:
            self.clicked = False
        self.text = new_text
        if len(self.text) * 15 > self.dim[0]:
            self.dim[0] = len(self.text) * 15
        return

    def draw(self,surface)-> bool:
        ' draw the text '
        action = False
        pos = pygame.mouse.get_pos()
        if pygame.mouse.get_pressed()[0] and self.clicked :
            self.clicked = False
        if self.rect.collidepoint(pos):
            if pygame.mouse.get_pressed()[0] and not self.clicked :
                self.clicked = True
                action = True
        surface.blit(self.font.render(self.text, True, self.text_color), (self.pos[0],self.pos[1]))
        return action
