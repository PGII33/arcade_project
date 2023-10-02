""" The game where u need to avoid balls """
import pygame as pygame
import display_class as display

running = True

pos = 20, 20

# Display creation
test_button = display.Button((0,0), (20,40),(122,122,122))

def esquive_game(screen:pygame.Surface, running:bool = False)-> None:
    while running :
        print('hey')
        player = pygame.Rect(pos[0], pos[1], 50,50)
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    running = False
        test_button.show(screen)
        pygame.display.update()
