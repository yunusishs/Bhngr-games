"""Bhgnr. made by a dumb Expad who discovered the Duuds"""
#WARNING: this game is confusing
'''
Goal: beat as many levels as you can by avoiding the duuds and the bernard osh
      you try to collect coins and the oshes
'''
from tkinter import *
import random
import math
window = Tk()
window.title('Bhgnr')
window.call('wm', 'iconphoto', window._w, PhotoImage(file='icon.gif'))
'''
all the backgrounds
'''
canvas_width = 1280
canvas_height = 640
canvas = Canvas(window, width=canvas_width, height=canvas_height)
canvas.pack()

bg=PhotoImage(file='backgrounds/bg.gif')
level1bg=PhotoImage(file='backgrounds/level 1 bg.gif')
level2bg=PhotoImage(file='backgrounds/level 2 bg.gif')
level3bg=PhotoImage(file='backgrounds/level 3 bg.gif')
level4bg=PhotoImage(file='backgrounds/level 4 bg.gif')
level5bg=PhotoImage(file='backgrounds/level 5 bg.gif')
level6bg=PhotoImage(file='backgrounds/level 6 bg.gif')
level7bg=PhotoImage(file='backgrounds/level 7 bg.gif')

start_game = False

game_bg = canvas.create_image(canvas_width/2,canvas_height/2, image=bg)
title = canvas.create_text(canvas_width/2, canvas_height/2-100, text= 'The Edosh Fighters', fill='red', font = ('consolas', 30,'bold'))
directions = canvas.create_text(canvas_width/2, canvas_height/2+100, text= 'Collect coins and oshes but avoid the enemies', fill='white', font = ('consolas', 20))
press_to_start = canvas.create_text(canvas_width/2, canvas_height/2+200, text="Press 'space' to start", font = ('consolas',20))

health = 1
health_display = Label(window, text="Health :" + str(health), font = ('consolas', 20, 'bold'))
health_display.pack()
health_bar = Canvas(window, width=300, height=20,bg='grey')
health_bar.pack()
health_bar_display=health_bar.create_rectangle(3,3,20,20,fill='red',outline='black',width=3)

score = 0
level = 0
time = 0
score_displays = Label(window, text="Score :" + str(score) + " Level :" + str(level) + " Time :" + str(time), font = ('consolas', 20, 'bold'))
score_displays.pack()

edosh_image = PhotoImage(file="players/edoshearless.gif")
mychar = canvas.create_image(canvas_width/2, canvas_height/2, image = edosh_image, state=NORMAL)
char_speed = 2
char_movement = False

coin_list = []
bernard_osh_list = []
duud_bot_list = []
pduud_list = []
cduud_list = []
boss_list = []
kunai_list = []
osh_list = []
coin_speed = 2 #this may look slow but the frame rate is high on the coins
bot_img=PhotoImage(file='enemies/bot.gif')
bernard_img=PhotoImage(file='enemies/bernardosh.gif')
pduud_img=PhotoImage(file='enemies/pduud.gif')
cduud_img=PhotoImage(file='enemies/cduud.gif')
kunai_img=PhotoImage(file='enemies/kunai.gif')
boss_img=PhotoImage(file='enemies/duudboss.gif')
osh_img=PhotoImage(file='oshes/osh.gif')
drain=False #drain is on when the character gets hit by duud
end_the_game=False #what do you think will happen

def make_coin():
    xposition = random.randint(0,canvas_width)
    coin = canvas.create_oval(xposition, -32, xposition+32, 0, width=4, fill='yellow', outline='red')
    coin_list.append(coin)
    window.after(1000, make_coin)
def make_osh():
    xposition = random.randint(0,canvas_width)
    osh = canvas.create_image(xposition, -32, image=osh_img)
    osh_list.append(osh)        
    window.after(2000, make_osh)
def move_coin():
    for coin in coin_list:
        canvas.move(coin, 0, coin_speed)
        if canvas.coords(coin)[1] > canvas_height:
            xposition = random.randint(0,canvas_width)
            canvas.coords(coin, xposition, 0, xposition+32,32)
    window.after(1, move_coin)
    
def move_osh():
    for osh in osh_list:
        canvas.move(osh, 0, 1)
        if canvas.coords(osh)[1] > canvas_height:
            canvas.delete(osh)
            osh_list.remove(osh)
    window.after(1,move_osh)
def move_enemies():
    for bot in duud_bot_list:
        (playerx, playery) = canvas.coords(mychar)
        (botx, boty) = canvas.coords(bot)
        if botx > playerx:
            canvas.move(bot, -0.5,0)
        if botx < playerx:
            canvas.move(bot, 0.5, 0)
        if boty > playery:
            canvas.move(bot, 0,-0.5)
        if boty < playery:
            canvas.move(bot, 0, 0.5)
        if canvas.coords(bot)[1] > canvas_height:
            canvas.delete(bot)
    for ber in bernard_osh_list:
        canvas.move(ber, random.randint(-1,1), 1.5)
        if canvas.coords(ber)[1] > canvas_height:
            canvas.delete(ber)
            bernard_osh_list.remove(ber)
    for pduud in pduud_list:
        canvas.move(pduud, random.randint(-1,1), 1.5)
        if canvas.coords(pduud)[1] > canvas_height:
            canvas.delete(pduud)
            pduud_list.remove(pduud)
    for cduud in cduud_list:
        canvas.move(cduud, random.randint(-1,1), 1.5)
        if canvas.coords(cduud)[1] > canvas_height:
            canvas.delete(cduud)
            cduud_list.remove(cduud)
    for kunai in kunai_list:
        canvas.move(kunai, random.randint(-1,1), -1.5)#kunai comes from the bottom
        if canvas.coords(kunai)[1] < 0:
            canvas.delete(kunai)
            kunai_list.remove(kunai)
    for boss in boss_list:
        canvas.move(boss, random.randint(-1,1), 2)
        if canvas.coords(boss)[1] > canvas_height:
            canvas.delete(boss)
            boss_list.remove(boss)
    window.after(1, move_enemies)
        
def update_time():
    global time
    if not end_the_game:
        time = time+1
    score_displays.config(text="Score :" + str(score) + " Level :" + str(level) + " Time :" + str(time))
    window.after(1000, update_time)
'''''''''
make functions to create enemies
'''''''''
def create_enemy(enemy_type, times, x=None, y=None):
    for i in range(times):#If no parameters for x and y, they will be random
        if not x:                
            xposition = random.randint(0,canvas_width)
        else:
            xposition = x
        if not y:
            if enemy_type == 'kunai':
               yposition = random.randint(canvas_height, canvas_height*2)
            else:
                yposition = random.randint(-canvas_height, 0)
        else:
            yposition = y
        if enemy_type == 'bot':
            duud_bot = canvas.create_image(xposition, yposition, image=bot_img)
            duud_bot_list.append(duud_bot)
        elif enemy_type == 'bernard osh':
            bernard_osh = canvas.create_image(xposition, yposition, image=bernard_img)
            bernard_osh_list.append(bernard_osh)
        elif enemy_type == 'pduud':
            pduud = canvas.create_image(xposition, yposition, image=pduud_img)
            pduud_list.append(pduud)
        elif enemy_type == 'cduud':
            cduud = canvas.create_image(xposition, yposition, image=cduud_img)
            cduud_list.append(cduud)
        elif enemy_type == 'kunai':
            kunai = canvas.create_image(xposition, yposition, image=kunai_img)
            kunai_list.append(kunai)
        elif enemy_type == 'boss':
            boss = canvas.create_image(xposition, yposition, image=boss_img)
            boss_list.append(boss)

''''''
def update_score_level():#every time the player scores a point, the program has to check it and then it will execute everything in this function
    global score, level, health
    score = score + 1
    if health <= 15 and health > 0:
        health = health+1
        if health > 15:
            health = 15
    if score >= 1 and score <= 10:
        if level != 1:
            canvas.delete(title)
            canvas.delete(directions)
            level = 1
            create_enemy('bot', 16)
            canvas.itemconfigure(game_bg, image=level1bg)
    if score >= 11 and score <= 20:
        if level != 2:
            level = 2
            create_enemy('bot', 4)
            create_enemy('bernard osh', 14)
            canvas.itemconfigure(game_bg, image=level2bg)
    if score >= 21 and score <= 30:
        if level != 3:
            level = 3
            create_enemy('bernard osh', 4)
            create_enemy('pduud', 7)
            canvas.itemconfigure(game_bg, image=level3bg)
    if score >= 31 and score <= 40:
        if level != 4:
            level = 4
            create_enemy('pduud', 6)
            create_enemy('cduud', 5)
            canvas.itemconfigure(game_bg, image=level4bg)
    if score >= 41 and score <= 50:
        if level != 5:
            level = 5
            create_enemy('pduud', 6)
            create_enemy('cduud', 6)
            create_enemy('kunai', 6)
            canvas.itemconfigure(game_bg, image=level5bg)
    if score >= 51 and score <= 60:
        if level != 6:
            level = 6
            create_enemy('bot', 8)
            create_enemy('bernard osh', 6)
            create_enemy('pduud', 6)
            create_enemy('cduud', 6)
            create_enemy('kunai', 4)
            canvas.itemconfigure(game_bg, image=level6bg)
    if score >= 61 and score <= 70:
        if level != 7:
            level = 7
            create_enemy('boss', 1)
            canvas.itemconfigure(game_bg, image=level7bg)
    if score >= 71 and score % 10 == 1:
        level = int((score-1)/10)+1
        create_enemy('bot', 8)
        create_enemy('bernard osh', 6)
        create_enemy('pduud', 4)
        create_enemy('cduud', 3)
        create_enemy('kunai', 2)
        create_enemy('boss', 1)
    score_displays.config(text="Score :" + str(score) + " Level :" + str(level) + " Time :" + str(time))
    
def health_bar_config():
    global health_bar_display
#                                it says 3
#                                because of
#                                a black outline
#                                                  *20 to be aligned with the health bar
    health_bar.coords(health_bar_display,3,3,health*20,20)
    health_display.config(text="Health :" + str(health))
    health_bar.itemconfigure(health_bar_display,fill='red',outline='black',width=3)
    window.after(1,health_bar_config)
def end_game_over():
    global char_speed, end_the_game
    char_speed = 0
    end_the_game = True

def end_whole_game():
    global kunai_list, boss_list, cduud_list, pduud_list, bernard_osh_list, duud_bot_list,\
           osh_list, coin_list, char_speed
    if end_the_game:#empty out everything
        kunai_list=[]
        boss_list=[]
        cduud_list=[]
        pduud_list=[]
        bernard_osh_list=[]
        duud_bot_list=[]
        osh_list=[]
        coin_list=[]
    window.after(1, end_whole_game)

def collision(item1, item2, distance):
    xdistance = abs(canvas.coords(item1)[0] - canvas.coords(item2)[0])
    ydistance = abs(canvas.coords(item1)[1] - canvas.coords(item2)[1])
    overlap = xdistance < distance and ydistance < distance
    return overlap

def stop_not_moving():
    global char_speed
    char_speed = 2
    
def stop_hiding():
    canvas.itemconfigure(mychar, state=NORMAL)

def drain_health():
    global health
    if drain and health !=1:
        health = health-1
        health_display.config(fg='red')
    window.after(1000, drain_health)

def check_hits():
    global char_speed, score, health, drain
    if health < 0:
        health = 0
    if health < 1:
        game_over = canvas.create_text(canvas.coords(mychar)[0], canvas.coords(mychar)[1], text= 'Game Over', fill='red', font = ('Consolas', 30))
        end_game_over()
    for boss in boss_list:
        (boss_x, boss_y) = canvas.coords(boss)
        if collision(mychar, boss, 384):#the duud boss will only shoot in a 384 radius
            if randrange(16) == 0:
                create_enemy('bot', 1, boss_x-128, boss_y)
        if collision(mychar, boss, 128):#the duud boss will attack edosh in a 128 radius
            canvas.delete(boss)
            boss_list.remove(boss)
            score=score-16
            health=int(health/5)
    for kunai in kunai_list:
        if collision(mychar, kunai, 64) and canvas.coords(kunai)[1] > canvas.coords(mychar)[1]:
            canvas.delete(kunai)
            kunai_list.remove(kunai)
            score=score-8
            health=int(health/2)
            char_speed=0
            window.after(2048, stop_not_moving)
    for cduud in cduud_list:
        if collision(mychar, cduud, 64):
            canvas.delete(cduud)
            cduud_list.remove(cduud)
            canvas.itemconfigure(mychar, state=HIDDEN)
            window.after(2048, stop_hiding)
    for pduud in pduud_list:
        if collision(mychar, pduud, 64):
            canvas.delete(pduud)
            pduud_list.remove(pduud)
            score=score-1
            char_speed = 0
            window.after(1024, stop_not_moving)
    for ber in bernard_osh_list:
        if collision(mychar, ber, 64):
            canvas.delete(ber)
            score=score-1
            bernard_osh_list.remove(ber)
            drain=True
    for bot in duud_bot_list:
        if collision(mychar, bot, 64):
            score = score - 1
            health=health-1
            canvas.delete(bot)
            duud_bot_list.remove(bot)
    for osh in osh_list:
        if collision(mychar, osh, 64):
            canvas.delete(osh)
            osh_list.remove(osh)
            drain=False
            health_display.config(fg='black')
            for i in 'osh!':
                update_score_level()
                #rather than doing score=score+4, i had to do update_score_level four times because every time the player scores, the program has to check
    for coin in coin_list:
        if collision(mychar, coin, 64):
            canvas.delete(coin)
            coin_list.remove(coin)
            update_score_level()
    score_displays.config(text="Score :" + str(score) + " Level :" + str(level) + " Time :" + str(time))
    window.after(1, check_hits)

move_direction = 0 
def check_input(event):
    global move_direction, char_movement, game_filter, start_game, difficulty, change_to_edosh_text, \
           change_to_bedosh_text, change_to_butter_text, change_to_frosht_text, change_to_oreosh_text, change_to_chocolosh_text
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

def move_back():
    if canvas.coords(mychar)[0] > canvas_width:
        canvas.move(mychar, -12,0)
    elif canvas.coords(mychar)[0] < 0 :
        canvas.move(mychar, 12,0)
    elif canvas.coords(mychar)[1] < 0:
        canvas.move(mychar, 0,12)
    elif canvas.coords(mychar)[1] > canvas_height :
        canvas.move(mychar, 0,-12)
    window.after(1, move_back)
    
def end_input(event):
    global move_direction, char_movement
    move_direction = "None"
    char_movement=False
    
canvas.bind_all('<KeyPress>', check_input) 
canvas.bind_all('<KeyRelease>', end_input)

def move_character():
    if move_direction == "Right" and canvas.coords(mychar)[0] < canvas_width:
        canvas.move(mychar, char_speed,0)
    elif move_direction == "Left" and canvas.coords(mychar)[0] > 0 :
        canvas.move(mychar, -char_speed,0)
    elif move_direction == "Up" and canvas.coords(mychar)[1] > 0:
        canvas.move(mychar, 0,-char_speed)
    elif move_direction == "Down" and canvas.coords(mychar)[1] < canvas_height :
        canvas.move(mychar, 0,char_speed)
    window.after(1, move_character)

def check_if_game_started():
    if not start_game:
        window.after(1, check_if_game_started)#it has to loop this function so it constantly checks if the player wants to start the game
    if start_game:#if it made sure the player started the game, it stops looping
        canvas.delete(press_to_start)
        window.after(1000, make_coin)
        window.after(1000, move_coin)
        window.after(1000, make_osh)
        window.after(1000, move_osh)
        window.after(1000, move_enemies)
        window.after(1000, check_hits)
        window.after(1000, move_back)     
        window.after(1000, update_time)
        window.after(1000, health_bar_config)
        window.after(1000, drain_health)
        window.after(1000, end_whole_game)
        
check_if_game_started()
move_character()
window.mainloop()
