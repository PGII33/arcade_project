from random import randint
import pygame

class Player:
    ''' Player '''
    def __init__(self, pos:list, dim:list) -> None:
        self.pos = pos
        self.dim = dim
        self.rect = pygame.Rect(pos[0], pos[1], dim[0], dim[1])

    def draw(self, screen:pygame.Surface) -> None:
        """ Draw the player """
        self.pos = [round(self.pos[0]), round(self.pos[1])]
        self.rect = pygame.Rect(self.pos[0], self.pos[1], self.dim[0], self.dim[1])
        pygame.draw.rect(screen, (0,0,0), self.rect)

class Ball:
    ''' A ball '''
    def __init__(self, pos:list, dim:int) -> None:
        self.pos = pos
        self.dim = dim

    def draw(self, screen:pygame.Surface) -> None:
        """ Draw the ball """
        self.pos = [round(self.pos[0]), round(self.pos[1])]
        pygame.draw.circle(screen, (0,0,0), self.pos, self.dim)

def pong(screen:pygame.Surface, running:bool, coef:tuple)-> None:
    ''' A pong Game '''
    
    PLAYER_WIDTH = 20*coef[0]
    PLAYER_HEIGHT = 100*coef[1]
    FPS = 60
    BORDER_UP = 0
    BORDER_DOWN = 1080*coef[1] * 2/3

    move_y = 5*coef[1]
    player1 = Player([0, 1080*coef[1]//2 - 50*coef[1]//2], [PLAYER_WIDTH, PLAYER_HEIGHT])
    player2 = Player([(1920- PLAYER_WIDTH - 4)*coef[0]*2/3, 1080*coef[1]//2 - 50*coef[1]//2], [PLAYER_WIDTH, PLAYER_HEIGHT])
    ball = Ball([1920*coef[0]*2/3//2, 1080*coef[1]*2/3//2], 10*coef[0])
    velocity = [randint(-2, 2)*coef[0], randint(-2, 2)*coef[1]]
    if velocity[0] < 0.5 or velocity[0] > -0.5:
        velocity[0] *= 3
    time_speed_velocity = 2
    elapsed_time = 0
    up1, down1 = False, False
    up2, down2 = False, False

    while running:
        
        # Gestion du temps
        clock = pygame.time.Clock()
        dt = clock.tick(FPS)
        elapsed_time += dt

        # AFfichage
        screen.fill((123,123,123))
        player1.draw(screen)
        player2.draw(screen)
        ball.draw(screen)

        # Gestion des inputs
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_e:
                    running = False
                if event.key == pygame.K_UP:
                    up2 = True
                if event.key == pygame.K_DOWN:
                    down2 = True
                if event.key == pygame.K_z:
                    up1 = True
                if event.key == pygame.K_s:
                    down1 = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_UP:
                    up2 = False
                if event.key == pygame.K_DOWN:
                    down2 = False
                if event.key == pygame.K_z:
                    up1 = False
                if event.key == pygame.K_s:
                    down1 = False

        # Gestion de la balle
        ball.pos[0] += velocity[0] * time_speed_velocity
        ball.pos[1] += velocity[1] * time_speed_velocity
        
        # Gestion des collisions balle joueurs et de la vitesse de la balle 
        if player1.rect.colliderect(ball.pos[0], ball.pos[1], ball.dim, ball.dim) or player2.rect.colliderect(ball.pos[0], ball.pos[1], ball.dim, ball.dim):
            velocity[0] = -velocity[0]
            velocity[1] += randint(-2, 2)*coef[1]
            velocity[1] = -velocity[1]
            time_speed_velocity += 0.01
        if ball.pos[1] < BORDER_UP or ball.pos[1] > BORDER_DOWN:
            velocity[1] = -velocity[1]
            ball.pos[1] += velocity[1] * time_speed_velocity
        if ball.pos[0] < 0 or ball.pos[0] > 1920*coef[0]*2/3:
            running = False

        print(ball.pos)

        # Gestion des mouvements des joueurs
        if up1 and player1.pos[1] > BORDER_UP - move_y:
            player1.pos[1] -= move_y * time_speed_velocity
        if down1 and player1.pos[1] + PLAYER_HEIGHT < BORDER_DOWN + move_y:
            player1.pos[1] += move_y * time_speed_velocity
        if up2 and player2.pos[1] > BORDER_UP - move_y:
            player2.pos[1] -= move_y * time_speed_velocity
        if down2 and player2.pos[1] + PLAYER_HEIGHT < BORDER_DOWN + move_y:
            player2.pos[1] += move_y * time_speed_velocity
 
        pygame.display.update()