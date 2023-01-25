# hello mr. k. i'd like to preface this by saying i did my best to keep things as organized as possible, but because bugs popped up, and the mountain of if statements i used, things were hard to keep in order. i also feel like i am descending into madness for every line i add to this, which is quite evident in my variable names and the amount of stream points i earned from watching dantes.  while you read this file over, you can listen to my playlist https://open.spotify.com/playlist/025NB2bV280hNPwPpnnm0L?si=acdfd3d3edd346f4 to fully emcompass yourself in this madness (its the playlist i listen to when i played my lol placement matches + i think you like some of the artists on it). that said, i have done my best to comment things to help you understand how this stinky game works. please enjoy my amazing abomination of a final performance task.
                                                                                        
from pygame.locals import *                                                                            # we start off like any game, with a pygame, math and system import. unlike my past projects,
import pygame, math, sys                                                                               # this time i import pygame.locals, allowing me to add my own custom files and sprites!
                                                                                        
pygame.init()                                                                                          # i continue by initiating the game, and the 'mixer' function. 
pygame.mixer.init()
pygame.display.set_caption('A Stinky Game about being Smelly')                                         # setting the game title, screen size and some base colours, we are ready to begin.
SIZE = (1000, 700)
screen = pygame.display.set_mode(SIZE)
BLACK = [15, 15, 15]
INTROBACKGROUND = [247, 243, 228]
INTROTEXT = [156, 153, 144]

backgroundmusic = pygame.mixer.Channel(0)                                                              # back to the mixer function, i have 3 channels that allow me to play multiple sounds at once.
backgroundmusic.set_volume(0.1)                                                                        # all quite self explanitory, background music changes from level to level, voicelines are all
voicelines = pygame.mixer.Channel(1)                                                                   # done over by Stefan, Richard (some kid from texas (he's a lee sin main like you)), and Sun Min
voicelines.set_volume(10000000000000000000000000000000000000)                                          # to bring maximum realism to the game. finally soundeffects adds some funny to the silly game
soundeffects = pygame.mixer.Channel(2)
soundeffects.set_volume(1)

# -------------------------------- V A R I A B L E S --------------------------------------------------------------------------

# l e v e l s
run = True                                                                                             # with that, my onslaught of variables begin. the first chunk is for levels and baseline
menuscreen = True                                                                                      # stuff. i probably could have reduced this by turning them all into classes, but that
gamescreen = False                                                                                     # is a project for my next game. "STINKY STEFAN, RETURN OF THE STENCH" coming to 
howtoplayscreen = False                                                                                # a dropbox near you in 2024!
intro = False
bedroom = False
kitchen = False
school = False
lunch = False
bathroom = False
league = False

# m e n u   b u t t o n s
buttonStart = False                                                                                    # here are my menu buttons. if you look later at my win/lose screen, they are done the same way
buttonControls = False                                                                                 # with buttons that highlight when you hover on it. 
buttonExit = False

# b a s e l i n e   s t e f a n   c h e c k s                                                          # what i have dubbed baseline stefan checks are my most important features. 
clothingon = False                                                                                     # he needs his clothes, so this is an obvious checks
deoapplied = False                                                                                     # stefan passively gains more stink each level, if he has deodorant on it is reduced
outfit = ("")                                                                        
animation = False                                                                                      # animation lets stefan go invisible without the hassle of checking his outfit each time
mcx = 100                                                                                              # i try to animate something
vel = 5
mcoutfit = 'MAIN CHARACTER PLAIN OUTFIT.png'
message = ''
loops = 0                                                                                              # finally, loops lets me play music easy! you'll see it get reset a lot. will explain more below


# -------------------------------- F U N C T I O N S --------------------------------------------------------------------------

def titleScreen():                                                                                     # title screen. like all my functions, they start with a background (bg). then some items
    titlebg = pygame.image.load('TITLE SCREEN.png')                                                    # this is the only function i put if statements in. i did it more efficiently below, but
    screen.blit(titlebg, (0, 0))                                                                       # when i tried to change this screen, it broke. i keep it how it is, and just do a better job
                                                                                                       # below in lose/win screen
    if buttonStart == True:
        startbuttonpt = pygame.image.load('START BUTTON.png')
        screen.blit(startbuttonpt, (602, 137))      
    
    if buttonControls == True:
        controlsbuttonpt = pygame.image.load('CONTROLS BUTTON.png')
        screen.blit(controlsbuttonpt, (604, 273))  

    if buttonExit == True:
        exitbuttonpt = pygame.image.load('EXIT BUTTON.png')
        screen.blit(exitbuttonpt, (596, 399))  

    pygame.display.flip()

# co n t r o l s   s c r e e n   v a r i a b l e s
returnbutton = 'EMPTY.png'                                                                             # this is my first instance of 'EMPTY.png' the real mvp of the game.
def controlsScreen():                                                                                  # this png lets me only make objects visable once stefan needs to interact with them.
    controlsbg = pygame.image.load('HOW 2 PLAY.png')                                                   # everything else here is for my HOW 2 PLAY screen images. pretty self explanitory
    screen.blit(controlsbg, (0, 0))
    
    returnart = pygame.image.load(returnbutton)
    screen.blit(returnart, (0, 0))
    
    pygame.display.flip()    

# i n t r o   s c r e e n   v a r i a b l e s
spaceclicked = 0                                                                                       # here are my variables for intro screen. i wanted to demonstrate a knowledge of 
line1 = ''                                                                                             # pygame drawing, so i drew things in pygame like my halloween house.
line2 = ''                                                                                             # instead of a drawing with my tablet, i draw a rectangle for my background and then
line3 = ''                                                                                             # i blit text on the screen each time the player hits space.
line4 = ''                                                                                             # this also lets the player control and read the text on their own.
line5 = ''                                                                                             # it feels slightly out of place, but i think it is a neat addition!
line6 = ''
line7 = ''
def introScreen():                                                                                     # and then i draw my intro with these blits
    pygame.draw.rect(screen, INTROBACKGROUND, (0, 0, 1000, 700))  
    
    font = pygame.font.Font('fixedsys.ttf', 30)
    text = font.render(line1, False, BLACK)
    screen.blit(text, (125, 100)) 
    
    font = pygame.font.Font('fixedsys.ttf', 30)
    text = font.render(line2, False, BLACK)
    screen.blit(text, (125, 150)) 
    
    font = pygame.font.Font('fixedsys.ttf', 30)
    text = font.render(line3, False, BLACK)
    screen.blit(text, (125, 200)) 
    
    font = pygame.font.Font('fixedsys.ttf', 30)
    text = font.render(line4, False, BLACK)
    screen.blit(text, (125, 250)) 
    
    font = pygame.font.Font('fixedsys.ttf', 30)
    text = font.render(line5, False, BLACK)
    screen.blit(text, (125, 300)) 
    
    font = pygame.font.Font('fixedsys.ttf', 30)
    text = font.render(line6, False, BLACK)
    screen.blit(text, (125, 350)) 
    
    font = pygame.font.Font('fixedsys.ttf', 40)
    text = font.render(line7, False, INTROTEXT)
    screen.blit(text, (210, 500))     
    
    pygame.display.flip()                                                                              # at the end of each chunk of blits and sprites, i refresh the screen

# b e d r o o m   v a r i a b l e s
dresser = 'DRESSER CLOSED.png'                                                                         # so i realized that instead of adding if statements, i can just change the variable. whenever
dresserx = 620                                                                                         # stinky stefan interacts with the environement, the object changes, editing image on the screen.
laundry = 'LAUNDRY BIN.png'                                                                            # for example, when stefan walks over the dresser, it opens. in order to do this, i change the x
deodorant = 'DEODORANT.png'                                                                            # and blitted image in the function to show his interaction. its the same for everything else
stinklevel = 20
stink = 'STINK METER 0%.png'
beddoor = 'EMPTY.png'
beddooropen = 'EMPTY.png'
def bedroomScreen():                                                                                   # being his first level, all of stefan's bedroom items are printed here
    bedroombg = pygame.image.load('BEDROOM BACKGROUND.png')
    screen.blit(bedroombg, (0, 0))

    dresserart = pygame.image.load(dresser)
    screen.blit(dresserart, (dresserx, 314)) 
    
    beddoorart = pygame.image.load(beddoor)
    screen.blit(beddoorart, (870, 200))       
    
    mcart = pygame.image.load(mcoutfit)
    screen.blit(mcart, (mcx, 230))  
    
    beddooropenart = pygame.image.load(beddooropen)
    screen.blit(beddooropenart, (870, 200))     
    
    laundryart = pygame.image.load(laundry)
    screen.blit(laundryart, (270, 560))
    
    nightstandart = pygame.image.load('NIGHTSTAND.png')
    screen.blit(nightstandart, (0, 540))
    
    deodorantart = pygame.image.load(deodorant)
    screen.blit(deodorantart, (80, 535))    
    
    thestinkmeter = pygame.image.load(stink)
    screen.blit(thestinkmeter, (0, 0))   
    
    pygame.display.flip()   

# k i t c h e n   v a r i a b l e s              
fridge = 'FRIDGE.png' 
lunch = 'EMPTY.png'
kitchendoor = 'EMPTY.png'
kitchendooropen = 'EMPTY.png'
chair = 'BREAKFAST CHAIR.png'
breakfasteaten = False                                                                                 # welcome to the kitchen. this is where stefan eats his breakfast and packs his lunch. however,
lunchpacked = False                                                                                    # i had problems come up with him eating and cut scenes triggering before they were needed,
eating = False                                                                                         # so my variables come in clutch and only change once the action has happened. all the variables
bellrung = False                                                                                       # dictate when to run certain scenes, and let the door pop up to let him go to the next level.
eat = 0
def kitchenScreen():                                                                                   # after my variables are dictated, i print my objects on the screen.
    kitchenbg = pygame.image.load('KITCHEN BACKGROUND.png')
    screen.blit(kitchenbg, (0, 0))    
    
    fridgeart = pygame.image.load(fridge)
    screen.blit(fridgeart, (50, 200))
    
    lunchart = pygame.image.load(lunch)
    screen.blit(lunchart, (50, 200))    
    
    kitchdoorart = pygame.image.load(kitchendoor)
    screen.blit(kitchdoorart, (750, 168))
    
    mcart = pygame.image.load(mcoutfit)                                                                # if you notice, the 'Main Character ART' is in almost every function. i put him in the middle so
    screen.blit(mcart, (mcx, 230))                                                                     # i can create depth by placing objects in front of him, or behind him.
    
    kitchdooropenart = pygame.image.load(kitchendooropen)
    screen.blit(kitchdooropenart, (750, 168))  
    
    tableart = pygame.image.load('DINING TABLE.png')
    screen.blit(tableart, (655, 450))
    
    chairart = pygame.image.load(chair)
    screen.blit(chairart, (550, 262))
    
    thestinkmeter = pygame.image.load(stink)                                                           # stink meter is also in every single level (almost). it's kind of important given the nature of
    screen.blit(thestinkmeter, (0, 0))                                                                 # the game.
    
    pygame.display.flip()   

# s c h o o l   v a r i a b l e s
tdesk = 'TEACHER SANITIZER.png'
klimo = 'MR. K.png'                                                                                    # surprise! you're in the game. you knew that already tho. just like above, i state my variables 
flip = True                                                                                            # change them once stefan needs to interact with the environement. 
desk = 'DIRTY DESK.png'                                                                
hansan = 'EMPTY.png'
dream = 'EMPTY.png'
hansanx = 180 # hasan is an inside joke in the friend group. i read handsan as 'hasan' when i first wrote it, so i left it as a little easter egg if any of my friends read over the code.
handsan = False
ddesk = True
classdoor = 'EMPTY.png'
cclassdoor = 'EMPTY.png'
def classroomScreen():                                                                                 # print the drawings on the screen! what a surprise! its the same as above!!!!
    classbg = pygame.image.load('CLASSROOM BACKGROUND.png')                        
    screen.blit(classbg, (0, 0))       

    klimart = pygame.image.load(klimo)                                                                 # i did something funky with your character. as you'll see in game and below, you move (slightly)
    screen.blit(klimart, (550, 200))                                                                   # as time progresses, you pivot and turn. i was going to make you track stefan, but i needed
                                                                                                       # a feature like this for later, so i just did this instead.
    teacherdeskart = pygame.image.load(tdesk)
    screen.blit(teacherdeskart, (475, 375))
    
    classdoorart = pygame.image.load(classdoor)
    screen.blit(classdoorart, (820, 230))
    
    mcart = pygame.image.load(mcoutfit)
    screen.blit(mcart, (mcx, 230))    
    
    cclassdoorart = pygame.image.load(cclassdoor)
    screen.blit(cclassdoorart, (820, 230))    
    
    hansart = pygame.image.load(hansan)
    screen.blit(hansart, (mcx+hansanx, 460))
    
    dreamart = pygame.image.load(dream)
    screen.blit(dreamart, (0, 0))
    
    deskart = pygame.image.load(desk)
    screen.blit(deskart, (-50, 85))
    
    thestinkmeter = pygame.image.load(stink)
    screen.blit(thestinkmeter, (0, 0))    

    pygame.display.flip()   

# l u n c h   v a r i a b l e s
fhdoor = 'W202.png'
frenchhdoor = 'EMPTY.png'
choi = 'SUN MIN COOKIE.png'
heeatshislunch = 'EMPTY.png'
lunchtime = False
luncheaten = False
def frencHall():                                                                                       # french hall is where we all eat lunch. therefore, this function blits our lunch photos
    frenchhallbg = pygame.image.load('FRENCH HALL.png')                        
    screen.blit(frenchhallbg, (0, 0))    
    
    fhalldoorart = pygame.image.load(fhdoor)
    screen.blit(fhalldoorart, (700, 230))
    
    sunmart = pygame.image.load(choi)                                                                  # fun fact, the french hall door is called W202 because originally he was going to have
    screen.blit(sunmart, (300, 470))                                                                   # another class after lunch. i didn't have time, and just made it a go home door after lunch
    
    mcart = pygame.image.load(mcoutfit)
    screen.blit(mcart, (mcx, 230))    
    
    stefanlunchart = pygame.image.load(heeatshislunch)
    screen.blit(stefanlunchart, (100, 382))
    
    frenchallart = pygame.image.load(frenchhdoor)
    screen.blit(frenchallart, (700, 230))      
    
    thestinkmeter = pygame.image.load(stink)
    screen.blit(thestinkmeter, (0, 0))       
    
    pygame.display.flip()   

# b a t h r o o m   v a r i a b l e s
stalldoor = 'STALL DOOR.png'
poop = False
soap = 'SOAP.png'
sink = 'SINK.png'
washhands = False
washing = True
soapused = False
hewasheshishands = 'EMPTY.png'
handswashed = False
secondtime = False
def lesToilettes():                                                                                    # because he was just in french hall, the bathroom is in french. stefan's bathroom adventures
    bathroombg = pygame.image.load('LES TOILETTES.png')                                                # are printed in this function.
    screen.blit(bathroombg, (0, 0)) 
    
    sinkart = pygame.image.load(sink)
    screen.blit(sinkart, (0, 0))
    
    soapart = pygame.image.load(soap)
    screen.blit(soapart, (0, -100))
    
    mcart = pygame.image.load(mcoutfit)
    screen.blit(mcart, (mcx, 230))  
    
    mcwashart = pygame.image.load(hewasheshishands)
    screen.blit(mcwashart, (40, 230))
    
    outertoiart = pygame.image.load(stalldoor)
    screen.blit(outertoiart, (0, 0))
    
    thestinkmeter = pygame.image.load(stink)
    screen.blit(thestinkmeter, (0, 0))       
    
    pygame.display.flip()   

# h o m e   s t r e t c h
thekitchen = False
thebedroom = False
goodending = False
tablea = 'DINING TABLE.png'
thebackground = 'KITCHEN BACKGROUND END.jpg'
gamingstation = 'EMPTY.png'
def homeStretch():                                                                                     # this is it! the final level. after lunch, stefan goes home to play league. this is
    homestrechbg = pygame.image.load(thebackground)                                                    # this is where his 'edited' home is printed
    screen.blit(homestrechbg, (0, 0)) 
    
    gamingstationart = pygame.image.load(gamingstation)
    screen.blit(gamingstationart, (0, 0))
    
    mcart = pygame.image.load(mcoutfit)
    screen.blit(mcart, (mcx, 230))  
    
    tableart = pygame.image.load(tablea)
    screen.blit(tableart, (655, 450))
    
    chairart = pygame.image.load(chair)
    screen.blit(chairart, (550, 262))    
    
    thestinkmeter = pygame.image.load(stink)
    screen.blit(thestinkmeter, (0, 0))       
    
    pygame.display.flip()       

# e n d i n g   v a r i a b l e s                                                                      # the ending variables are the same for the good and bad ending, it's essentially the same bg 
replaybuttoning = 'EMPTY.png'                                                                          # too (with buttons), but some things change, so i keep it separate. in the future, i will 
mainmenubuttoning = 'EMPTY.png'                                                                        # combine them since it will be less hassle
exitbuttoning = 'EMPTY.png'
replay = False
def itslikeitsWinnersqueue():                                                                          # this is what dantes says when he is winning, so if they get the good ending, winners queue
    winnerqbg = pygame.image.load('WINNER QUEUE.png')                                                  # prints that ending on the screen. 
    screen.blit(winnerqbg, (0, 0))

    replayart = pygame.image.load(replaybuttoning)
    screen.blit(replayart, (0, 0))
    
    mmart = pygame.image.load(mainmenubuttoning)
    screen.blit(mmart, (0, 0))
    
    ebart = pygame.image.load(exitbuttoning)
    screen.blit(ebart, (0, 0))    

    pygame.display.flip()

# d e a t h   v a r i a b l e s
stefandead = 'STEFAN DIE UP.png'
deathscreen = False
def danteslosttheRace():                                                                               # in my website, i mention i was watching the "DANTES CHALLENGER RACE". spoiler; he lost. 
    loserqbg = pygame.image.load('LOSER QUEUE.png')                                                    # therefore, if stefan dies of stench, dantes loss is booted up as the loser screen.
    screen.blit(loserqbg, (0, 0))
    
    replayart = pygame.image.load(replaybuttoning)
    screen.blit(replayart, (0, 0))
    
    mmart = pygame.image.load(mainmenubuttoning)
    screen.blit(mmart, (0, 0))
    
    ebart = pygame.image.load(exitbuttoning)
    screen.blit(ebart, (0, 0))    
    
    stefandeadart = pygame.image.load(stefandead)
    screen.blit(stefandeadart, (mcx, 230))

    pygame.display.flip()    


# -------------------------------- G A M E --------------------------------------------------------------------------

while run:                                                                                             # new record: game starts at line 390. this game is over 1000 lines!!! YAY!! :,)
    while menuscreen == True:                                                                          # starting with our menu screen. 
        loops += 1
        titleScreen()                                                                                  # like all the subsiquent levels, i start by printing the background which refreshes for me
        
        if loops == 1:                                                                                 # loops! my favourite variable. this loops if statement starts my menu music up for me, letting 
            backgroundmusic.play(pygame.mixer.Sound('loading screen.mp3'), -1)                         # the music not start a million times everytime it goes through the menu screen
        
        for event in pygame.event.get():
            (mousex, mousey) = pygame.mouse.get_pos()                                                  # when the mouse hovers over my buttons, it changes the colour of the button to signify the button
            if mousex >= 625 and mousex <= 860 and mousey >= 165 and mousey <= 235:                    # has been selected
                buttonStart = True
            else:
                buttonStart = False
            if mousex >= 630 and mousex <= 860 and mousey >= 295 and mousey <= 370:
                buttonControls = True                
            else:
                buttonControls = False                
            if mousex >= 630 and mousex <= 860 and mousey >= 430 and mousey <= 500:
                buttonExit = True                
            else:
                buttonExit = False             
                
            if event.type == MOUSEBUTTONDOWN:                                                          # if the mouse clicks, an event is triggered
                mousex, mousey = event.pos
                if mousex >= 625 and mousex <= 860 and mousey >= 165 and mousey <= 235:                # this is my start button. it turns off the menu while loop and boots up the game
                    menuscreen = False
                    gamescreen = True
                    intro = True
                    loops = 0
                if mousex >= 630 and mousex <= 860 and mousey >= 295 and mousey <= 370:
                    menuscreen = False                                                                 # this is my HOW2PLAY screen. it turns off the menu while loop and boots up the h2p screen
                    howtoplayscreen = True  
                if mousex >= 630 and mousex <= 860 and mousey >= 430 and mousey <= 500:
                    menuscreen = False                                                                 # dont want to play? i have a quit button
                    pygame.quit()
                    sys.exit()        
            if event.type == QUIT:                                                                     # if the game crashes, or the 'x' button is pressed, this loop lets it stop effectively
                pygame.quit()
                sys.exit()  
                
    while howtoplayscreen == True:                                                                     # when you press the how to play button, it boots up this screen.
        controlsScreen()                                                                               # i start with my images using the function made for it
        
        for event in pygame.event.get():                                                               # then, like above, it sees if the mouse is over the return button, and if it is pressed,
            (mousex, mousey) = pygame.mouse.get_pos()                                                  # goes back to the main menu
            if mousex >= 800 and mousex <= 950 and mousey >= 90 and mousey <= 150:
                returnbutton = 'RETURN BUTTON.png'    
            else:
                returnbutton = 'EMPTY.png'
            
            if event.type == MOUSEBUTTONDOWN:
                mousex, mousey = event.pos
                if mousex >= 800 and mousex <= 950 and mousey >= 90 and mousey <= 150:
                    menuscreen = True
                    howtoplayscreen = False        
            if event.type == QUIT:
                pygame.quit()
                sys.exit()  
    
    while gamescreen == True:                                                                          # this should really be where the game starts.
              
        if stinklevel == 100:                                                                          # first i draw my stink meter using this list of if statements
            stink = 'STINK METER 100%.png'                                                             # each time the stink level is increased, the meter changes accordingly. these statements
        elif stinklevel == 90:                                                                         # change the meter based on the level given by choices the user inputs!
            stink = 'STINK METER 90%.png'        
        elif stinklevel == 80:
            stink = 'STINK METER 80%.png'        
        elif stinklevel == 70:
            stink = 'STINK METER 70%.png'        
        elif stinklevel == 60:
            stink = 'STINK METER 60%.png'
        elif stinklevel == 50:
            stink = 'STINK METER 50%.png'        
        elif stinklevel == 40:
            stink = 'STINK METER 40%.png'        
        elif stinklevel == 30:
            stink = 'STINK METER 30%.png'        
        elif stinklevel == 20:
            stink = 'STINK METER 20%.png'        
        elif stinklevel == 10:
            stink = 'STINK METER 10%.png'   
        elif stinklevel == 0:
            stink = 'STINK METER 0%.png'              
        
        # u s e r   i n p u t s
        playerinput = pygame.key.get_pressed()                                                         # and now we have key presses! this variable gets what the user inputs into the game
        
        if playerinput[pygame.K_a] and mcx >= 0:                                                       # press 'a'? move left until 0 so you don't fall off the screen
            mcx -= vel                                                                                 # vel is the fixed rate stefan walks at
            hansanx = 180  # later on, stefan can interact with hand sanitizer. its 'x' is based on which way he moves          
            if (mcx >= 0 and mcx <= 100) or (mcx >= 200 and mcx <= 300) or (mcx >= 400 and mcx <= 500) or (mcx >= 600 and mcx <= 700):      # these two statements animate stefan when he walks
                mcoutfit = 'STEFAN RUN RIGHT 1.png'                                                                                         # in the future i will use clock or time to animate more
            elif (mcx >= 100 and mcx <= 200) or (mcx >= 300 and mcx <= 400) or (mcx >= 500 and mcx <= 600) or (mcx >= 700 and mcx <= 800):  # efficiently.
                mcoutfit = 'STEFAN RUN RIGHT 2.png'                
        elif playerinput[pygame.K_d] and mcx <= 800:                                                   # press 'd'? move right until your x = 800 so you don't walk off screen
            mcx += vel    
            hansanx = 140                        
            if (mcx >= 0 and mcx <= 100) or (mcx >= 200 and mcx <= 300) or (mcx >= 400 and mcx <= 500) or (mcx >= 600 and mcx <= 700):
                mcoutfit = 'STEFAN RUN LEFT 1.png'   
            elif (mcx >= 100 and mcx <= 200) or (mcx >= 300 and mcx <= 400) or (mcx >= 500 and mcx <= 600) or (mcx >= 700 and mcx <= 800):
                mcoutfit = 'STEFAN RUN LEFT 2.png'  
        elif (playerinput[pygame.K_d]) == False or (playerinput[pygame.K_a]) == False:
            hansanx = 180            
            if animation == True:                                                                      # if i need to play a cutscene, animation is made True and stefan disappears.
                mcoutfit = 'EMPTY.png'            
            elif outfit == ("clean"):
                mcoutfit = 'MAIN CHARACTER CLEAN OUTFIT.png'                                           # to make him return to his normal state after an animation, stefan's outfit is redeclared here
            elif outfit == ("dirty"):
                mcoutfit = 'MAIN CHARACTER DIRTY OUTFIT.png'
            elif clothingon == False:
                mcoutfit = 'MAIN CHARACTER PLAIN OUTFIT.png'    
        
        # r e p l a y   t h e   g a m e
        if replay == True:                                                                             # if the user chooses to replay the game, i reset all my variables here
            run = True                                                                                 # i feel like there is an easier way to code this, but i havent learned it yet
            menuscreen = True
            gamescreen = False
            howtoplayscreen = False
            intro = False
            bedroom = False
            kitchen = False
            school = False
            lunch = False
            bathroom = False
            league = False
            
            buttonStart = False
            buttonControls = False
            buttonExit = False
            
            deoapplied = False
            clothingon = False
            outfit = ("")
            animation = False
            mcx = 100
            vel = 5
            mcoutfit = 'MAIN CHARACTER PLAIN OUTFIT.png'
            message = ''
            loops = 0
            
            spaceclicked = 0
            line1 = ''
            line2 = ''
            line3 = ''
            line4 = ''
            line5 = ''
            line6 = ''
            line7 = ''
            
            dresser = 'DRESSER CLOSED.png'
            dresserx = 620
            laundry = 'LAUNDRY BIN.png'
            deodorant = 'DEODORANT.png'
            stinklevel = 20
            stink = 'STINK METER 0%.png'
            beddoor = 'EMPTY.png'
            beddooropen = 'EMPTY.png'
            
            fridge = 'FRIDGE.png'
            lunch = 'EMPTY.png'
            kitchendoor = 'EMPTY.png'
            kitchendooropen = 'EMPTY.png'
            chair = 'BREAKFAST CHAIR.png'
            breakfasteaten = False
            lunchpacked = False
            eating = False
            bellrung = False
            eat = 0
            
            tdesk = 'TEACHER SANITIZER.png'
            klimo = 'MR. K.png'
            flip = True
            desk = 'DIRTY DESK.png'
            hansan = 'EMPTY.png'
            dream = 'EMPTY.png'
            hansanx = 180
            handsan = False
            ddesk = True
            classdoor = 'EMPTY.png'
            cclassdoor = 'EMPTY.png'
            
            fhdoor = 'W202.png'
            frenchhdoor = 'EMPTY.png'
            choi = 'SUN MIN COOKIE.png'
            heeatshislunch = 'EMPTY.png'
            lunchtime = False
            luncheaten = False
            
            stalldoor = 'STALL DOOR.png'
            poop = False
            soap = 'SOAP.png'
            sink = 'SINK.png'
            washhands = False
            washing = True
            soapused = False
            hewasheshishands = 'EMPTY.png'
            handswashed = False
            secondtime = False
            
            thekitchen = False
            thebedroom = False
            goodending = False
            tablea = 'DINING TABLE.png'
            thebackground = 'KITCHEN BACKGROUND END.jpg'
            gamingstation = 'EMPTY.png'
            
            stefandead = 'STEFAN DIE UP.png'
            deathscreen = False            
            
            replaybuttoning = 'EMPTY.png'
            mainmenubuttoning = 'EMPTY.png'
            exitbuttoning = 'EMPTY.png'
            
            replay = False
            
        # h e   f a i n t s
        if stinklevel >= 100:                                                                          # when stefan reaches stink 100, he faints because he is too smelly. if the stink reaches 100
            deathscreen = True                                                                         # the game is over, so all the levels are closed off, and the end screen is triggered
            intro = False
            bedroom = False
            kitchen = False
            school = False
            lunch = False
            bathroom = False
            league = False  
            loops = 0
               
        if intro == True:                                                                              # this is my intro screen
            introScreen()
            
            if loops == 0:                                                                             # boot up background, the loops give me music and then we start
                backgroundmusic.play(pygame.mixer.Sound('bedroom music.mp3'), -1)
            
            for event in pygame.event.get():                                                           # as the user presses space, the dialogue/intro progresses with voice lines and visuals
                if playerinput[pygame.K_SPACE]:   
                    spaceclicked += 1
                    if spaceclicked == 1:
                        line1 = 'Your name is Stinky Stefan.'
                        voicelines.play(pygame.mixer.Sound('stinkystefan.mp3'))                        
                    if spaceclicked == 2:
                        line2 = 'You have trouble staying clean throughout the day.'
                        voicelines.play(pygame.mixer.Sound('clean.mp3'))                        
                    if spaceclicked == 3:
                        line3 = 'But today will be different.'
                        voicelines.play(pygame.mixer.Sound('diff.mp3'))                        
                    if spaceclicked == 4:
                        line4 = 'Today you will make it through the day without'
                        line5 = 'passing out from your own stench.'
                        voicelines.play(pygame.mixer.Sound('stench.mp3'))                        
                    if spaceclicked == 5:
                        line6 = 'Good luck Stefan! Do not get too stinky'
                        voicelines.play(pygame.mixer.Sound('toostink.mp3'))                        
                    if spaceclicked == 6:
                        line7 = 'Press SPACE to start playing'
                        
                    if spaceclicked == 7:                                                              # once it is over, the game goes into the bedroom, resetting loops to repeat the first step
                        intro = False
                        bedroom = True
                        loops = 0
                        
        # -------------------------------- L E V E L   O N E   ||   B E D R O O M --------------------------------------------------------------------------
        
        if bedroom == True:
            bedroomScreen()
            
            if loops == 0:                                                                             # background, music and this time a cut scene
                voicelines.play(pygame.mixer.Sound('good_morning.mp3'))                                # stefan speaks 
                
                stefanmessage = pygame.image.load('SPEECH BUBBLE.png')                                 # a speech bubble is blitted to the screen
                screen.blit(stefanmessage, (mcx + 200, 50))        
                
                message = 'I need to put on clothes.'                                                  # the screen writes in the bubble
                
                font = pygame.font.Font('fixedsys.ttf', 15)
                text = font.render(message, False, BLACK)
                screen.blit(text, (mcx + 245, 200))    
                
                pygame.display.flip()                                                                  # the display is paused and flipped to update the cut scene
                pygame.time.delay(3500)
            
            for event in pygame.event.get():                                                           # now my if statements checks if he is over his laundry bin or his wardrobe
                if clothingon == False:                                                                # highlights it, and then changes his outfit if the user presses 'e'
                    if mcx >= 410 and mcx <= 883:
                        dresser = 'DRESSER OPEN.png'
                        dresserx = 580
                        if playerinput[pygame.K_e]:
                            soundeffects.play(pygame.mixer.Sound('changing.mp3'))                                                
                            outfit = ("clean")
                            mcoutfit = 'MAIN CHARACTER CLEAN OUTFIT.png'       
                            stinklevel -= 10
                            clothingon = True
                            dresser = 'DRESSER CLOSED.png'                
                            dresserx = 620                         
                    else:
                        dresser = 'DRESSER CLOSED.png'                
                        dresserx = 620 
                        
                    if mcx >= 140 and mcx <= 400:
                        laundry = 'LAUNDRY BIN SELECT.png'
                        if playerinput[pygame.K_e]:
                            soundeffects.play(pygame.mixer.Sound('changing.mp3'))                                                                            
                            outfit = ("dirty")                        
                            mcoutfit = 'MAIN CHARACTER DIRTY OUTFIT.png'
                            stinklevel += 10
                            clothingon = True    
                            laundry = 'LAUNDRY BIN.png'
                    else:
                        laundry = 'LAUNDRY BIN.png'
                    
                if deoapplied == False:                                                                # he also has a stick of deodorant. same mechanics as the clothes
                    if mcx >= -50 and mcx <= 50:
                        deodorant = 'DEODORANT SELECT.png'
                        if playerinput[pygame.K_e]:
                            deodorant = 'EMPTY.png'
                            stinklevel -= 10
                            deoapplied = True
                    else:
                            deodorant = 'DEODORANT.png'
                    
                if clothingon == True:                                                                 # once he is dressed, he can leave his room and proceed to the next level via a door
                    beddoor = 'BEDROOM DOOR.png'                                                       # that appears on the screen
                    if mcx >= 730 and mcx <= 900:
                        beddooropen = 'BEDROOM DOOR OPEN.png'
                        beddoor = 'BEDROOM DOOR BEHIND.png'                        
                        if playerinput[pygame.K_e]: 
                            bedroom = False
                            kitchen = True
                            mcx = 0
                            loops = 0
                    else:
                        beddoor = 'BEDROOM DOOR.png'
                        beddooropen = 'EMPTY.png'
                        
        # -------------------------------- L E V E L   T W O   ||   K I T C H E N --------------------------------------------------------------------------

        if kitchen == True:                                                                            # just like before, boot up background for kitchen, switch music and cut scene
            kitchenScreen()
                            
            if loops == 0:
                if deoapplied == False:                                                                # also, every level, your stink goes up. just like in real life, you gain stink throughout the
                    stinklevel += 20                                                                   # day passively. if he put on deodorant, it is reduced, otherwise, it goes up a ton
                elif deoapplied == True:
                    stinklevel += 10
                    
                voicelines.play(pygame.mixer.Sound('Get_breakfast.mp3'))
                
                backgroundmusic.play(pygame.mixer.Sound('kitchen music.mp3'), -1)                
                stefanmessage = pygame.image.load('SPEECH BUBBLE.png')
                screen.blit(stefanmessage, (mcx + 200, 50))        
                
                message = 'I need to eat breakfast.'
                
                font = pygame.font.Font('fixedsys.ttf', 15)
                text = font.render(message, False, BLACK)
                screen.blit(text, (mcx + 245, 200))    
                
                pygame.display.flip()                   
                pygame.time.delay(2500)            
            
            if breakfasteaten == True and loops == 1:                                                  # this time i have 2 dialogue scenes. the first one (above) plays if he hasn't eaten yet
                voicelines.play(pygame.mixer.Sound('father_sladjan.mp3'))                              # this one plays after he has eaten breakfast and he needs his lunch
                
                stefanmessage = pygame.image.load('SPEECH BUBBLE.png')
                screen.blit(stefanmessage, (mcx + 200, 50))        
                
                message = 'I need to pack my lunch.'
                
                font = pygame.font.Font('fixedsys.ttf', 15)
                text = font.render(message, False, BLACK)
                screen.blit(text, (mcx + 245, 200))    
                
                pygame.display.flip()                   
                pygame.time.delay(3500)   
            
            if eating == True:                                                                         # this is an animation for while he is eating. it is the same as the one for lunch
                if eat == 0:                                                                           # first, each eat if statement changes his photo
                    chair = 'STEFAN BREAKFAST 1.png'
                elif eat == 1:
                    chair = 'STEFAN BREAKFAST 2.png'
                    soundeffects.play(pygame.mixer.Sound('nomnom.mp3'))                                # then his eating noises start to play
                elif eat == 2:
                    chair = 'STEFAN BREAKFAST 3.png'
                elif eat == 3:
                    chair = 'STEFAN EMPTY PLATE.png'
                elif eat == 4:                                                                         # once he is done eating, it returns the kitchen to normal and turns off the animation
                    animation = False
                    chair = 'KITCHEN CHAIR.png'
                    lunchpacked = False
                    loops = 0
                    mcx = 380
                    eating = False
                chairart = pygame.image.load(chair)                                                    # and each eat count pauses the screen, and updates the chair art to show him eating his food!
                screen.blit(chairart, (550, 262))                
                eat += 1  
                pygame.display.flip()
                pygame.time.delay(1500)                  
                
            for event in pygame.event.get():                                                           # finally, all my if statements check where he is, and if he needs to interact with the 
                if breakfasteaten != True:                                                             # environement or not!
                    if mcx >= 390 and mcx <= 575:
                        chair = 'BREAKFAST CHAIR SELECTED.png'
                        if playerinput[pygame.K_e]: 
                            eating = True
                            animation = True
                            breakfasteaten = True
                    else:
                        chair = 'BREAKFAST CHAIR.png'
                                                                                  
                if breakfasteaten == True and lunchpacked == False:                                    # this opens the fridge when he is ready to pack his lunch
                    if mcx >= 80 and mcx <= 270:
                        fridge = 'OPEN FRIDGE.png'
                        lunch = 'LUNCH.png'                        
                        if playerinput[pygame.K_e]: 
                            lunch = 'EMPTY.png'
                            lunchpacked = True
                            fridge = 'FRIDGE.png'  
                            soundeffects.play(pygame.mixer.Sound('fridge.mp3'))     
                            voicelines.play(pygame.mixer.Sound('go_to_school.mp3'))                                                
                    else:
                        fridge = 'FRIDGE.png'
                        lunch = 'EMPTY.png'
                if lunchpacked == True:
                    if mcx >= 555 and mcx <= 790:
                        kitchendoor = 'KITCHEN DOOR BEHIND.png' 
                        kitchendooropen = 'KITCHEN DOOR OPEN.png'                      
                        if playerinput[pygame.K_e]: 
                            kitchen = False                                                            # just like the bedroom, once the kitchen needs are fulfilled, door pops up and he goes to school
                            school = True
                            mcx = 800
                            loops = 0
                    else:
                        kitchendoor = 'KITCHEN DOOR.png'
                        kitchendooropen = 'EMPTY.png'                        
        
        # -------------------------------- L E V E L   T H R E E   ||   S C H O O L --------------------------------------------------------------------------

        if school == True:                                                                             # school level, same old same old. going forward i wont reiterate things ive already defined
            classroomScreen()

            if (loops%200) == 0:                                                                       # in order to animate yourself, i did it so that everytime 200 loops have passed
                if flip == True:                                                                       # a variable is toggled. if 'flip' is 'True', then you are normal
                    klimo = 'MR. K.png'                                                                # when 'flip' is 'False', you flip. neat little animation
                    flip = False
                else:
                    klimo = 'MR. K(1).png'
                    flip = True
                    
            if loops == 0:
                
                backgroundmusic.play(pygame.mixer.Sound('classroom music.mp3'))                
                voicelines.play(pygame.mixer.Sound('desk_dirty.mp3'))                                                                
                
                if deoapplied == False:
                    stinklevel += 20
                elif deoapplied == True:
                    stinklevel += 10  
                    
                stefanmessage = pygame.image.load('SPEECH BUBBLE FLIP.png')
                screen.blit(stefanmessage, (mcx - 250, 50))        
                
                message = 'My desk is dirty.'
                
                font = pygame.font.Font('fixedsys.ttf', 15)
                text = font.render(message, False, BLACK)
                screen.blit(text, (mcx - 170, 200))    
                
                pygame.display.flip()                   
                pygame.time.delay(2500)     

            if bellrung == True:                                                                       # this is stefans animation for when he falls asleep in your class
                if loops == 1:
                    voicelines.play(pygame.mixer.Sound('dozing off.mp3'))                              # it plays a special voice line
                    dream = 'DREAMLAND.jpg'                                                            # and edits the background while it happens         
                if loops == 2:
                    pygame.display.flip()                   
                    pygame.time.delay(8500)  
                if loops == 3:
                    dream = 'EMPTY.png'
                    mcx = 100
                    soundeffects.play(pygame.mixer.Sound('thebell.mp3'))                               # once it is over, the bell rings and stefan is free to move again
                    classdoor = 'CLASSROOM DOOR.png'
            
            for event in pygame.event.get():                                                           # some checking where stefan is and if he needs to interact
                if handsan == False:                                                                   # checks if he has the hand sanitizer, if not, he can pick it up to clean his desk
                    if mcx >= 350 and mcx <= 540:
                        tdesk = 'SANITIZER SELECT.png'                     
                        if playerinput[pygame.K_e]: 
                            tdesk = 'TDESK.png'
                            hansan = 'SANITIZER.png'
                            handsan = True
                    else:
                        tdesk = 'TEACHER SANITIZER.png'
                        hansan = 'EMPTY.png'
                        
                if mcx >= -5 and mcx <= 320:
                    if bellrung == False:
                        if ddesk == True:                                                       
                            desk = 'DIRTY DESK HIGHLIGHT.png'
                            if playerinput[pygame.K_e]:                                                # if stefan doesnt pick up the hand san, he can sit at the dirty desk
                                if handsan == False:                                                   # this increases his stink level however
                                    animation = True
                                    desk = 'STEFAN SITS DIRTY.png'
                                    stinklevel += 10
                                    loops = 0
                                    bellrung = True
                                elif handsan == True:                                                  # if his desk is still dirty, and he picked up the hand sanitizer, he can use it on the desk 
                                    hansan = 'EMPTY.png'
                                    tdesk = 'TDESK.png'
                                    desk = 'DESK.png'
                                    ddesk = False
                            else:
                                animation = False                                
                        else:
                            desk = 'DESK HIGHLIGHT.png'
                            if playerinput[pygame.K_e]:                                                # once the desk is clean, he can sit at it and it will reduce his stink level
                                bellrung = True                                
                                animation = True
                                desk = 'STEFAN SITS.png'
                                loops = 0
                                stinklevel -= 10
                            else:
                                animation = False                         
                                
                    else:
                        desk = 'DIRTY DESK.png'
                
                if bellrung == True and loops > 1:                                                     # once the bell has been rung, he returns to class
                    tdesk = 'TDESK.png'
                    animation = False                    
                    if ddesk == True:
                        desk = 'DIRTY DESK.png'
                    elif ddesk == False:
                        desk = 'DESK.png'
                        
                    if mcx >= 730 and mcx <= 1000:                                                     # a door appears and he may walk over and leave the class when he is ready to go to lunch
                        classdoor = 'CLASSROOM DOOR BLACK.png' 
                        cclassdoor = 'CLASSROOM DOOR OPEN.png'                      
                        if playerinput[pygame.K_e]: 
                            school = False
                            lunch = True
                            mcx = 0
                            loops = 0
                    else:
                        classdoor = 'CLASSROOM DOOR.png'
                        cclassdoor = 'EMPTY.png'      
                        
        # -------------------------------- L E V E L   F O U R   ||   L U N C H --------------------------------------------------------------------------

        if lunch == True:
            frencHall()
            
            if loops == 0:
                
                backgroundmusic.play(pygame.mixer.Sound('french hall music.mp3'))                
                voicelines.play(pygame.mixer.Sound('stefan have lunch.mp3'))                           # sun min asks stefan to eat lunch with her (his gf)
                
                if deoapplied == False:
                    stinklevel += 20
                elif deoapplied == True:
                    stinklevel += 10  
            
            if luncheaten == False and lunchtime == True:                                              # here is my stefan eating animation, same as breakfast
                animation = True
                if eat == 0:
                    heeatshislunch = 'STEFAN LUNCH 1.png'
                elif eat == 1:
                    heeatshislunch = 'STEFAN LUNCH 2.png'
                    voicelines.play(pygame.mixer.Sound('he a hungry boy.mp3'))                                               
                    soundeffects.play(pygame.mixer.Sound('nomnom.mp3'))                    
                elif eat == 2:
                    heeatshislunch = 'STEFAN LUNCH 3.png'
                elif eat == 3:
                    heeatshislunch = 'STEFAN LUNCH EMPTY.png'
                elif eat == 4:
                    animation = False
                    heeatshislunch = 'EMPTY.png'
                    luncheaten = True
                    loops = 0
                    mcx = 100
                eat += 1  
                pygame.display.flip()
                pygame.time.delay(1500)  
                
            if luncheaten == True and loops == 1:                                                      # once stefan finishes his lunch, he needs to go to bathroom
                                                                                                       # this is where he states that
                voicelines.play(pygame.mixer.Sound('ate_too_much.mp3'))                                                                
                    
                stefanmessage = pygame.image.load('SPEECH BUBBLE.png')
                screen.blit(stefanmessage, (mcx + 200, 50))        
                
                message = 'I need bathroom now.'
                
                font = pygame.font.Font('fixedsys.ttf', 15)
                text = font.render(message, False, BLACK)
                screen.blit(text, (mcx + 245, 200))    
                
                pygame.display.flip()                   
                pygame.time.delay(4500)                     
                    
            for event in pygame.event.get():
                if lunchtime == False:
                    if mcx >= 175 and mcx <= 420:
                        choi = 'COOKIE MIN I CHOOSE YOU.png'                                           # if stefan still needs to eat, he can walk over to sun min to trigger the animation with 'e'
                        if playerinput[pygame.K_e]: 
                            lunchtime = True
                            choi = 'SUN MIN COOKIE.png'                            
                            loops = 0  
                            eat = 0
                            mcx = 100
                    else:
                        choi = 'SUN MIN COOKIE.png'
                if luncheaten == True:
                    if mcx >= 560 and mcx <= 740:                                                      # after lunch, stefan can go straight home
                        fhdoor = 'W202 BEHIND.png'
                        frenchhdoor = 'W202 OPEN.png'
                        if playerinput[pygame.K_e]:     
                                league = True
                                thekitchen = True
                                mcx = 600
                                lunch = False
                                loops = 0
                    elif playerinput[pygame.K_d] and mcx >= 780 and secondtime == False:               # or he can walk off the screen and go to the bathroom following the 'toilettes' sign
                            bathroom = True
                            lunch = False
                            mcx = 0
                            loops = 0
                    else:
                        fhdoor = 'W202.png'
                        frenchhdoor = 'EMPTY.png'
                        
        # -------------------------------- B O N U S    L E V E L  ||   B A T H R O O M --------------------------------------------------------------------------

        if bathroom == True:
            lesToilettes()
            
            if loops == 0:
                
                backgroundmusic.play(pygame.mixer.Sound('bathroom music.mp3'))                
                
                if deoapplied == False:
                    stinklevel += 20
                elif deoapplied == True:
                    stinklevel += 10              
            
            elif poop == True and loops == 1:                                                          # this is my stefan in the stall sound. it just pauses, then flushes, then opens the stall door
                    stalldoor = 'STALL DOOR.png'  
                    pygame.display.flip()                                       
                    pygame.time.delay(500)                      
                    soundeffects.play(pygame.mixer.Sound('toilet noises.mp3'))     
                    pygame.time.delay(7500)  
                    stalldoor = 'STALL DOOR OPEN.png'
                    pygame.display.flip()                                       
            
            elif washhands == True and handswashed == False:                                           # if stefan walks over to the sink and use it, a wash hand animation will play with sound
                animation = True
                if washing == True:
                    hewasheshishands = 'STEFAN WASHING HANDS.png'
                    soundeffects.play(pygame.mixer.Sound('wash hands.mp3'))
                    washing = False
                elif washing == False:
                    pygame.time.delay(5500)
                    animation = False  
                    handswashed == True
                    if soapused == True:
                        stinklevel -= 20                                                               # if he uses soap, his stink is lowered much more
                    elif soapused == False:
                        stinklevel -= 10                                                               # if he doesnt use soap, his stink is lowered, just not as much
                    hewasheshishands = 'EMPTY.png'
                    handswashed = True
                    sink = 'SINK.png'
                
            for event in pygame.event.get():
                if poop == False:                                                                      # stefan just needs to walk into the stall to use the toilet and load the animation
                    if mcx >= 300 and mcx <= 460:
                        stalldoor = 'STALL DOOR OPEN.png'                            
                    else:
                        stalldoor = 'STALL DOOR.png'
                        
                    if mcx >= 600:
                        poop = True
                        loops = 0  
                        
                if poop == True:
                    if washhands == False:
                        if mcx >= 10 and mcx <= 170:                                                   # this is where he interacts with the sink to wash his hands. he doesn't need to wash them tho
                            sink = 'SINK SELECT.png'
                            if playerinput[pygame.K_e]:
                                sink = 'SINK WET.png'
                                washhands = True
                        else:
                            sink = 'SINK.png'
                    
                    if soapused == False:
                        if mcx >= 190 and mcx <= 290:                                                  # this is where stefan can use soap if he wants to
                            soap = 'SOAP SELECT.png'
                            if playerinput[pygame.K_e]:  
                                soapused = True
                                soap = 'SOAP.png'
                        else:
                            soap = 'SOAP.png'
                    
                    if mcx <= 0 and playerinput[pygame.K_a]:
                        if washhands == False:                                                         # if stefan doesn't wash his hands, his stink increases
                            stinklevel += 20                                                           # this is where he walks off the screen to return to french hall
                        bathroom = False
                        mcx = 740
                        lunch = True       
                        choi = 'EMPTY.png'
                        secondtime = True                                                              # once he walks back, he cannot walk off, he must just walk home
                        
        # -------------------------------- L E V E L   F I V E   ||   R E T U R N --------------------------------------------------------------------------
        
        if league == True:
            homeStretch()
            
            if loops == 0:
                if deoapplied == False:
                    stinklevel += 20
                elif deoapplied == True:
                    stinklevel += 10                 
    
                if poop == False:                                                                      # if stefan chose to not go to the bathroom at school, he poops his pants and stink go up
                    voicelines.play(pygame.mixer.Sound('pooped_pants.mp3'))       
                    soundeffects.play(pygame.mixer.Sound('poopy stink.mp3'))   
                    stinklevel += 50          
                    pygame.time.delay(2500)
                
                backgroundmusic.play(pygame.mixer.Sound('ITS THE END FINALLY.mp3'))      
                voicelines.play(pygame.mixer.Sound('time_to_play_league.mp3'))    
                pygame.time.delay(1500)
            
            for event in pygame.event.get():
                if thekitchen == True:                                                                 # stefan is to run back to his room, and once he leaves the kitchen
                    if mcx <= 0:                                                                       # the background changes and he is back in his room
                        thekitchen = False
                        thebedroom = True
                        loops = 0
                        mcx = 740
                        tablea = 'EMPTY.png'
                        chair = 'EMPTY.png'
                        thebackground = 'BEDROOM BACKGROUND END.jpg'    
                        gamingstation = 'GAMING DESK.png'
                if thebedroom == True:                                                                 # when he is in his room, he goes to his computer and boots up league! he made it!
                    if goodending == False:
                        if mcx >= 210 and mcx <= 490:                    
                            gamingstation = 'GAMING DESK SELECTED.png'
                            if playerinput[pygame.K_e]:
                                gamingstation = 'BOOTING UP LEAGUE.png'
                                goodending = True
                                league = False
                                pygame.time.delay(1500)
                                soundeffects.play(pygame.mixer.Sound('winnered.mp3'))  
                                voicelines.play(pygame.mixer.Sound('man i love richard.mp3'))                                                
                                
                        else:
                            gamingstation = 'GAMING DESK.png'
                            
        # -------------------------------- G O O D   E N D I N G --------------------------------------------------------------------------

        if goodending == True:
            itslikeitsWinnersqueue()
            
            for event in pygame.event.get():                                                           # the good ending is like the main menu, it has a few buttons formatted the same way
                (mousex, mousey) = pygame.mouse.get_pos()
                if mousex >= 620 and mousex <= 855 and mousey >= 75 and mousey <= 130:                 # play again button
                    replaybuttoning = 'PLAY AGAIN BUTTON.png'
                else:
                    replaybuttoning = 'EMPTY.png'
                if mousex >= 610 and mousex <= 860 and mousey >= 170 and mousey <= 220:                # main menu button
                    mainmenubuttoning = 'MAIN MENU BUTTON.png'
                else:
                    mainmenubuttoning = 'EMPTY.png'
                if mousex >= 615 and mousex <= 870 and mousey >= 270 and mousey <= 330:                # exit button
                    exitbuttoning = 'EXITING BUTTON.png'
                else:
                    exitbuttoning = 'EMPTY.png'
        
                if event.type == MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    if mousex >= 620 and mousex <= 855 and mousey >= 75 and mousey <= 130:             # main menu button resets the game, and sends back to main menu
                        gamescreen = True
                        goodending = False                          
                        intro = True
                        loops = 0
                        replay = True
                        animation = False 
                    if mousex >= 610 and mousex <= 860 and mousey >= 170 and mousey <= 220:            # replay button resets the game but sends you back to the intro
                        menuscreen = True
                        gamescreen = False                        
                        goodending = False 
                        replay = True
                        animation = False                       
                    if mousex >= 615 and mousex <= 870 and mousey >= 270 and mousey <= 330:            # quits the game
                        goodending = False
                        pygame.quit()
                        sys.exit()   
                        
        # -------------------------------- B A D   E N D I N G --------------------------------------------------------------------------
                
        if deathscreen == True:
            danteslosttheRace()                                                                        # just like the notes above with an animation
            
            if loops == 0:
                animation = True 
                stinklevel = 20                
                backgroundmusic.play(pygame.mixer.Sound('its like were almost done.mp3'))                                

                pygame.display.flip
                pygame.time.delay(2500)                    
            elif loops == 1:      
                stefandead = 'STEFAN DIE DOWN 1.png'                                                   # stefan is placed on the screen now with crossed out eyes
                
                stefandeadart = pygame.image.load(stefandead)
                screen.blit(stefandeadart, (mcx, 230))                    
                
                pygame.display.flip
                pygame.time.delay(2500)   
            
            
            if loops > 2 and (loops%50) == 0:                                                          # then he flops over, and using the same mechanics i used for you, he animates with flies 
                if flip == True:
                    stefandead = 'STEFAN DIE DOWN 1.png'
                    flip = False
                else:
                    stefandead = 'STEFAN DIE DOWN 2.png'
                    flip = True
            
            
            for event in pygame.event.get():
                (mousex, mousey) = pygame.mouse.get_pos()
                if mousex >= 620 and mousex <= 855 and mousey >= 75 and mousey <= 130:
                    replaybuttoning = 'PLAY AGAIN BUTTON.png'
                else:
                    replaybuttoning = 'EMPTY.png'
                if mousex >= 610 and mousex <= 860 and mousey >= 170 and mousey <= 220:
                    mainmenubuttoning = 'MAIN MENU BUTTON.png'
                else:
                    mainmenubuttoning = 'EMPTY.png'
                if mousex >= 615 and mousex <= 870 and mousey >= 270 and mousey <= 330:
                    exitbuttoning = 'EXITING BUTTON.png'
                else:
                    exitbuttoning = 'EMPTY.png'
        
                if event.type == MOUSEBUTTONDOWN:
                    mousex, mousey = event.pos
                    if mousex >= 620 and mousex <= 855 and mousey >= 75 and mousey <= 130:
                        gamescreen = True
                        goodending = False                          
                        intro = True
                        loops = 0
                        replay = True
                        animation = False
                    if mousex >= 610 and mousex <= 860 and mousey >= 170 and mousey <= 220:
                        menuscreen = True
                        gamescreen = False                        
                        goodending = False  
                        replay = True
                        animation = False                        
                    if mousex >= 615 and mousex <= 870 and mousey >= 270 and mousey <= 330:
                        goodending = False
                        pygame.quit()
                        sys.exit()      
            
        loops += 1                                                                                     # this is where loops is added every round
        
        if event.type == QUIT:                                                                         # and an if they click 'x', the game ends smoothly
            pygame.quit()
            sys.exit()    

# and we are done! i hope you enjoyed the game, and my comments along the way. i hope it wasn't too messy and maybe... just maybe... you give me 100% ?