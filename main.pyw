''' An Arcade Project '''
import pygame
import esquive
import pong
import snake
import display_class as dis

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

Button_esquive_game = dis.ButtonText((round(10*coef[0]), round(10*coef[0])),
                                     (round(150*coef[0]), round(30*coef[1])),
                                     (198, 170, 120),
                                     "Esquive Game",
                                     round(20*coef[0]))
Button_pong_game = dis.ButtonText((round(10*coef[0]), round(50*coef[0])),
                                  (round(150*coef[0]), round(30*coef[1])),
                                  (198, 170, 120),
                                  "Pong Game",
                                  round(20*coef[0]))
RUNNING = True
while RUNNING:
    screen.fill((123,123,123))
    if Button_esquive_game.draw(screen):
        esquive.menu(screen, True, coef)
    if Button_pong_game.draw(screen):
        pong.pong(screen, True, coef)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            RUNNING = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_e:
                RUNNING = False
            elif event.key == pygame.K_a:
                snake.snake(screen, True, coef)
    pygame.display.update()

pygame.display.quit()
pygame.quit()