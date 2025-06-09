import pygame
import sys

pygame.init()

window_width = 800
window_height = 600
screen = pygame.display.set_mode((window_width, window_height))
pygame.display.set_caption("Пинг-понг")

FPS = 60
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

paddle_width = 10
paddle_height = 100
paddle_speed = 5

ball_size = 15
ball_speed_x = 5
ball_speed_y = 5

score_font = pygame.font.Font(None, 50)

class Paddle:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, paddle_width, paddle_height)
        self.color = WHITE
        self.speed = paddle_speed

    def update_arrows(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_DOWN] and self.rect.y < window_height - self.rect.height:
            self.rect.y += self.speed

    def update_ws(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[pygame.K_s] and self.rect.y < window_height - self.rect.height:
            self.rect.y += self.speed

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


class Ball:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, ball_size, ball_size)
        self.color = WHITE
        self.speed_x = ball_speed_x
        self.speed_y = ball_speed_y

    def update(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.top <= 0 or self.rect.bottom >= window_height:
            self.speed_y *= -1

    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)


def reset_ball():
    ball.rect.x = window_width // 2 - ball_size // 2
    ball.rect.y = window_height // 2 - ball_size // 2
    ball.speed_x = ball_speed_x * (-1 if random.random() < 0.5 else 1)
    ball.speed_y = ball_speed_y * (-1 if random.random() < 0.5 else 1)


import random
paddle1 = Paddle(50, window_height // 2 - 50)
paddle2 = Paddle(window_width - 60, window_height // 2 - 50)
ball = Ball(window_width // 2 - ball_size // 2, window_height // 2 - ball_size // 2)

player1_score = 0
player2_score = 0
max_score = 3

game_over = False
winner = None

reset_ball()  


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not game_over:
        paddle1.update_ws()
        paddle2.update_arrows()
        ball.update()

        if ball.rect.colliderect(paddle1.rect) or ball.rect.colliderect(paddle2.rect):
            ball.speed_x *= -1

        if ball.rect.left <= 0: 
            player2_score += 1
            reset_ball()
        if ball.rect.right >= window_width:  
            player1_score += 1
            reset_ball()

        if player1_score >= max_score:
            game_over = True
            winner = "Игрок 1"
        if player2_score >= max_score:
            game_over = True
            winner = "Игрок 2"

        screen.fill(BLACK)
        paddle1.draw()
        paddle2.draw()
        ball.draw()

        score_text = score_font.render(f"{player1_score} - {player2_score}", True, WHITE)
        screen.blit(score_text, (window_width // 2 - score_text.get_width() // 2, 20))

    else: 
        win_text = score_font.render(f"Победил: {winner}!", True, WHITE)
        screen.blit(win_text, (window_width // 2 - win_text.get_width() // 2, window_height // 2 - win_text.get_height() // 2))

    pygame.display.flip()

    clock.tick(FPS)

pygame.quit()
sys.exit()
