#Importing Library
from fastapi import FastAPI
from PIL import Image
from sys import argv
import io
import random

def process_text_to_image(text):
    BG=Image.open("myfont/bg.png") #path of page(background)photo (I have used blank page)
    
    gap, ht = 0, 0
    
    width = 0
    height = 0

    for char in text:
        try:
            char_code = ord(char)
            cases = Image.open("myfont/{}.png".format(char_code))
            width += cases.width
            if cases.height > height:
                height = cases.height
        except:
            pass

    BG = BG.resize((width, height - 100))
    sheet_width=BG.width

    # for each letter in the uploaded txt file, read the unicode value and replace it with
    # the corresponding handwritten file in the "myfont" folder.
    for char in text:
        try:
            char_code = ord(char)
            cases = Image.open("myfont/{}.png".format(char_code))
            BG.paste(cases, (gap + random.randrange(-20, 20), ht + random.randrange(-30, 30)))
            size = cases.width
            height=cases.height
            #print(size)
            print("Running...........")
            gap+=size

            if sheet_width < gap or len(char)*115 >(sheet_width-gap):
                gap,ht=0,ht+140
        except FileNotFoundError:
            char_code = ord(char)
            print("Missing file: myfont/{}.png".format(char_code))

    return BG

def generate_image(text: str):
    generated_image = process_text_to_image(text)

    # Convert the generated image to bytes
    img_byte_array = io.BytesIO()
    generated_image.save(img_byte_array, format="PNG")
    img_byte_array.seek(0)
    
    return generated_image

image = generate_image("5+10=15")

image.save("test.png")