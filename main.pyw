''' An Arcade Project '''
import pygame
import esquive

#To get the screen values
pygame.init()
screen = pygame.display.set_mode()
SCREEN_WEIGHT, SCREEN_HEIGHT = screen.get_size()
WEIGHT_COEF = round(SCREEN_WEIGHT/1920, 3)
HEIGHT_COEF = round(SCREEN_HEIGHT/1080, 3)
coef = (WEIGHT_COEF, HEIGHT_COEF)
pygame.quit()

pygame.init()
screen = pygame.display.set_mode((SCREEN_WEIGHT//1.5, SCREEN_HEIGHT//1.5))

RUNNING = True
while RUNNING:
    screen.fill((123,123,123))
    for event in pygame.event.get():           
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                RUNNING = False
            elif event.key == pygame.K_a:
                esquive.menu(screen, True, coef)
    pygame.display.update()

pygame.display.quit()
