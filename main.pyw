''' An Arcade Project '''
import pygame
import esquive

#To get the screen values

pygame.init()
screen = pygame.display.set_mode()
SCREEN_WEIGHT, SCREEN_HEIGHT = screen.get_size()
WEIGHT_COEF = SCREEN_WEIGHT/1920
HEIGHT_COEF = SCREEN_HEIGHT/1080
coef = (WEIGHT_COEF, HEIGHT_COEF)
pygame.quit()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WEIGHT//2, SCREEN_HEIGHT//2))

RUNNING = True
while RUNNING:
    screen.fill((123,123,123))
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                RUNNING = False
            elif event.key == pygame.K_a:
                esquive.esquive_game(screen, True, coef)
    pygame.display.update()

pygame.display.quit()
