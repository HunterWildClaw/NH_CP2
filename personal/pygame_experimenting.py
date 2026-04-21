import pygame
import random

# --- 1. Setup & Constants ---
pygame.init()

SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
FPS = 60
GRAVITY = 1
JUMP_HEIGHT = -20
PLAYER_SPEED = 5
AUTO_SCROLL_SPEED = 4

# Colors
SKY_BLUE = (135, 206, 235)
PLAYER_COLOR = (0, 0, 255)
PLATFORM_COLOR = (34, 139, 34)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Auto-Scrolling Platformer")
clock = pygame.time.Clock()

# --- 2. Classes ---
class Player:
    def __init__(self):
        self.rect = pygame.Rect(100, 300, 40, 40)
        self.vel_y = 0
        self.on_ground = False

    def move(self, platforms):
        dx = 0
        dy = 0
        
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            dx -= PLAYER_SPEED
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            dx += PLAYER_SPEED
        
        if (keys[pygame.K_SPACE] or keys[pygame.K_UP] or keys[pygame.K_w]) and self.on_ground:
            self.vel_y = JUMP_HEIGHT
            self.on_ground = False

        self.vel_y += GRAVITY
        dy += self.vel_y

        # Collision Handling
        self.on_ground = False
        
        # X Collision
        self.rect.x += dx
        for plat in platforms:
            if self.rect.colliderect(plat):
                if dx > 0: self.rect.right = plat.left
                if dx < 0: self.rect.left = plat.right

        # Y Collision
        self.rect.y += dy
        for plat in platforms:
            if self.rect.colliderect(plat):
                if self.vel_y > 0:
                    self.rect.bottom = plat.top
                    self.vel_y = 0
                    self.on_ground = True
                elif self.vel_y < 0:
                    self.rect.top = plat.bottom
                    self.vel_y = 0

        if keys[pygame.K_r]:
            # Reset player state
            self.rect = pygame.Rect(100, 300, 40, 40)
            self.vel_y = 0
            self.on_ground = False

            # Reset platforms to starting state and return the new list
            platforms = [pygame.Rect(0, 550, 800, 50)]
            platforms += spawn_platforms(400, 10)

            # stop further movement processing this frame
            return platforms

        return platforms
            
    def draw(self):
        pygame.draw.rect(screen, PLAYER_COLOR, self.rect)

# --- 3. Functions ---
def spawn_platforms(start_x, count):
    new_plats = []
    current_x = start_x
    for _ in range(count):
        width = random.randint(100, 250)
        current_x += random.randint(150, 300)
        y = random.randint(200, 500)
        new_plats.append(pygame.Rect(current_x, y, width, 20))
    return new_plats

# --- 4. Main Game Loop ---
player = Player()
platforms = [pygame.Rect(0, 550, 800, 50)] 
platforms += spawn_platforms(400, 10)

running = True
while running:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 1. Constant Auto-Scroll: Move all platforms left
    for plat in platforms:
        plat.x -= AUTO_SCROLL_SPEED
    # 2. Update Player
    platforms = player.move(platforms)
    
    # 3. Infinite Generation Logic
    # 3. Infinite Generation Logic
    if platforms[-1].x < SCREEN_WIDTH + 500:
        platforms += spawn_platforms(platforms[-1].x, 5)

    # 4. Clean up old platforms
    platforms = [p for p in platforms if p.right > -100]

    # Draw everything
    screen.fill(SKY_BLUE)
    for plat in platforms:
        pygame.draw.rect(screen, PLATFORM_COLOR, plat)
    player.draw()

    pygame.display.update()

pygame.quit()