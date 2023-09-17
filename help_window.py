from tkinter import *
import tkinter as tk
from latex_to_response import image_handling
from PIL import ImageTk, Image
from latex_to_response import gpt


def main(query, answer):
    window=Tk()

    frame = Frame(window, width=500, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # also saves image to a file
    # returns 1 if image found, 0 otherwise
    print("finding image")
    image_found = image_handling.save_image(query, "help_image.png")
    print("found image")

    if image_found:
        img = ImageTk.PhotoImage(Image.open("help_image.png"))
        label = Label(frame, image = img)
        label.pack()
    
    print("running query")
    explanation = gpt.explanation(query, answer)
    print("finished query")

    label = tk.Label(text=explanation, wraplength=500)
    label.pack()

    window.title('Hello Python')
    window.geometry(f"500x400+10+20")
    window.mainloop()

if __name__ == "__main__":
    main("3 + 3", "6")