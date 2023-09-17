# directions:
# 1. add `from handwriting/main import generate_image`
# 2. generate_image takes in text and returns a PIL image object
from PIL import Image
from sys import argv
import io
import random
<<<<<<< HEAD
import os
=======
>>>>>>> 9125d73 (tys first commit)

def process_text_to_image(text):
    """
    Takes in a text string and returns a PIL object

    Args:
        text (str): a string (preferably numbers)

    Returns:
        PIL.image: PIL image library
    """
    BG=Image.open("myfont/bg.png") #path of page(background)photo (I have used blank page)
    
<<<<<<< HEAD
=======
    gap, ht = 0, 0
>>>>>>> 9125d73 (tys first commit)
    
    width = 0
    height = 0

<<<<<<< HEAD
    written_chars = []

    for char in text:
        try:
            char_code = ord(char)
            cases_list = os.listdir("myfont/{}".format(char_code))
            random_file = random.choice(cases_list)
            cases = Image.open(f"myfont/{char_code}/{random_file}")
            written_chars.append(cases)
=======
    for char in text:
        try:
            char_code = ord(char)
            cases = Image.open("myfont/{}.png".format(char_code))
>>>>>>> 9125d73 (tys first commit)
            width += cases.width
            if cases.height > height:
                height = cases.height
        except:
<<<<<<< HEAD
            cases_list = os.listdir("myfont/{}".format(char_code))
            random_file = random.choice(cases_list)
            print(f"missing folder: myfont/{char_code}")

    BG = BG.resize((width, height))
    # sheet_width=BG.width

    # for each letter in the uploaded txt file, read the unicode value and replace it with
    # the corresponding handwritten file in the "myfont" folder.
    gap = 0

    for written_char in written_chars:
        BG.paste(written_char, (gap, 0))
        gap+=written_char.width

        # if sheet_width < gap or len(char)*115 >(sheet_width-gap):
        #     gap,ht=0,ht
            
=======
            pass

    BG = BG.resize((width, height))
    sheet_width=BG.width

    # for each letter in the uploaded txt file, read the unicode value and replace it with
    # the corresponding handwritten file in the "myfont" folder.
    for char in text:
        try:
            char_code = ord(char)
            cases = Image.open("myfont/{}.png".format(char_code))
            BG.paste(cases, (gap, ht))
            size = cases.width
            height=cases.height
            gap+=size

            if sheet_width < gap or len(char)*115 >(sheet_width-gap):
                gap,ht=0,ht+140
        except FileNotFoundError:
            char_code = ord(char)
            print("Missing file: myfont/{}.png".format(char_code))
>>>>>>> 9125d73 (tys first commit)

    return BG

def generate_image(text: str):
    """
    Returns handwriting as a png

    Args:
        text (str): solution (ideally a number)

    Returns:
        png file: A png image file
    """
    generated_image = process_text_to_image(text)

    # Convert the generated image to bytes
    img_byte_array = io.BytesIO()
    generated_image.save(img_byte_array, format="PNG")
    img_byte_array.seek(0)
    
    return generated_image

if __name__ == "__main__":
    image = generate_image("5+10")
    image.save("test.png")