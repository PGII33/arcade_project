# An Arcade Project
import pygame
import esquive

pygame.init()

screen = pygame.display.set_mode()
pygame.display.set_caption("Arcade ")
SCREEN_WEIGHT, SCREEN_HEIGHT = screen.get_size()
screen = pygame.display.set_mode((SCREEN_WEIGHT, SCREEN_HEIGHT))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                running = False
            elif event.key == pygame.K_a:
                esquive.running = True
                esquive.esquive_game(esquive.running)
    pygame.display.update()

pygame.display.quit()