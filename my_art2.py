import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FONT_SIZE = 120
print("Who are you")
NAME = input("Enter your name: ")  # Ask for name

# Colors
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Name Art Animation")
font = pygame.font.Font(None, FONT_SIZE)

# Function to create sparkles
def create_sparkle():
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    sparkle_color = (255, 255, random.randint(200, 255))
    lifetime = random.randint(20, 40)  # Frames before disappearing
    return [x, y, sparkle_color, lifetime]

def main():
    clock = pygame.time.Clock()
    displayed_name = ""
    index = 0
    sparkles = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Add next letter over time
        if index < len(NAME):
            displayed_name += NAME[index]
            index += 1

        # Render the full displayed name
        color = pygame.Color(0)
        color.hsva = (random.randint(0, 360), 100, 100)
        text_surface = font.render(displayed_name, True, color)
        screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2))

        # Create sparkles
        if random.random() < 0.2:
            sparkles.append(create_sparkle())

        # Draw and update sparkles
        for sparkle in sparkles[:]:
            x, y, sparkle_color, lifetime = sparkle
            pygame.draw.circle(screen, sparkle_color, (x, y), 5)
            sparkle[3] -= 1
            if sparkle[3] <= 0:
                sparkles.remove(sparkle)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
