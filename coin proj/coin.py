import pgzrun
import tkinter as tk
#it is important to insert import pygame at the start or the fullscreen function won't work
import pygame





pygame.init()
pygame.display.set_caption("Catch the egg")
icon = pygame.image.load('bird.png')
pygame.display.set_icon(icon)
#Inditcates who the actors are and where they should be placedel
from random import randint
WIDTH = 800
HEIGHT = 604
score = 0
game_over = False
egg= Actor("egg")
egg.pos = 200, 200
bird = Actor("bird")
bird.pos = 100, 100
house = Actor("house")
house.pos = 100, 800
#--------------------------------


def draw():
    #(The first 2 lines are for screen resizeability)
    pygame.init()
    DISPLAYSURF = pygame.display.set_mode((800, 600),pygame.RESIZABLE)

    screen.clear()
    screen.blit("sky", (0, 0))
    egg.draw()
    bird.draw()
    house.draw()
    screen.draw.text("Score: " + str(score), color="white", topleft=(10, 10))

#contains what happens if the game is over/timer is finished
    if game_over:
        screen.fill("black")
        screen.draw.text("This is your final score: " + str(score), topleft=(10, 10), fontsize=60)
    pass
#-----------------------------------------------------------------------------------------------------

#Everything below is dedicated to the level system. The goal for the amount of level is adleast 30
#contains 28 Levels
    if (score > 10):
        screen.draw.text("Level 1 " + str(score), topleft=(10, 30))
    pass

    if (score > 30):
        screen.draw.text("Level 2 " +str(score), topleft=(10,50))
    pass

    if (score > 50):
        screen.draw.text("Level 3 " + str(score), topleft=(10,70))
    pass

    if (score > 70):
        screen.draw.text("Level 4 " + str(score), topleft=(10,90))
    pass

    if (score > 90):
        screen.draw.text("Level 5 " + str(score), topleft=(10,110))
    pass

    if (score > 110):
        screen.draw.text("Level 6 " + str(score), topleft=(10, 130))
    pass

    if (score > 130):
        screen.draw.text("Level 7 " + str(score), topleft=(10, 150))
    pass

    if (score > 150):
        screen.draw.text("Level 8 " + str(score), topleft=(10, 170))
    pass

    if (score > 170):
        screen.draw.text("Level 9 " + str(score), topleft=(10, 190))
    pass

    if (score > 190):
        screen.draw.text("Level 10 " + str(score), topleft=(10, 210))
    pass

    if (score > 210):
        screen.draw.text("Level 11 " + str(score), topleft=(10, 230))
    pass

    if (score > 230):
        screen.draw.text("Level 12 " + str(score), topleft=(10, 250))
    pass

    if (score > 250):
        screen.draw.text("Level 13 " +str(score), topleft=(10, 270))
    pass

    if (score > 270):
        screen.draw.text("Level 14 " + str(score), topleft=(10, 290))
    pass

    if (score > 290):
        screen.draw.text("Level 15 " + str(score), topleft=(10, 310))
    pass

    if (score > 310):
        screen.draw.text("Level 16 " + str(score), topleft=(10, 330))
    pass

    if (score > 330):
        screen.draw.text("Level 17 " + str(score), topleft=(10, 350))
    pass

    if (score > 350):
        screen.draw.text("Level 18 " + str(score), topleft=(10, 370))
    pass

    if (score > 370):
        screen.draw.text("Level 19 " + str(score), topleft=(10, 390))
    pass

    if (score > 390):
        screen.draw.text("Level 20 " + str(score), topleft=(10, 410))
    pass

    if (score > 410):
        screen.draw.text("Level 21 " + str(score), topleft=(10, 430))
    pass

    if (score > 430):
        screen.draw.text("Level 22 " + str(score), topleft=(10, 450))
    pass

    if (score > 450):
        screen.draw.text("Level 23 " + str(score), topleft=(10, 470))
    pass

    if (score > 470):
        screen.draw.text("Level 24 " + str(score), topleft=(10, 490))
    pass

    if (score > 490):
        screen.draw.text("Level 25 " + str(score), topleft=(10, 510))
    pass

    if (score > 510):
        screen.draw.text("Level 26 " + str(score), topleft=(10, 530))
    pass

    if (score > 530):
        screen.draw.text("Level 27 " + str(score), topleft=(10, 550))
    pass

    if (score > 550):
        screen.draw.text("Level 28 Final Level" + str(score), topleft=(10, 570))
    pass
#----------------------------------------------------------------------------------------------


music.play("temperatures-rising")


#Egg's placement coordinates
def place_egg():
    egg.x = randint(20, (WIDTH - 20))
    egg.y = randint(20, (HEIGHT - 20))
    pass
#---------------------------------------------

# connected to the time function in def update():
#Acts as a time function for the game
def time_up():
    global game_over
    game_over = True
    pass
#-----------------------------------------

#contains movement controls for the bird
#contains score wheel
#contains a timer which is connected to def time_up():
#contains what happens if the bird collected its egg
def update():
    global score

    if keyboard.left:
        bird.x = bird.x - 4
    elif keyboard.right:
        bird.x = bird.x + 4
    elif keyboard.up:
        bird.y = bird.y - 4
    elif keyboard.down:
        bird.y = bird.y + 4

        egg_found = bird.colliderect(egg)
        if egg_found:
            score = score + 10
            clock.schedule(time_up, 100.0)
            place_egg()
#--------------------------------------------------

pgzrun.go()
