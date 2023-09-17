import tkinter as tk
from tkinter import ttk
from PIL import ImageGrab, Image, ImageTk  # Import the ImageGrab module from Pillow
import customtkinter
import image_processing
import resizing
import help_window

# Initialize the main application window
# root = tk.Tk()
customtkinter.set_default_color_theme('green')
root =  customtkinter.CTk()
root.title("Mouse Drawing Sketch")

# Create a canvas widget for drawing
width = 1048
height = 715
canvas = tk.Canvas(root, width=width, height=height, bg="white")
# root.geometry("1048x715")
canvas.pack()

# Initialize drawing variables
draw_color = "black"
drawing = False
prev_x, prev_y = None, None
newLine = True
newSquare = True

mode = "draw"

pencil_button = None
select_button = None
eraser_button = None
completion = None
# Function to start drawing when the mouse is clicked
def mouse_clicked(event):
    global drawing, prev_x, prev_y, start_x, start_y, mode
    if mode == "draw":
        start_draw(event)
    else:
        start_select(event)

# Function to stop drawing when the mouse button is released
def mouse_released(event):
    global drawing, prev_x, prev_y, newLine, mode
    if mode == "draw":
        end_draw(event)
    else:
        end_select(event)


# Function to draw lines as the mouse moves
def mouse_dragged(event):
    global mode
    if mode == "draw":
        draw(event)
    elif mode == "select":
        select(event)
    else:
        erase(event)

def start_draw(event):
    global drawing, prev_x, prev_y
    drawing = True
    prev_x, prev_y = event.x, event.y

def draw(event):
    global drawing, prev_x, prev_y, newLine
    if drawing:
        if newLine:
            x, y = event.x, event.y
            # canvas.create_line(prev_x, prev_y, x, y, fill=draw_color, width=2)
            prev_x, prev_y = x, y
            newLine = False
        else:
            x, y = event.x, event.y
            canvas.create_line(prev_x, prev_y, x, y, fill=draw_color, width=2)
            prev_x, prev_y = x, y

def end_draw(event):
    global drawing, newLine
    drawing = False
    newLine = True

def start_select(event):
    global start_x, start_y
    start_x, start_y = event.x, event.y

def select(event):
    global start_x, start_y, newSquare
    if newSquare:
        start_x, start_y = event.x, event.y
        newSquare = False
    else:
        if start_x and start_y:
            x, y = event.x, event.y
            canvas.delete("rect")  # Delete any previous rectangles
            canvas.create_rectangle(
                start_x,
                start_y,
                x,
                y,
                outline="black",
                width=2,
                tags="rect"  # Add a tag to identify the rectangle
            )

def end_select(event):
    global start_x, start_y, mode, newSquare
    print("end select")

    x0, y0, x1, y1 = canvas.coords("rect")  # Get coordinates of the rectangle
    x0, y0, x1, y1 = int(x0), int(y0), int(x1), int(y1)
    print("comparison", x1, event.x)
    width = x1 - x0
    height = y1 - y0
    screenshot = None
    if width > 0 and height > 0:
        # Adjust the coordinates to be relative to the Tkinter window
        screenx0, screeny0 = root.winfo_x() + canvas.winfo_x() + x0 +4, root.winfo_y() + canvas.winfo_y() + y0 +4
        screenx1, screeny1 = screenx0 + width -8, screeny0 + height - 8 

        # Capture the content inside the adjusted rectangle
        screenshot = ImageGrab.grab(bbox=(screenx0, screeny0, screenx1, screeny1))

        # Display the captured content
        # screenshot.show()
    canvas.delete("rect")  # Delete any previous rectangles
    start_x, start_y = None, None
    newSquare = True
    print("updated", x1)
    place_image(screenshot, x0, y0, x1, y1)
    help_window.main("15 + 7", "22")
    
    
def erase(event):
    x, y = event.x, event.y
    canvas.create_rectangle(x - 5, y - 5, x + 5, y + 5, fill="white", outline="white")
    
def place_image(input_img, x0, y0, x1, y1):
    global completion
    output_img = image_processing.hand_to_hand(input_img)
    
    print("newest x1", x1)
    tarHeight = (y1 - y0)*3/4
    
    aspectRatio = output_img.width/output_img.height
    tarWidth = tarHeight * aspectRatio
    print("new sizes", int(tarWidth), int(tarHeight))
    output_img = output_img.resize((int(tarWidth), int(tarHeight)))
    # (y0, y1, x0, x1), output_img = resizing.insert_image(output_img, (y0, y1-1, x0, x1-1), (0, height, 0, width))

    output_img = ImageTk.PhotoImage(output_img)
    completion = customtkinter.CTkButton(master =root, image=output_img, state = "disabled", fg_color ='white', text = "")
    centerLine = (y0+y1)/2
    orgX = x1
    orgY = centerLine - tarHeight/2
    print("CL",centerLine)
    print("orgY",orgY)
    print("orgX",orgX)
    print("tarSize", tarWidth, tarHeight)
    completion.place(x= orgX, y=orgY)


    

# Create buttons to change drawing color
def change_color(new_color):
    global draw_color
    draw_color = new_color

def set_mode_select():
    global mode, select_button, pencil_button
    mode = "select"
    select_button.configure(fg_color ='#c9c9c9')
    pencil_button.configure(fg_color ='white')
    eraser_button.configure(fg_color ='white')

def set_mode_draw():
    global mode, select_button, select_button
    mode = "draw"
    pencil_button.configure(fg_color ='#c9c9c9')
    select_button.configure(fg_color ='white')
    eraser_button.configure(fg_color ='white')

def set_mode_erase():
    global mode, select_button, select_button
    mode = "erase"
    eraser_button.configure(fg_color ='#c9c9c9')
    pencil_button.configure(fg_color ='white')
    select_button.configure(fg_color ='white')




# black_button = tk.Button(root, text="Black", command=lambda: change_color("black"))
# black_button.pack(side=tk.LEFT)

# red_button = tk.Button(root, text="Red", command=lambda: change_color("red"))
# red_button.pack(side=tk.LEFT)

# blue_button = tk.Button(root, text="Blue", command=lambda: change_color("blue"))
# blue_button.pack(side=tk.LEFT)

# select_button = tk.Button(root, text="Select", command=set_mode_select)
# select_button.pack(side=tk.LEFT)

# style = ttk.Style()
# style.configure("RoundedButton.TButton", borderwidth=0, relief="flat", padding = -1, foreground="white")
pencilIcon = Image.open("pencil.png")
pencilIcon = pencilIcon.resize((30, 30))
pencilIcon = ImageTk.PhotoImage(pencilIcon)
# pencilIcon = tk.PhotoImage(file="pencil.png")
pencil_button = customtkinter.CTkButton(master =root, image = pencilIcon, width = 50, height = 50, fg_color ='#c9c9c9', text = "", border_width =0, hover_color = '#c9c9c9', corner_radius = 0, command = set_mode_draw)
pencil_button.place(x= width/2 + 50, y=20)

selectIcon = Image.open("select.png")
selectIcon = selectIcon.resize((40, 40))
selectIcon = ImageTk.PhotoImage(selectIcon)
# pencilIcon = tk.PhotoImage(file="pencil.png")
select_button = customtkinter.CTkButton(master =root, image = selectIcon, width = 50, height = 50, fg_color = 'white', text = "", border_width =0,  hover_color = '#c9c9c9', corner_radius = 0, command = set_mode_select)
select_button.place(x= width/2 - 50 -30, y=20)

eraserIcon = Image.open("eraser.png")
eraserIcon = eraserIcon.resize((40, 40))
eraserIcon = ImageTk.PhotoImage(eraserIcon)
# pencilIcon = tk.PhotoImage(file="pencil.png")
eraser_button = customtkinter.CTkButton(master =root, image = eraserIcon, width = 50, height = 50, fg_color = 'white', text = "", border_width =0,  hover_color = '#c9c9c9', corner_radius = 0, command = set_mode_erase)
eraser_button.place(x= width/2 - 13, y=20)

# Bind mouse events to canvas
canvas.bind("<Button-1>", mouse_clicked)
canvas.bind("<ButtonRelease-1>", mouse_released)
canvas.bind("<B1-Motion>", mouse_dragged)

# Run the Tkinter main loop
root.mainloop()
