from tkinter import *
import random
import winsound
window = Tk()
window.title('Bhgnr maze version')
window.call('wm', 'iconphoto', window._w, PhotoImage(file='icon.gif'))

canvas = Canvas(window, width=768, height=768)
canvas.pack()


access_tile=[]
no_access_tile=[]

start_game=False

char_speed = 10

#Dictionaries of tiles gets created so it can store the tiles
level1_tiles= {}
for x in range(1,11):
    for y in range(1,11):
        level1_tiles[str(x)+' '+str(y)] = None #the coordinates are currently strings but will be turned into integers

level2_tiles= {}
for x in range(1,11):
    for y in range(1,11):
        level2_tiles[str(x)+' '+str(y)] = None

level3_tiles= {}
for x in range(1,11):
    for y in range(1,11):
        level3_tiles[str(x)+' '+str(y)] = None
        
#Now for the tiles
level1_tiles['1 1'] = 'access'
level1_tiles['1 2'] = 'access'
level1_tiles['2 2'] = 'access'
level1_tiles['3 2'] = 'access'
level1_tiles['4 2'] = 'access'
level1_tiles['5 2'] = 'access'
level1_tiles['6 2'] = 'access'
level1_tiles['6 3'] = 'access'
level1_tiles['6 4'] = 'access'
level1_tiles['6 5'] = 'access'
level1_tiles['6 6'] = 'access'
level1_tiles['6 7'] = 'access'
level1_tiles['7 7'] = 'access'
level1_tiles['7 6'] = 'access'

for tile in level1_tiles:
    if level1_tiles[tile]=='access':
        coords=tile.split()
        x_coords = int(coords[0])
        y_coords = int(coords[1])
        canvas.create_rectangle(x_coords*64-64,y_coords*64-64,x_coords*64,y_coords*64, fill='black')
        
edosh_image = PhotoImage(file="players/edoshearless.gif")
mychar = canvas.create_image(32, 32, image = edosh_image, state=NORMAL)

def check_if_on_access_tile():
    (playerx, playery) = canvas.coords(mychar)
    y_access_coords=[]
    x_access_coords=[]
    for tile in level1_tiles:
        if level1_tiles[tile]=='access':
            access_coords=tile.split()
            x_access=access_coords[0]
            y_access=access_coords[1]
            y_
    if playerx not in x_access_coords and playery not in y_access_coords:
        if move_direction == "Right":
            canvas.move(mychar,-1,0)
        if move_direction == "Left":
            canvas.move(mychar,1,0)
        if move_direction == "Up":
            canvas.move(mychar,0,1)
        if move_direction == "Down":
            canvas.move(mychar,0,-1)
    window.after(10, check_if_on_access_tile)

    
move_direction = 0 
def check_input(event):
    global move_direction, char_movement, start_game
    key = event.keysym
    if key == "Right" or key.lower() == "d":
        move_direction = "Right"
        char_movement=True
    elif key == "Left" or key.lower() == "a":
        move_direction = "Left"
        char_movement=True
    elif key == "Up" or key.lower() == "w":
        move_direction = "Up"
        char_movement=True
    elif key == "Down" or key.lower() == "s":
        move_direction = "Down"
        char_movement=True
    elif key == 'space':
        start_game = True
    
def end_input(event):
    global move_direction, char_movement
    move_direction = "None"
    char_movement=False
    
canvas.bind_all('<KeyPress>', check_input) 
canvas.bind_all('<KeyRelease>', end_input)

def move_character():
    if move_direction == "Right" and canvas.coords(mychar)[0] < 800:
        canvas.move(mychar, char_speed,0)
    elif move_direction == "Left" and canvas.coords(mychar)[0] > 0 :
        canvas.move(mychar, -char_speed,0)
    elif move_direction == "Up" and canvas.coords(mychar)[1] > 0:
        canvas.move(mychar, 0,-char_speed)
    elif move_direction == "Down" and canvas.coords(mychar)[1] < 600 :
        canvas.move(mychar, 0,char_speed)
    window.after(16, move_character)

def check_if_game_started():
    if not start_game:
        window.after(1, check_if_game_started)#it has to loop this function so it constantly checks if the player wants to start the game
    if start_game:#if it made sure the player started the game, it stops looping
        pass
        
window.after(1000, check_if_game_started)
window.after(1000, check_if_on_access_tile)
window.after(1000, move_character)
window.mainloop()
