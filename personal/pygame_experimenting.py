# NH pygame experiment
import pygame

# 1. Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
GRAVITY = 0.8
JUMP_HEIGHT = -16
PLAYER_SPEED = 5

# Colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
SKY_BLUE = (135, 206, 235)

# Setup Window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Basic Pygame Platformer")
clock = pygame.time.Clock()

# Player Class
class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 500, 40, 40)
        self.vel_y = 0
        self.on_ground = False

    def update(self, platforms):
        # Movement
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]:
            self.rect.x += PLAYER_SPEED
        
        # Jump logic
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = JUMP_HEIGHT
            self.on_ground = False

        # Apply Gravity
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y

        # Collision with Platforms
        self.on_ground = False
        for plat in platforms:
            if self.rect.colliderect(plat):
                if self.vel_y > 0: # Falling down
                    self.rect.bottom = plat.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0: # Hitting ceiling
                    self.rect.top = plat.bottom
                    self.vel_y = 0

    def draw(self):
        pygame.draw.rect(screen, BLUE, self.rect)

# 2. Main Game Loop
player = Player()
# Create floor and some floating platforms
platforms = [
    pygame.Rect(0, 550, 800, 50), # Floor
    pygame.Rect(200, 400, 150, 20),
    pygame.Rect(450, 300, 150, 20),
    pygame.Rect(100, 200, 100, 20)
]

running = True
while running:
    # Event Handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Update Logic
    player.update(platforms)

    # Rendering
    screen.fill(SKY_BLUE)
    for plat in platforms:
        pygame.draw.rect(screen, GREEN, plat)
    player.draw()

    pygame.display.update()
    clock.tick(FPS)

pygame.quit()
