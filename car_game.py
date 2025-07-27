import pygame
import random

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 400, 600
window = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Simple Car Race")

# Colors
WHITE = (255, 255, 255)
GRAY = (100, 100, 100)
RED = (255, 0, 0)
BLUE = (0, 0, 255)

# Car settings
CAR_WIDTH, CAR_HEIGHT = 50, 100
car_x = WIDTH // 2 - CAR_WIDTH // 2
car_y = HEIGHT - CAR_HEIGHT - 10
car_speed = 5

# Obstacle settings
obs_width, obs_height = 50, 100
obs_x = random.randint(0, WIDTH - obs_width)
obs_y = -obs_height
obs_speed = 7

# Clock and font
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 36)

# Game variables
running = True
score = 0

# Main game loop
while running:
    clock.tick(60)  # 60 FPS

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move car with keys
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and car_x > 0:
        car_x -= car_speed
    if keys[pygame.K_RIGHT] and car_x < WIDTH - CAR_WIDTH:
        car_x += car_speed

    # Move obstacle
    obs_y += obs_speed
    if obs_y > HEIGHT:
        obs_y = -obs_height
        obs_x = random.randint(0, WIDTH - obs_width)
        score += 1

    # Collision detection
    car_rect = pygame.Rect(car_x, car_y, CAR_WIDTH, CAR_HEIGHT)
    obs_rect = pygame.Rect(obs_x, obs_y, obs_width, obs_height)
    if car_rect.colliderect(obs_rect):
        running = False

    # Drawing
    window.fill(GRAY)
    pygame.draw.rect(window, BLUE, car_rect)
    pygame.draw.rect(window, RED, obs_rect)

    # Display score
    score_text = font.render(f"Score: {score}", True, WHITE)
    window.blit(score_text, (10, 10))

    # Update display
    pygame.display.flip()

pygame.quit()
print("Game Over! Final Score:", score)
