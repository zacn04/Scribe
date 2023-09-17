from processing_py import *
import api
app = App(600,400) # create window: width, height

paths = []  # A list to store multiple paths
current_path = []  # The currently active path

selectState = 0

mode = 'write'
boxStartX = 0 
boxStartY = 0
number = 0

selectButtonWidth = 0
selectButtonHeight = 0
selectButtonX = 0
selectButtonY = 0
writeButtonWidth = 0
writeButtonHeight = 0
writeButtonX = 0
writeButtonY = 0



def setup():
    global paths, current_path, cp5, selectButtonWidth, selectButtonHeight, selectButtonX, selectButtonY, writeButtonWidth, writeButtonHeight, writeButtonX, writeButtonY
    selectButtonWidth = 30 
    selectButtonHeight = 30 
    selectButtonX = app.width/2 + 25 
    selectButtonY = 20 
    
    writeButtonWidth = 25 
    writeButtonHeight = 25 
    writeButtonX = width/2 - writeButtonWidth - 25 
    writeButtonY = 20
    
    app.size(1048, 715)
    app.background(255)
    
    paths = []  # Initialize a list to store multiple paths
    
    selectButtonImg = app.loadImage("select.png")
    selectButtonImg.resize(selectButtonWidth, selectButtonHeight)
    # cp5 = ControlP5(this)
    
    # (cp5.addButton('select')
    # .setPosition(selectButtonX, selectButtonY)
    # .onClick( lambda e: println("clicked") )
    # .setImage(selectButtonImg)
    # .updateSize()
    # )
    
    writeButtonImg = app.loadImage("pencil.png")
    writeButtonImg.resize(writeButtonWidth, writeButtonHeight)
    # cp5 = ControlP5(this)
    
    # (cp5.addButton('write')
    # .setPosition(writeButtonX, writeButtonY)
    # .onClick( lambda e: println("clicked") )
    # .setImage(writeButtonImg)
    # .updateSize()
    # )

def write():
    # Draw all the paths
    for path in paths:
        app.stroke(0)  # Set stroke color (black)
        app.strokeWeight(2)  # Set stroke weight
        app.noFill()  # Disable filling shapes
        app.beginShape()
        for pt in path:
            app.vertex(pt.x, pt.y)
        app.endShape()

    # Draw the current path
    if current_path:
        app.stroke(0)
        app.strokeWeight(2)
        app.noFill()
        app.beginShape()
        for pt in current_path:
            app.vertex(pt.x, pt.y)
        app.endShape()

def select():
    global selectState, boxStartX, boxStartY, number, image_to_text
    if selectState == 0:
        if mousePressed:
            boxStartX = app.mouseX
            boxStartY = app.mouseY
            selectState = 1
    elif selectState == 1:
        if mousePressed:
            app.noFill()
            app.rect(boxStartX, boxStartY, app.mouseX - boxStartX, app.mouseY - boxStartY)
        else:
            slice = app.get(boxStartX, boxStartY, app.mouseX - boxStartX, app.mouseY - boxStartY)
            slice.save("slice" + nf(number, 4) + ".png")
            app.println("saved to" + "slice" + app.nf(number, 4) + ".png")
            number += 1
            selectState = 0
            app.println(api.image_to_text("slice" + app.nf(number, 4) + ".png"))
            # println(api.image_to_text(slice))
            mode = "write"
            
def showSelectedButton():
    global selectButtonWidth, selectButtonHeight, selectButtonX, selectButtonY, writeButtonWidth, writeButtonHeight, writeButtonX, writeButtonY
    app.fill(200)
    if mode == 'select':
        app.rect(selectButtonX, selectButtonY, selectButtonWidth, selectButtonHeight, 5)
    else:
        app.rect(writeButtonX, writeButtonY, writeButtonWidth, writeButtonHeight, 5)
        
    

def keyPressed():
    global mode
    if app.key == 's':
        mode = 'select'
        startX = app.mouseX
        startY = app.mouseY
    if app.key == 'd':
        mode = 'write'
        
        
def mousePressed():
    # Start a new path when the mouse is pressed
    global current_path
    current_path = []
    if mode == 'write':
        pt = app.PVector(app.mouseX, appp.mouseY)
        current_path.append(pt)

def mouseDragged():
    # Store mouse coordinates as you drag
    if mode == 'write':
        pt = app.PVector(app.mouseX, app.mouseY)
        current_path.append(pt)

def mouseReleased():
    # Save the completed path to the list of paths
    global paths, current_path
    paths.append(current_path)
    current_path = []

while(True):    # Erase the entire canvas by setting the background
    app.background(255)
    showSelectedButton()
    write()
    if mode == 'select':
        select()