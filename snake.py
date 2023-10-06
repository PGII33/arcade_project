""" A snake game """
import pygame
import random

class Snake:
    """ The snake """
    def __init__(self, pos:list, dim:list, color:tuple) -> None:
        self.pos = pos
        self.dim = dim
        self.color = color
        self.rect = pygame.Rect(pos[0], pos[1], dim[0], dim[1])

    def draw(self, screen:pygame.Surface) -> None:
        """ Draw the snake """
        self.pos = [round(self.pos[0]), round(self.pos[1])]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.dim[0], self.dim[1])
        pygame.draw.rect(screen, self.color, self.rect)

class Food:
    """ The food """
    def __init__(self, pos:list, dim:list, color:tuple) -> None:
        self.pos = pos
        self.dim = dim
        self.color = color
        self.rect = pygame.Rect(pos[0], pos[1], dim[0], dim[1])

    def draw(self, screen:pygame.Surface) -> None:
        """ Draw the food """
        self.pos = [round(self.pos[0]), round(self.pos[1])]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.dim[0], self.dim[1])
        pygame.draw.rect(screen, self.color, self.rect)

def snake(screen:pygame.Surface, running:bool, coef:tuple)-> None:
    ''' A snake game '''
    # Variables
    BORDER_LEFT = 0
    BORDER_RIGHT = int(1000*coef[0] * 2/3)
    BORDER_UP = 0
    BORDER_DOWN = int(1000*coef[1] * 2/3)
    SNAKE_WIDTH = 50*coef[0]
    SNAKE_HEIGHT = 50*coef[1]
    FOOD_WIDTH = int(50*coef[0])
    FOOD_HEIGHT = int(50*coef[1])
    FPS = 60

    mov_speed_x = 50*coef[0]
    mov_speed_y = 50*coef[1]
    elapsed_time = 0
    score = 0
    snake = [Snake([1900*coef[0]* 2/6 - SNAKE_WIDTH /2, 1000*coef[1]*2/3  - SNAKE_HEIGHT], [SNAKE_WIDTH, SNAKE_HEIGHT], (0,0,0))]
    food = Food([random.randint(BORDER_LEFT//50, (BORDER_RIGHT - FOOD_WIDTH)//50)*50, random.randint(BORDER_UP//50, (BORDER_DOWN - FOOD_HEIGHT)//50)*50], [FOOD_WIDTH, FOOD_HEIGHT], (255,0,0))

    mov_left = False
    mov_right = False
    mov_up = False
    mov_down = False

    while running:

        # Gestion du temps
        clock = pygame.time.Clock()
        dt = clock.tick(FPS)
        elapsed_time += dt

        # Affichage
        screen.fill((123,123,123))
        food.draw(screen)
        for i in snake:
            i.draw(screen)

        # Gestion des évènements
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            # Gestion des touches
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and not mov_right:
                    mov_left = True
                    mov_right = False
                    mov_up = False
                    mov_down = False
                if event.key == pygame.K_RIGHT and not mov_left:
                    mov_left = False
                    mov_right = True
                    mov_up = False
                    mov_down = False
                if event.key == pygame.K_UP and not mov_down:
                    mov_left = False
                    mov_right = False
                    mov_up = True
                    mov_down = False
                if event.key == pygame.K_DOWN and not mov_up:
                    mov_left = False
                    mov_right = False
                    mov_up = False
                    mov_down = True
                if event.key == pygame.K_e:
                    running = False

        #Gestion des collisions avec le corps
        for i in range(1, len(snake)):
            if snake[0].rect.colliderect(snake[i].rect):
                running = False

        # Gestion du mouvement
        if elapsed_time >= 2000/FPS:
            elapsed_time = 0
            for i in range(len(snake)-1, 0, -1):
                snake[i].pos = snake[i-1].pos
            if mov_left:
                snake[0].pos[0] -= mov_speed_x
            if mov_right:
                snake[0].pos[0] += mov_speed_x
            if mov_up:
                snake[0].pos[1] -= mov_speed_y
            if mov_down:
                snake[0].pos[1] += mov_speed_y

        # Gestion de la nourriture
        if snake[0].rect.colliderect(food.rect):
            score += 1
            snake.append(Snake([snake[-1].pos[0], snake[-1].pos[1]], [SNAKE_WIDTH, SNAKE_HEIGHT], (0,0,0)))
            food = Food([random.randint(BORDER_LEFT//50, (BORDER_RIGHT - FOOD_WIDTH)//50)*50, random.randint(BORDER_UP//50, (BORDER_DOWN - FOOD_HEIGHT)//50)*50], [FOOD_WIDTH, FOOD_HEIGHT], (255,0,0))

        # Gestion des collisions avec les bords
        if snake[0].pos[0] < BORDER_LEFT:
            snake[0].pos[0] = BORDER_LEFT
        if snake[0].pos[0] > BORDER_RIGHT - SNAKE_WIDTH:
            snake[0].pos[0] = BORDER_RIGHT - SNAKE_WIDTH
        if snake[0].pos[1] < BORDER_UP:
            snake[0].pos[1] = BORDER_UP
        if snake[0].pos[1] > BORDER_DOWN - SNAKE_HEIGHT:
            snake[0].pos[1] = BORDER_DOWN - SNAKE_HEIGHT
        
        pygame.display.update()
