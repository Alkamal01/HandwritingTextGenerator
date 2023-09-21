from PIL import Image, ImageDraw, ImageFont

text = input("Enter the text you want to convert to handwriting: ")

font = ImageFont.truetype("handwriting.ttf", size=36)

text_width, text_height = font.getsize(text)

image = Image.new("RGB", (text_width, text_height), "white")

draw = ImageDraw.Draw(image)

draw.text((0, 0), text, fill="black", font=font)

image.save("handwriting.png")

image.show()
