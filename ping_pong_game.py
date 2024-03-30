import pygame
import random

# Initialize Pygame
pygame.init()

# Set up the screen
WIDTH, HEIGHT = 800, 600
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ping Pong")

# Set up the clock
clock = pygame.time.Clock()

# Define constants
BALL_RADIUS = 10
PADDLE_WIDTH = 10
PADDLE_HEIGHT = 100
BALL_SPEED = 5
PADDLE_SPEED = 5

# Set up initial positions
ball_x = WIDTH // 2
ball_y = HEIGHT // 2
ball_dx = BALL_SPEED * random.choice([1, -1])
ball_dy = BALL_SPEED * random.choice([1, -1])

paddle1_y = (HEIGHT - PADDLE_HEIGHT) // 2
paddle2_y = (HEIGHT - PADDLE_HEIGHT) // 2
paddle1_dy = 0
paddle2_dy = 0

# Function to draw the ball
def draw_ball(x, y):
    pygame.draw.circle(screen, WHITE, (x, y), BALL_RADIUS)

# Function to draw the paddles
def draw_paddles():
    pygame.draw.rect(screen, WHITE, (0, paddle1_y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, (WIDTH - PADDLE_WIDTH, paddle2_y, PADDLE_WIDTH, PADDLE_HEIGHT))

# Function to update ball position
def move_ball():
    global ball_x, ball_y, ball_dx, ball_dy

    # Update ball position
    ball_x += ball_dx
    ball_y += ball_dy

    # Check for collisions with walls
    if ball_y - BALL_RADIUS <= 0 or ball_y + BALL_RADIUS >= HEIGHT:
        ball_dy *= -1

    # Check for collisions with paddles
    if ball_x - BALL_RADIUS <= PADDLE_WIDTH and paddle1_y <= ball_y <= paddle1_y + PADDLE_HEIGHT:
        ball_dx *= -1
    elif ball_x + BALL_RADIUS >= WIDTH - PADDLE_WIDTH and paddle2_y <= ball_y <= paddle2_y + PADDLE_HEIGHT:
        ball_dx *= -1

    # Check for scoring
    if ball_x - BALL_RADIUS <= 0 or ball_x + BALL_RADIUS >= WIDTH:
        ball_x = WIDTH // 2
        ball_y = HEIGHT // 2
        ball_dx = BALL_SPEED * random.choice([1, -1])
        ball_dy = BALL_SPEED * random.choice([1, -1])

# Function to update paddle position
def move_paddles():
    global paddle1_y, paddle2_y

    # Update paddle positions
    paddle1_y += paddle1_dy
    paddle2_y += paddle2_dy

    # Keep paddles within screen bounds
    if paddle1_y < 0:
        paddle1_y = 0
    elif paddle1_y + PADDLE_HEIGHT > HEIGHT:
        paddle1_y = HEIGHT - PADDLE_HEIGHT

    if paddle2_y < 0:
        paddle2_y = 0
    elif paddle2_y + PADDLE_HEIGHT > HEIGHT:
        paddle2_y = HEIGHT - PADDLE_HEIGHT

# Main game loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                paddle1_dy = -PADDLE_SPEED
            elif event.key == pygame.K_s:
                paddle1_dy = PADDLE_SPEED
            elif event.key == pygame.K_UP:
                paddle2_dy = -PADDLE_SPEED
            elif event.key == pygame.K_DOWN:
                paddle2_dy = PADDLE_SPEED
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                paddle1_dy = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                paddle2_dy = 0

    # Clear the screen
    screen.fill(BLACK)

    # Move ball and paddles
    move_ball()
    move_paddles()

    # Draw the ball and paddles
    draw_ball(ball_x, ball_y)
    draw_paddles()

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
