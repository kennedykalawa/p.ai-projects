import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 800, 600
FPS = 60
FONT_SIZE = 100
NAME = "Kenny"  # Change this to your name

# Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Name Art Animation")
font = pygame.font.Font(None, FONT_SIZE)

# Function to create sparkles
def create_sparkle():
    x = random.randint(0, WIDTH)
    y = random.randint(0, HEIGHT)
    sparkle_color = (255, 255, random.randint(200, 255))
    return (x, y, sparkle_color)

# Main loop
def main():
    clock = pygame.time.Clock()
    letters = []
    for letter in NAME:
        letters.append((letter, random.randint(0, 360)))  # Store letter and color hue

    index = 0
    sparkles = []

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        screen.fill(BLACK)

        # Draw letters
        if index < len(letters):
            letter, hue = letters[index]
            color = pygame.Color(0)
            color.hsva = (hue, 100, 100)  # Set HSL color
            text_surface = font.render(letter, True, color)
            screen.blit(text_surface, (WIDTH // 2 - text_surface.get_width() // 2, HEIGHT // 2))
            index += 1

        # Create sparkles
        if random.random() < 0.1:  # 10% chance to create a sparkle each frame
            sparkles.append(create_sparkle())

        # Draw sparkles
        for sparkle in sparkles:
            x, y, sparkle_color = sparkle
            pygame.draw.circle(screen, sparkle_color, (x, y), 5)

        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()