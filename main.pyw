# An Arcade Project
import pygame
import esquive

#To get the screen values

pygame.init()
screen = pygame.display.set_mode()
SCREEN_WEIGHT, SCREEN_HEIGHT = screen.get_size()
WEIGHT_COEF = 1920/SCREEN_WEIGHT
HEIGHT_COEF = 1080/SCREEN_HEIGHT
COEF = (WEIGHT_COEF, HEIGHT_COEF)
pygame.quit()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WEIGHT//2, SCREEN_HEIGHT//2))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                running = False
            elif event.key == pygame.K_a:
                esquive.running = True
                esquive.esquive_game(screen, True, COEF)
    screen.fill((123,123,123))
    pygame.display.update()

pygame.display.quit()