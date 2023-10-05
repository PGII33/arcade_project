""" The game where u need to avoid balls """
from random import randint
import pygame

class Player:
    """ The player """
    def __init__(self, pos:list, dim:list) -> None:
        self.pos = pos
        self.dim = dim
        self.rect = pygame.Rect(pos[0], pos[1], dim[0], dim[1])

    def draw(self, screen:pygame.Surface) -> None:
        """ Draw the player """
        self.pos = [round(self.pos[0]), round(self.pos[1])]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.dim[0], self.dim[1])
        pygame.draw.rect(screen, (0,0,0), self.rect)

    def gravity(self, gravity:float) -> None:
        """ Apply gravity to the player """
        self.pos[1] += gravity

class Ennemie:
    ''' Ennemie '''
    def __init__(self, pos:list, dim:list) -> None:
        self.pos = pos
        self.dim = dim
        self.rect = pygame.Rect(pos[0], pos[1], dim[0], dim[1])

    def draw(self, screen:pygame.Surface) -> None:
        """ Draw the ennemie """
        self.pos = [round(self.pos[0]), round(self.pos[1])]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.dim[0], self.dim[1])
        pygame.draw.rect(screen, (255,0,0), self.rect)

def esquive_game(screen:pygame.Surface, running:bool, coef:tuple)-> None:
    ''' In this game u want to avoid enemies falling from the sky '''
    # Variables
    BORDER_LEFT = 0
    BORDER_RIGHT = 1920*coef[0] * 2/3
    BORDER_UP = 0
    BORDER_DOWN = 1080*coef[1] * 2/3
    PLAYER_WIDTH = 50*coef[1]
    PLAYER_HEIGHT = 50*coef[0]
    FPS = 60

    gravity = 1*coef[1]
    mov_speed_x = 10*coef[0]
    mov_speed_y = 5*coef[1]
    elapsed_time = 0
    not_up = 0
    saut_max = 300
    number_of_ennemies_max = 0
    number_of_ennemies = 0

    ennemies = []

    player = Player([1920*coef[0]* 2/6 - PLAYER_WIDTH /2, 1080*coef[1]*2/3  - PLAYER_HEIGHT], [PLAYER_WIDTH, PLAYER_HEIGHT] )
    mov_up = False
    mov_down = False
    mov_left = False
    mov_right = False
    can_up = True

    # Boucle while
    while running :

        # Gestion des fps
        clock = pygame.time.Clock()
        dt = clock.tick(FPS)

        # Gestion des evenements
        screen.fill((120,50,70))
        player.draw(screen)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    running = False
                    menu(screen, True, coef, elapsed_time)
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
                    can_up = False
                if event.key == pygame.K_DOWN:
                    mov_down = False
                if event.key == pygame.K_LEFT:
                    mov_left = False
                if event.key == pygame.K_RIGHT:
                    mov_right = False

        # Gestion des mouvements et des collisions avec les bords et la gravité
        if mov_up and BORDER_UP < player.pos[1] - 1*coef[1] and not_up > -saut_max and can_up:
            player.pos[1] -= (mov_speed_y + gravity)
            not_up -= 10
            if not_up <= -saut_max:
                can_up = False
        if can_up is False and not_up < 0 :
            if player.pos[1] >= round(BORDER_DOWN - PLAYER_HEIGHT) :
                not_up = 0
                can_up = True
        if player.pos[1] == BORDER_DOWN - PLAYER_HEIGHT:
            not_up = 0
        if mov_down and round(BORDER_DOWN - PLAYER_HEIGHT) > player.pos[1] + 1*coef[1]:
            player.pos[1] += mov_speed_y
        if mov_left and BORDER_LEFT < player.pos[0] - 1*coef[0]:
            player.pos[0] -= mov_speed_x
        if mov_right and BORDER_RIGHT - PLAYER_WIDTH > player.pos[0] + 1*coef[0]:
            player.pos[0] += mov_speed_x

        if player.pos[1] < BORDER_DOWN - PLAYER_HEIGHT:
            player.gravity(gravity)

        # Gestion des ennemies
        if number_of_ennemies < number_of_ennemies_max:
            ennemies.append(Ennemie([randint(0, round(BORDER_RIGHT)), 0], [20*coef[0], 20*coef[1]]))
            number_of_ennemies +=1
        for ennemie in ennemies:
            ennemie.draw(screen)
            ennemie.pos[1] += gravity
            if ennemie.pos[1] > BORDER_DOWN:
                ennemies.remove(ennemie)
                number_of_ennemies -= 1
            if ennemie.rect.colliderect(player.rect):
                running = False
                menu(screen, True, coef, elapsed_time)


        elapsed_time += dt

        # Gestion de la difficulté
        if elapsed_time > number_of_ennemies_max*1000 +1000:
            number_of_ennemies_max += 1
            gravity += 0.1*coef[1]

        # Gestion de l'affichage du score en temps réel
        font = pygame.font.Font(None, 36)
        text = font.render(f"Temps écoulé : {elapsed_time / 1000:.2f} secondes", True, (255, 255, 255))
        text_rect = text.get_rect()
        text_rect.center = (200, 50)
        screen.blit(text, text_rect)

        pygame.display.update()

def menu(screen:pygame.Surface, running:bool, coef:tuple, score:str = 'Aucun Score')-> None:
    ''' The menu of the game '''
    # Variables
    score = str(score)
    FPS = 60
    font = pygame.font.Font(None, 36)
    text = font.render("Press A to start", True, (255, 255, 255))
    text_rect = text.get_rect()
    text_rect.center = (1920*coef[0]//3, 1080*coef[1]//3)

    text_score = font.render(score, True, (255, 255, 255))
    text_score_rect = text.get_rect()
    text_score_rect.center = (1920*coef[0]//3, 1080*coef[1]//3 + 50*coef[1])
    # Boucle while
    while running :
        screen.fill((120,50,70))
        screen.blit(text, text_rect)
        screen.blit(text_score, text_score_rect)

        # Gestion des fps
        clock = pygame.time.Clock()
        dt = clock.tick(FPS)

        # Gestion des evenements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    running = False
                elif event.key == pygame.K_a:
                    running = False
                    esquive_game(screen, True, coef)

        pygame.display.update()