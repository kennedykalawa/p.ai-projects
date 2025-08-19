import time
import sys
from colorama import init, Fore, Style
import random

# Initialize colorama for colored output
init(autoreset=True)

# Some color choices for letters
colors = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.BLUE, Fore.MAGENTA, Fore.CYAN, Fore.WHITE]

# Sparkle effect symbols
sparkles = ['✨', '🌟', '💫', '*', '+', '🌟']

# Get the name from user
name = input("Enter your name: ")

# Print animation
for letter in name:
    color = random.choice(colors)
    sparkle = random.choice(sparkles)
    sys.stdout.write(color + letter + " " + sparkle + " ")
    sys.stdout.flush()
    time.sleep(0.3)  # delay for animation effect

print(Style.BRIGHT + Fore.WHITE + "\n👍Done! Your name is shining! ⚡🌠")
