""" The game where u need to avoid balls """
import pygame as pygame
import display_class as display

def esquive_game(screen:pygame.Surface, running, coef)-> None:
    test_button = display.Button((0,0), (20,40),(122,122,122))
    pos = 20*coef[0], 20*coef[1]
    while running :
        player = pygame.Rect(pos[0], pos[1], 50*coef[0],50*coef[1])
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    running = False
        test_button.show(screen)
        screen.fill((120,50,70))
        pygame.display.update()
