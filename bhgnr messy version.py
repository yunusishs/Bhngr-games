"""Bhgnr. made by a dumb Expad who discovered the Duuds"""
#WARNING: this game is confusing
'''
Goal: beat as many levels as you can by avoiding the duuds and the bernard osh
      you try to collect coins and the oshes
'''
from tkinter import *
import random
import winsound
window = Tk()
window.title('Bhgnr')
window.call('wm', 'iconphoto', window._w, PhotoImage(file='icon.gif'))

'''
stuff to change the filter
'''
change_to_edosh_text="Press '1' to change to Sandbox"
change_to_edosh = Label(window, text=change_to_edosh_text, fg='cyan', font = ('consolas', 10,'bold'))
change_to_edosh.pack()

change_to_bedosh_text = "Press '2' to change to Very Easy"#the text is currently difficulty
change_to_bedosh = Label(window, text=change_to_bedosh_text, fg='blue', font = ('consolas', 10,'bold'))
change_to_bedosh.pack()
able_to_change_to_bedosh=False

change_to_butter_text = "Press '3' to change to Easy"#and this applies to the other characters
change_to_butter = Label(window, text=change_to_butter_text, fg='light green', font = ('consolas', 10,'bold'))
change_to_butter.pack()
able_to_change_to_butter=False

change_to_chocolosh_text = "Press '4' to change to Normal"#and this applies to the other characters
change_to_chocolosh = Label(window, text=change_to_chocolosh_text, fg='green', font = ('consolas', 10,'bold'))
change_to_chocolosh.pack()
able_to_change_to_chocolosh=False

change_to_oreosh_text = "Press '5' to change to Hard"
change_to_oreosh = Label(window, text=change_to_oreosh_text, fg='red', font = ('consolas', 10,'bold'))
change_to_oreosh.pack()
able_to_change_to_oreosh=False

change_to_frosht_text = ""
change_to_frosht = Label(window, text=change_to_frosht_text, fg='blue', font = ('consolas', 10, 'bold'))
change_to_frosht.pack()
able_to_change_to_frosht=False

'''
all the backgrounds
'''
canvas = Canvas(window, width=800, height=600)
canvas.pack()
bg=PhotoImage(file='backgrounds/bg.gif')
level1bg=PhotoImage(file='backgrounds/level 1 bg.gif')
level2bg=PhotoImage(file='backgrounds/level 2 bg.gif')
level3bg=PhotoImage(file='backgrounds/level 3 bg.gif')
level4bg=PhotoImage(file='backgrounds/level 4 bg.gif')
level5bg=PhotoImage(file='backgrounds/level 5 bg.gif')
level6bg=PhotoImage(file='backgrounds/level 6 bg.gif')
level7bg=None#the background depends on the filter
game_filter='expadshian'#game filter chnages as character changes
city = ''

start_game = False
difficulty = ''

game_bg = canvas.create_image(400,300, image=bg)
difficulty_display=canvas.create_text(400,20, text="You need to press a difficulty", font = ('consolas', 10,'bold'))
title = canvas.create_text(400, 200, text= 'The Edosh Fighters', fill='red', font = ('consolas', 30,'bold'))
directions = canvas.create_text(400, 300, text= 'Collect coins and oshes but avoid the duuds', fill='white', font = ('consolas', 20))
setting = canvas.create_text(120,20, text = city, fill = 'red', font = ('consolas', 10))
press_to_start = canvas.create_text(400,500, text="Press numbers 1 to 5 to select a difficulty", font = ('consolas',20))

health = 1
health_display = Label(window, text="Health :" + str(health), font = ('consolas', 20, 'bold'))
health_display.pack()
health_bar = Canvas(window, width=300, height=20,bg='grey')
health_bar.pack()
health_bar_display=health_bar.create_rectangle(3,3,300,20,fill='red',outline='black',width=3)

score = 0
level = 0
time = 0
score_displays = Label(window, text="Score :" + str(score) + " Level :" + str(level) + " Time :" + str(time), font = ('consolas', 20, 'bold'))
score_displays.pack()

edosh_image = PhotoImage(file="players/edoshearless.gif")
butter_image = PhotoImage(file="players/butter.gif")
chocolosh_image = PhotoImage(file="players/chocolosh.gif")
frosht_image = PhotoImage(file="players/frosht.gif")
bedosherus_image = PhotoImage(file="players/bedosherus.gif")
oreosh_image = PhotoImage(file="players/oreosh.gif")
mychar = canvas.create_image(400, 400, image = edosh_image, state=NORMAL)
char_speed = 10


coin_list = []
bernard_osh_list = []
duud_bot_list = []
av_duud_list = []
cduud_list = []
boss_list = []
kunai_list = []
top_barrier_list = []
left_barrier_list = []
osh_list = []
coin_speed = 0.05#this may look slow but the frame rate is high on the coins
bot_img=PhotoImage(file='enemies/bot.gif')
bernard_img=PhotoImage(file='enemies/bernardosh.gif')
average_duud_img=PhotoImage(file='enemies/duud.gif')
cduud_img=PhotoImage(file='enemies/cduud.gif')
kunai_img=PhotoImage(file='enemies/kunai.gif')
boss_img=PhotoImage(file='enemies/duudboss.gif')
barrier_img=PhotoImage(file='enemies/barrier.gif')
osh_img=PhotoImage(file='oshes/osh.gif')
bidshian_osh_img=PhotoImage(file='oshes/bidshian osh.gif')
zenish_osh_img=PhotoImage(file='oshes/zenish osh.gif')
idshian_osh_img=PhotoImage(file='oshes/idshian osh.gif')
heggonian_osh_img=PhotoImage(file='oshes/heggonian osh.gif')
cremish_osh_img=PhotoImage(file='oshes/cremish osh.gif')
drain=False #drain is on when the character gets hit by duud
end_the_game=False #what do you think will happen

def change_filter():
    if game_filter == 'expadshian':#(edosh)
        canvas.itemconfigure(mychar, image=edosh_image)
        for osh in osh_list:
            canvas.itemconfigure(osh, image=osh_img)
        for coin in coin_list:
            canvas.itemconfigure(coin, outline='red', fill='yellow')
    elif game_filter == 'heggonian':
        canvas.itemconfigure(mychar, image=bedosherus_image)
        for osh in osh_list:
            canvas.itemconfigure(osh, image=heggonian_osh_img)
        for coin in coin_list:
            canvas.itemconfigure(coin, outline='brown', fill='gold')
    elif game_filter == 'bidshian':
        canvas.itemconfigure(mychar, image=butter_image)
        for osh in osh_list:
            canvas.itemconfigure(osh, image=bidshian_osh_img)
        for coin in coin_list:
            canvas.itemconfigure(coin, outline='magenta', fill='gold')
    elif game_filter == 'zenish':
        canvas.itemconfigure(mychar, image=chocolosh_image)
        for osh in osh_list:
            canvas.itemconfigure(osh, image=zenish_osh_img)
        for coin in coin_list:
            canvas.itemconfigure(coin, outline='green', fill='gold')
    elif game_filter == 'cremish':
        canvas.itemconfigure(mychar, image=oreosh_image)
        for osh in osh_list:
            canvas.itemconfigure(osh, image=cremish_osh_img)
        for coin in coin_list:
            canvas.itemconfigure(coin, outline='brown',fill='white')
    elif game_filter == 'idshian':
        canvas.itemconfigure(mychar, image=frosht_image)
        for osh in osh_list:
            canvas.itemconfigure(osh, image=idshian_osh_img)
        for coin in coin_list:
            canvas.itemconfigure(coin, outline='dark blue',fill='white')
    window.after(10, change_filter)
def make_coin():
    xposition = random.randint(32,768)
    coin = canvas.create_oval(xposition, -30, xposition+30, 0, width=3)
    coin_list.append(coin)
    window.after(960, make_coin)
def make_osh():
    xposition = random.randint(32,768)
    if game_filter == 'expadshian':
        winsound.PlaySound("sounds/osh.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    if game_filter == 'bidshian':
        winsound.PlaySound("sounds/butter osh.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    #I haven't recorded all the other sounds yet
    if game_filter == 'heggonian':
        winsound.PlaySound("sounds/butter osh.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    if game_filter == 'cremish':
        winsound.PlaySound("sounds/butter osh.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    if game_filter == 'zenish':
        winsound.PlaySound("sounds/butter osh.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    if game_filter == 'cremish':
        winsound.PlaySound("sounds/butter osh.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
    osh = canvas.create_image(xposition, -30, image=osh_img)
    osh_list.append(osh)        
    window.after(2000, make_osh)
def move_coin():
    for coin in coin_list:
        canvas.move(coin, 0, coin_speed)
        if canvas.coords(coin)[1] > 600:
            xposition = random.randint(32,768)
            canvas.coords(coin, xposition, 0, xposition+30,30)
    for osh in osh_list:
        canvas.move(osh, 0, 1)
    window.after(1, move_coin)
def move_osh():
    for osh in osh_list:
        canvas.move(osh, 0, 2)
        if canvas.coords(osh)[1] > 600:
            canvas.delete(osh)
            osh_list.remove(osh)
    window.after(10,move_osh)
def move_enemies():
    for bot in duud_bot_list:
        canvas.move(bot, random.randint(-20,20), 10)
        if canvas.coords(bot)[1] > 600:
            canvas.coords(bot,random.randint(32,768),0)
    for ber in bernard_osh_list:
        canvas.move(ber, random.randint(-10,10), 5)
        if canvas.coords(ber)[1] > 600:
            canvas.delete(ber)
            bernard_osh_list.remove(ber)
    for duud in av_duud_list:
        canvas.move(duud, random.randint(-10,10), 10)
        if canvas.coords(duud)[1] > 600:
            canvas.delete(duud)
            av_duud_list.remove(duud)
    for duud in cduud_list:
        canvas.move(duud, random.randint(-10,10), 10)
        if canvas.coords(duud)[1] > 600:
            canvas.delete(duud)
            cduud_list.remove(duud)
    for kunai in kunai_list:
        canvas.move(kunai, random.randint(-10,10), -15)#kunai comes from the bottom
        if canvas.coords(kunai)[1] < 0:
            canvas.delete(kunai)
            kunai_list.remove(kunai)
    for barrier in top_barrier_list:
        canvas.move(barrier, random.randint(-10,10),10)
        if canvas.coords(barrier)[1] > 600:
            canvas.coords(barrier,random.randint(32,768),0)
    for left_barrier in left_barrier_list:
        canvas.move(left_barrier,10, random.randint(-10,10))
        if canvas.coords(left_barrier)[0] > 800:
            canvas.coords(left_barrier, 0, random.randint(32,768))
    for boss in boss_list:
        canvas.move(boss, random.randint(-10,10), 15)
        if canvas.coords(boss)[1] > 600:
            canvas.delete(boss)
            boss_list.remove(boss)
    window.after(50, move_enemies)
def limit_enemies():
    bot_times = 0
    if difficulty == 'Very Easy':
        bot_times = 1
    elif difficulty == 'Easy':
        bot_times = 3
    elif difficulty == 'Normal' or difficulty == 'Hard':
        bot_times = 7
    if len(duud_bot_list) > bot_times:#the amount of them are limited
        the_chosen_deleted = random.choice(duud_bot_list)
        canvas.delete(the_chosen_deleted)
        duud_bot_list.remove(the_chosen_deleted)
    barrier_times = 0
    if difficulty == 'Very Easy':
        barrier_times = 1
    elif difficulty == 'Easy':
        barrier_times = 2
    elif difficulty == 'Normal' or difficulty == 'Hard':
        barrier_times = 4
    if len(top_barrier_list) > barrier_times:
        the_chosen_deleted = random.choice(top_barrier_list)
        canvas.delete(the_chosen_deleted)
        top_barrier_list.remove(the_chosen_deleted)
    left_barrier_times = 0
    if difficulty == 'Very Easy':
        left_barrier_times = 1
    elif difficulty == 'Easy':
        left_barrier_times = 1
    elif difficulty == 'Normal' or difficulty == 'Hard':
        left_barrier_times = 2
    if len(left_barrier_list) > left_barrier_times:
        the_chosen_deleted = random.choice(left_barrier_list)
        canvas.delete(the_chosen_deleted)
        left_barrier_list.remove(the_chosen_deleted)
    window.after(10, limit_enemies)
        
def update_time():
    global time
    if not end_the_game:
        time = time+1
    score_displays.config(text="Score :" + str(score) + " Level :" + str(level) + " Time :" + str(time))
    window.after(1000, update_time)
'''''''''
make functions to create enemies
'''''''''
def create_enemy(enemy_type, times_input):
    if difficulty != 'Sandbox':
        if difficulty == 'Very Easy':
            times = 1
        elif difficulty == 'Easy':
            times = int(times_input/2)
            if times == 0:
                times = 1
        elif difficulty == 'Normal':
            times = times_input
        elif difficulty == 'Hard':
            times = times_input * 2
        for i in range(times):
            if enemy_type == 'bot':
                duud_bot = canvas.create_image(random.randint(0,800), random.randint(-600, 0), image=bot_img)
                duud_bot_list.append(duud_bot)
            elif enemy_type == 'bernard osh':
                bernard_osh = canvas.create_image(random.randint(0,800), random.randint(-600,0), image=bernard_img)
                bernard_osh_list.append(bernard_osh)
            elif enemy_type == 'duud':
                average_duud = canvas.create_image(random.randint(0,800), random.randint(-600,0), image=average_duud_img)
                av_duud_list.append(average_duud)
            elif enemy_type == 'cduud':
                cduud = canvas.create_image(random.randint(0,800), random.randint(-600,0), image=cduud_img)
                cduud_list.append(cduud)
            elif enemy_type == 'barrier':
                barrier = canvas.create_image(random.randint(0,800), random.randint(-600,0), image=barrier_img)
                top_barrier_list.append(barrier)
            elif enemy_type == 'left barrier':
                left_barrier = canvas.create_image(random.randint(-800,0), random.randint(0,600), image=barrier_img)
                left_barrier_list.append(left_barrier)
            elif enemy_type == 'kunai':
                kunai = canvas.create_image(random.randint(0,800), random.randint(600,1200), image=kunai_img)
                kunai_list.append(kunai)
def create_boss():
    if difficulty != 'Sandbox':
        boss = canvas.create_image(random.randint(400,650), random.randint(-400, -250), image=boss_img)
        boss_list.append(boss)    
''''''
def update_score_level():#every time the player scores a point, the program has to check it and then it will execute everything in this function
    global score, level, coin_speed, x, y, health
    score = score + 1
    if health <= 15 and health > 0:
        health = health+1
        if health > 15:
            health = 15
    coin_speed = coin_speed + 0.01
    if score == 1:#duud bot x 12
        level = 1
        create_enemy('bot', 12)
    elif score == 11:#bernard osh x12
        level = 2
        create_enemy('bernard osh', 12)
    elif score == 21:#duud bot and bernard osh x 6
        level = 3
        create_enemy('bot', 6)
        create_enemy('bernard osh', 6)
    elif score == 31:#duud bot and beranrd osh and av duud x3
        level = 4
        create_enemy('bot', 3)
        create_enemy('bernard osh', 3)
        create_enemy('duud', 3)
    elif score == 41:#camaflouge duud, average duud, beranrd osh x 4
        level = 5
        create_enemy('bernard osh', 4)
        create_enemy('duud', 4)
        create_enemy('cduud', 4)
    elif score == 51:#barrier,  bernard osh x6 left barrier, bernard osh, average duud x 4
        level=6
        create_enemy('bernard osh', 16)
        create_enemy('barrier', 16)
        create_enemy('left barrier', 6)
        create_enemy('duud', 6)
    elif score == 61:#kunai, bernard osh x3
        level=7
        create_enemy('bernard osh', 2)
        create_enemy('kunai', 2)
    elif score == 71:# one duud boss
        level = 8
        create_boss()
    elif score > 80 and (score-1)%10==0:
        level=(score+9)/10
        create_enemy('bot', 4)
        create_enemy('barrier', 4)
        create_enemy('bernard osh', 2)
        create_enemy('duud', 2)
        create_enemy('cduud', 2)
        create_enemy('kunai', 2)
    elif score > 80 and (score-1)%50==0:
        create_boss()
    score_displays.config(text="Score :" + str(score) + " Level :" + str(level) + " Time :" + str(time))
    
def health_bar_config():
    global health_bar_display
#                                it says 3
#                                because of
#                                a black outline
#                                                  *20 to be aligned with the health bar
    health_bar.coords(health_bar_display,3,3,health*20,20)
    health_display.config(text="Health :" + str(health))
    if game_filter == 'expadshian':
        health_bar.itemconfigure(health_bar_display,fill='red',outline='black',width=3)
    if game_filter == 'heggonian':
        health_bar.itemconfigure(health_bar_display,fill='yellow',outline='cyan',width=3)
    if game_filter == 'bidshian':
        health_bar.itemconfigure(health_bar_display,fill='pink',outline='blue',width=3)
    if game_filter == 'zenish':
        health_bar.itemconfigure(health_bar_display,fill='yellow',outline='green',width=3)
    if game_filter == 'cremish':
        health_bar.itemconfigure(health_bar_display,fill='white',outline='magenta',width=3)
    if game_filter == 'idshian':
        health_bar.itemconfigure(health_bar_display,fill='white',outline='blue',width=3)
    window.after(16,health_bar_config)
def end_game_over():
    global char_speed, end_the_game
    char_speed = 0
    end_the_game = True

    
def end_title():
    if level == 2:
        canvas.delete(title)
        canvas.delete(directions)
    window.after(1000,end_title)

def end_whole_game():
    global top_barrier_list, left_barrier_list, kunai_list, boss_list, cduud_list, av_duud_list, bernard_osh_list, duud_bot_list,\
           osh_list, coin_list, time
    if end_the_game:#empty out all enemies
        top_barrier_list=[]
        left_barrier_list=[]
        kunai_list=[]
        boss_list=[]
        cduud_list=[]
        av_duud_list=[]
        bernard_osh_list=[]
        duud_bot_list=[]
        osh_list=[]
        coin_list=[]
    window.after(1,end_whole_game)

def collision(item1, item2, distance):
    try:
        xdistance = abs(canvas.coords(item1)[0] - canvas.coords(item2)[0])
        ydistance = abs(canvas.coords(item1)[1] - canvas.coords(item2)[1])
        overlap = xdistance < distance and ydistance < distance
        return overlap
    except:#don't know why i have to add this
        pass
def stop_not_moving():
    global char_speed
    char_speed = 10
def stop_hiding():
    canvas.itemconfigure(mychar, state=NORMAL)

def drain_health():
    global health
    if drain and health !=1:
        health = health-1
        health_display.config(fg='red')
    window.after(1000, drain_health)

def change_background():
    global level, coin_speed, city, level7bg
    if level == 1:
        canvas.itemconfigure(game_bg, image=level1bg)
        city = 'Duudtown, Mintshies'
    elif level == 2:
        canvas.itemconfigure(game_bg, image=level2bg)
        city = 'Pyriltown, Expadshia'
    elif level == 3:
        canvas.itemconfigure(game_bg, image=level3bg)
        city='Duudtown, Mintshies'
    elif level == 4:
        canvas.itemconfigure(game_bg, image=level4bg)
        city='Duudtown, Mintshies'
    elif level == 5:
        canvas.itemconfigure(game_bg, image=level5bg)
        city='Trifletree, Mintshies'
    elif level == 6:
        canvas.itemconfigure(game_bg, image=level6bg)
        city='Trifletree, Mintshies'
    elif level >= 7:#this is what i meant
        if game_filter == 'expadshian':
            level7bg = PhotoImage(file='backgrounds/level 7 Oilosh.gif')
            city='Oilosh, Expadshia'
        if game_filter == 'heggonian':
            level7bg = PhotoImage(file='backgrounds/level 7 Honeykomb city.gif')
            city='Honeykomb city, Heggonia'
        if game_filter == 'bidshian':
            level7bg = PhotoImage(file='backgrounds/level 7 Pentimots.gif')
            city='Pentimots, Bidshia'
        if game_filter == 'zenish':
            level7bg = PhotoImage(file='backgrounds/level 7 Zenish Main City.gif')
            city='Not Available'
        if game_filter == 'cremish':
            level7bg = PhotoImage(file='backgrounds/level 7 Milkia.gif')
            city='Milkia, Creamia'
        if game_filter == 'idshian':
            level7bg = PhotoImage(file='backgrounds/level 7 Shopow.gif')
            city='Shopow, Idshia'
        canvas.itemconfigure(game_bg, image=level7bg)
    if level > 8:
        coin_speed = 2
    canvas.itemconfigure(setting, text=city)
    window.after(1000, change_background)
def check_hits():
    global char_speed, score, health, drain
    if health < 0:
        health = 0
    if health < 1:
        game_over = canvas.create_text(200, 200, text= 'Game Over', fill='red', font = ('Consolas', 30))
        window.after(2000, end_game_over)
    for barrier in top_barrier_list:
        if collision(mychar, barrier, 64):
            canvas.move(mychar, 0, 32)
    for left_barrier in left_barrier_list:
        if collision(mychar, left_barrier, 64):
            canvas.move(mychar, 32, 0)
    for boss in boss_list:
        (boss_x, boss_y) = canvas.coords(boss)
        if collision(mychar, boss, 384):#the duud boss will only shoot in a 384 radius
            winsound.PlaySound("sounds/weeh.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            average_duud = canvas.create_image(boss_x-250, boss_y, image=average_duud_img)
            for i in range(random.randint(1,5)):
                canvas.move(average_duud, random.randint(-50, 50), random.randint(-50, 50))
            av_duud_list.append(average_duud)
            kunai = canvas.create_image(boss_x-250, boss_y, image=kunai_img)
            for i in range(random.randint(1,5)):
                canvas.move(kunai, random.randint(-50, 50), random.randint(-50, 50))
            kunai_list.append(kunai)
        if collision(mychar, boss, 200):#the duud boss will attack edosh in a 200 radius
            canvas.delete(boss)
            boss_list.remove(boss)
            score=score-16
            health=int(health/5)
    for kunai in kunai_list:
        if collision(mychar, kunai, 64) and canvas.coords(kunai)[1] > canvas.coords(mychar)[1]:
            winsound.PlaySound("sounds/weeh.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            canvas.delete(kunai)
            kunai_list.remove(kunai)
            score=score-8
            health=int(health/2)
            char_speed=0
            window.after(3000, stop_not_moving)
    for duud in cduud_list:
        if collision(mychar, duud, 64):
            winsound.PlaySound("sounds/weeh.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            canvas.delete(duud)
            cduud_list.remove(duud)
            canvas.itemconfigure(mychar, state=HIDDEN)
            window.after(2048, stop_hiding)
    for duud in av_duud_list:
        if collision(mychar, duud, 64):
            canvas.delete(duud)
            av_duud_list.remove(duud)
            score=score-1
            char_speed = 0
            window.after(3000, stop_not_moving)
    for ber in bernard_osh_list:
        if collision(mychar, ber, 64):
            winsound.PlaySound("sounds/weeh.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
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
            winsound.PlaySound("sounds/osh.wav", winsound.SND_ASYNC | winsound.SND_ALIAS )
            canvas.delete(osh)
            osh_list.remove(osh)
            drain=False
            health_display.config(fg='black')
            for i in 'osh!':
                update_score_level()
                #rather than doing score=score+4, i had to do update_score_level four times because every time the player scores, the program has to check
    for coin in coin_list:
        if collision(mychar, coin, 64):
            winsound.PlaySound("sounds/coin", winsound.SND_ASYNC | winsound.SND_ALIAS )
            canvas.delete(coin)
            coin_list.remove(coin)
            update_score_level()
    score_displays.config(text="Score :" + str(score) + " Level :" + str(level) + " Time :" + str(time))
    window.after(10, check_hits)

def notice_to_change_filter():
    global change_to_butter_text, change_to_bedosh_text, change_to_chocolosh_text, change_to_oreosh_text, \
           change_to_frosht_text, able_to_change_to_butter, able_to_change_to_bedosh, able_to_change_to_frosht, able_to_change_to_oreosh, able_to_change_to_chocolosh
    if level > 7:
        change_to_bedosh_text="Press '9' to change to Bedosh"
        able_to_change_to_bedosh=True
        change_to_butter_text="Press '8' to change to Butter"
        able_to_change_to_butter=True
    if level > 15:
        change_to_chocolosh_text="Press '7' to change to Chocolosh"
        able_to_change_to_chocolosh=True
        change_to_oreosh_text="Press '6' to change to Oreosh"
        able_to_change_to_oreosh=True
    if level > 31:
        change_to_frosht_text="Press '5' to change to Frosht"
        able_to_change_to_frosht=True
    change_to_butter.config(text=change_to_butter_text)
    change_to_chocolosh.config(text=change_to_chocolosh_text)
    change_to_bedosh.config(text=change_to_bedosh_text)
    change_to_oreosh.config(text=change_to_oreosh_text)
    change_to_frosht.config(text=change_to_frosht_text)
    window.after(10, notice_to_change_filter)

move_direction = 0 
def check_input(event):
    global move_direction, game_filter, start_game, difficulty, change_to_edosh_text, \
           change_to_bedosh_text, change_to_butter_text, change_to_frosht_text, change_to_oreosh_text, change_to_chocolosh_text
    key = event.keysym
    if key == "Right" or key.lower() == "d":
        move_direction = "Right"
    elif key == "Left" or key.lower() == "a":
        move_direction = "Left"
    elif key == "Up" or key.lower() == "w":
        move_direction = "Up"
    elif key == "Down" or key.lower() == "s":
        move_direction = "Down"
    elif key == '0':
        game_filter = 'expadshian'
    elif key == '9' and able_to_change_to_bedosh:
        game_filter = 'heggonian'
    elif key == '8' and able_to_change_to_butter:
        game_filter = 'bidshian'
    elif key == '7' and able_to_change_to_chocolosh:
        game_filter = 'zenish'
    elif key == '6' and able_to_change_to_oreosh:
        game_filter = 'cremish'
    elif key == '5':
        if able_to_change_to_frosht:
            game_filter = 'idshian'
        if not start_game:
            difficulty='Hard'
    elif key == '1' and not start_game:
        difficulty='Sandbox'
    elif key == '2' and not start_game:
        difficulty='Very Easy'
    elif key == '3' and not start_game:
        difficulty='Easy'
    elif key == '4' and not start_game:
        difficulty='Normal'
    elif key == 'space':
        if difficulty == '':
            canvas.itemconfigure(press_to_start, text='Press a difficulty!', fill='red')
        elif difficulty != '':
            change_to_edosh_text="Press '0' to change to Edosh"
            change_to_bedosh_text=''
            change_to_butter_text=''
            change_to_chocolosh_text=''
            change_to_oreosh_text=''
            change_to_frosht_text=''
            change_to_edosh.config(fg='red',text=change_to_edosh_text)
            change_to_bedosh.config(fg='brown')
            change_to_butter.config(fg='magenta')
            change_to_chocolosh.config(fg='green')
            change_to_oreosh.config(fg='pink')
            change_to_frosht.config(fg='blue')
            start_game = True

def move_back():
    if canvas.coords(mychar)[0] > 800:
        canvas.move(mychar, -12,0)
    elif canvas.coords(mychar)[0] < 0 :
        canvas.move(mychar, 12,0)
    elif canvas.coords(mychar)[1] < 0:
        canvas.move(mychar, 0,12)
    elif canvas.coords(mychar)[1] > 600 :
        canvas.move(mychar, 0,-12)
    window.after(1, move_back)
    
def end_input(event):
    global move_direction
    move_direction = "None"
    
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

def check_difficulty():
    if difficulty != '':
        canvas.itemconfigure(difficulty_display, text ='Difficulty is currently '+difficulty)
        canvas.itemconfigure(press_to_start, text = "Press 'space' to start", fill='black')
    else:
        canvas.itemconfigure(difficulty_display, text ='You need to press a difficulty')
    if not start_game:
        window.after(10, check_difficulty)

def check_if_game_started():
    if not start_game:
        window.after(1, check_if_game_started)#it has to loop this function so it constantly checks if the player wants to start the game
    if start_game:#if it made sure the player started the game, it stops looping
        canvas.delete(press_to_start)
        window.after(1000, end_title)
        window.after(1000, make_coin)
        window.after(1000, move_coin)
        window.after(1000, make_osh)
        window.after(1000, move_osh)
        window.after(1000, move_enemies)
        window.after(1000, limit_enemies)
        window.after(1000, check_hits)
        window.after(1000, move_back)     
        window.after(1000, update_time)
        window.after(1000, change_filter)
        window.after(1000, change_background) 
        window.after(1000, health_bar_config)
        window.after(1000, drain_health)
        window.after(1000, end_whole_game)
        window.after(1000, notice_to_change_filter)
        
window.after(1000, check_if_game_started)
window.after(1000, check_difficulty)
window.after(1000, move_character)
window.mainloop()
