from PIL import Image, ImageDraw, ImageFont
import numpy as np

# Emoji set for mapping
emojis = ["😀", "😂", "😎", "😍", "😜", "😡", "😴", "🤯", "🥶", "🤩", "😇", "😭", "🤑", "🤮", "🥳"]

# Load image
image_path = "/home/ghost-engineer/Pictures/wt4.jpg"  # Replace with your image
img = Image.open("/home/ghost-engineer/Pictures/wt4.jpg").convert("RGB")

# Resize for fewer emojis (smaller = faster)
emoji_size = 20
img = img.resize((50, 50))  # Smaller width/height for faster rendering

# Create new blank image for emoji art
output_img = Image.new("RGB", (img.width * emoji_size, img.height * emoji_size), (255, 255, 255))
draw = ImageDraw.Draw(output_img)

# Load a font that supports emojis (Apple Color Emoji or Noto Color Emoji)
try:
    font = ImageFont.truetype("NotoColorEmoji.ttf", emoji_size)  
except:
    font = ImageFont.load_default()  # Fallback

# Convert image to numpy for easy pixel reading
pixels = np.array(img)

# Function to pick an emoji based on brightness
def brightness_to_emoji(r, g, b):
    brightness = (r + g + b) / 3
    index = int((brightness / 255) * (len(emojis) - 1))
    return emojis[index]

# Draw emojis
for y in range(img.height):
    for x in range(img.width):
        r, g, b = pixels[y, x]
        emoji = brightness_to_emoji(r, g, b)
        draw.text((x * emoji_size, y * emoji_size), emoji, font=font, fill=(0, 0, 0))

# Save result
output_img.save("emoji_mosaic.png")
print("✅ Emoji mosaic saved as emoji_mosaic.png")
