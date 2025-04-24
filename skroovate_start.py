import pygame
import random
import time

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
TRACK_COLOR = (50, 50, 50)
POINT_COLOR = (0, 255, 0)
OBSTACLE_COLOR = (255, 0, 0)
BOOSTER_COLOR = (0, 200, 255)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
CYAN = (0, 255,255)

# Screen setup
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("SKROOVATE Demo Game Projection")
clock = pygame.time.Clock()
font = pygame.font.Font(None, 36)

# Player settings
player_size = 20
player_pos = [WIDTH//4, HEIGHT//2]
player_speed = 5
score = 0
out_of_bounds = False
booster_collect = False

# Track
track_rect = pygame.Rect(100, 50, WIDTH-200, HEIGHT-100)

# Interactive elements in display
point_zones = [(random.randint(150, WIDTH-150), random.randint(100, HEIGHT-100)) for _ in range(5)]
obstacles = [(random.randint(150, WIDTH-150), random.randint(100, HEIGHT-100)) for _ in range(4)]
boosters = [(random.randint(150, WIDTH-150), random.randint(100, HEIGHT-100)) for _ in range(2)]

# Timers for updating obstacle, game duration, and 
last_obstacle_update = time.time()
game_start_time = time.time()
game_duration = 300  # 5 minutes
booster_message_time = 0  # For splash text timing

def draw_track():
    screen.fill(WHITE)
    pygame.draw.rect(screen, TRACK_COLOR, track_rect, 5)
    
    for point in point_zones:
        pygame.draw.circle(screen, POINT_COLOR, point, 15)
    
    for obs in obstacles:
        pygame.draw.circle(screen, OBSTACLE_COLOR, obs, 15)
    
    for booster in boosters:
        pygame.draw.circle(screen, BOOSTER_COLOR, booster, 15)

def move_player(keys):
    global player_pos, score, out_of_bounds, point_zones, booster_message_time, boosters

    prev_pos = player_pos[:]
    if keys[pygame.K_LEFT]:
        player_pos[0] -= player_speed
    if keys[pygame.K_RIGHT]:
        player_pos[0] += player_speed
    if keys[pygame.K_UP]:
        player_pos[1] -= player_speed
    if keys[pygame.K_DOWN]:
        player_pos[1] += player_speed

    # Check if player is out of bounds
    if not track_rect.collidepoint(player_pos[0], player_pos[1]):
        out_of_bounds = True
        player_pos = prev_pos
    else:
        out_of_bounds = False

    # Collision with obstacles
    for obs in obstacles:
        if pygame.Rect(player_pos[0], player_pos[1], player_size, player_size).collidepoint(obs):
            out_of_bounds = True
            player_pos = prev_pos
            break

    # Collect points
    for i, point in enumerate(point_zones):
        if pygame.Rect(player_pos[0], player_pos[1], player_size, player_size).collidepoint(point):
            score += 10
            point_zones[i] = (random.randint(150, WIDTH-150), random.randint(100, HEIGHT-100))

    # Collecting Point Booster 
    for i, booster in enumerate(boosters):
        if pygame.Rect(player_pos[0], player_pos[1], player_size, player_size).collidepoint(booster):
            score += 30
            booster_message_time = time.time()
            boosters[i] = (random.randint(150, WIDTH-150), random.randint(100, HEIGHT-100))

running = True
while running:
    clock.tick(30)
    screen.fill(WHITE)
    draw_track()
    
    keys = pygame.key.get_pressed()
    move_player(keys)

    # Draw player
    if out_of_bounds:
        player_color = RED
    elif booster_collect:
        player_color = CYAN
    else:
        player_color = BLUE
    pygame.draw.rect(screen, player_color, (*player_pos, player_size, player_size))

    # Display warning
    if out_of_bounds:
        warning_text = font.render("Warning: You're losing points!", True, RED)
        screen.blit(warning_text, (WIDTH//4, HEIGHT//2))
        score = max(0, score - 1)

    # Display booster splash
    if time.time() - booster_message_time < 1:
        boost_text = font.render("30-point boost!", True, BOOSTER_COLOR)
        screen.blit(boost_text, (WIDTH // 2 - 100, HEIGHT // 2 - 50))

    # Display score
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (10, 10))

    # Display timer
    elapsed_time = int(time.time() - game_start_time)
    remaining_time = max(0, game_duration - elapsed_time)
    timer_text = font.render(f"Time Left: {remaining_time}s", True, (0, 0, 0))
    screen.blit(timer_text, (WIDTH - 200, 10))

    # Update obstacles' positions every 5 seconds
    if time.time() - last_obstacle_update > 5:
        obstacles = [(random.randint(150, WIDTH-150), random.randint(100, HEIGHT-100)) for _ in range(3)]
        last_obstacle_update = time.time()

    # End game after duration
    if elapsed_time >= game_duration:
        screen.fill(WHITE)
        game_over_text = font.render("Game Over", True, RED)
        final_score_text = font.render(f"Final Score: {score}", True, (0, 0, 0))
        screen.blit(game_over_text, (WIDTH//3, HEIGHT//3))
        screen.blit(final_score_text, (WIDTH//3, HEIGHT//2))
        pygame.display.flip()
        pygame.time.delay(3000)
        running = False

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()

pygame.quit()
