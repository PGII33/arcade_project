""" The game where u need to avoid balls """
import pygame as pygame

class Player:
    """ The player """
    def __init__(self, pos:list, dim:list):
        self.pos = pos
        self.dim = dim
        self.rect = pygame.Rect(pos[0], pos[1], dim[0], dim[1])

    def draw(self,screen:pygame.Surface):
        """ Draw the player """
        self.pos = [round(self.pos[0]), round(self.pos[1])]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.dim[0], self.dim[1])
        pygame.draw.rect(screen, (0,0,0), self.rect)

def esquive_game(screen:pygame.Surface, running:bool, coef:tuple)-> None:
    ''' In this game u want to avoid enemies falling from the sky '''
    # Variables
    BORDER_LEFT = 0
    BORDER_RIGHT = 1920*coef[0] * 2/3
    BORDER_UP = 0
    BORDER_DOWN = 1080*coef[1] * 2/3
    PLAYER_WIDTH = 50*coef[1]
    PLAYER_HEIGHT = 100*coef[0]
    
    mov_speed_x = 10*coef[0]
    mov_speed_y = 10*coef[1]
    
    player = Player([1920*coef[0]* 2/6 - PLAYER_WIDTH /2, 1080*coef[1]*2/3  - PLAYER_HEIGHT], [PLAYER_WIDTH, PLAYER_HEIGHT] )
    mov_up = False
    mov_down = False
    mov_left = False
    mov_right = False

    # Boucle while
    while running :
        
        # Gestion des fps
        clock = pygame.time.Clock()
        clock.tick(60)
        
        # Gestion des evenements
        screen.fill((120,50,70))
        player.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    running = False
                if event.key == pygame.K_UP:
                    mov_up = True
                if event.key == pygame.K_DOWN:
                    mov_down = True
                if event.key == pygame.K_LEFT:
                    mov_left = True
                if event.key == pygame.K_RIGHT:
                    mov_right = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    mov_up = False
                if event.key == pygame.K_DOWN:
                    mov_down = False
                if event.key == pygame.K_LEFT:
                    mov_left = False
                if event.key == pygame.K_RIGHT:
                    mov_right = False

        # Gestion des mouvements et des collisions
        if mov_up and BORDER_UP < player.pos[1] - 1*coef[1]:
            player.pos[1] -= mov_speed_y
        if mov_down and BORDER_DOWN - PLAYER_HEIGHT > player.pos[1] + 1*coef[1] :
            player.pos[1] += mov_speed_y
        if mov_left and BORDER_LEFT < player.pos[0] - 1*coef[0]:
            player.pos[0] -= mov_speed_x
        if mov_right and BORDER_RIGHT - PLAYER_WIDTH > player.pos[0] + 1*coef[0]:
            player.pos[0] += mov_speed_x

        pygame.display.update()
