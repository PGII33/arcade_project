""" The game where u need to avoid balls """
import pygame as pygame
import display_class as display

class Player:
    """ The player """
    def __init__(self, pos:list, dim:list):
        self.pos = pos
        self.dim = [0,0,dim[0],dim[1]]
        self.rect = pygame.Rect(pos[0], pos[1], self.dim[2]-self.dim[0], self.dim[3]-self.dim[1])
    
    def draw(self,screen:pygame.Surface):
        """ Draw the player """
        pygame.draw.rect(screen, (0,0,0), self.rect)

def esquive_game(screen:pygame.Surface, running:bool, coef:tuple)-> None:

    # Initialisation des variables
    player = Player([1920*coef[0]//2, 1080*coef[1]//2], [20*coef[0], 20*coef[1]])
    mov_up = False
    mov_down = False
    mov_left = False
    mov_right = False

    # Boucle while
    while running :
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
        
        # Gestion des mouvements
        if mov_up:
            player.pos[1] -= 1*coef[1]
        if mov_down:
            player.pos[1] += 1*coef[1]
        if mov_left:
            player.pos[0] -= 1*coef[0]
        if mov_right:
            player.pos[0] += 1*coef[0]

        print(player.pos, player.dim)
        pygame.display.update()
