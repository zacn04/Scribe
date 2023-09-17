from tkinter import *
import tkinter as tk
from latex_to_response import image_handling
from PIL import ImageTk, Image
from latex_to_response import gpt


def main(query, answer):
    window=Tk()

    helpWindow = tk.Toplevel()
    helpWindow.title("Help Window")
    helpWindow.geometry(f"500x400+10+20")

    frame = Frame(window, width=500, height=400)
    frame.pack()
    frame.place(anchor='center', relx=0.5, rely=0.5)

    # also saves image to a file
    # returns 1 if image found, 0 otherwise
    image_found = image_handling.save_image(query, "help_image.png")

    if image_found:
        img = ImageTk.PhotoImage(Image.open("help_image.png"))
        label = Label(frame, image = img)
        label.pack()
    
    explanation = gpt(query, answer)

    label = tk.Label(text=explanation)
    label.pack()

    window.title('Hello Python')
    window.geometry(f"500x400+10+20")
    window.mainloop()

if __name__ == "__main__":
    main("5 * 3", "15")