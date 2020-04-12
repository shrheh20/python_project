import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0,0,0)
white = (255,255,255)
red = (255,0,0)

block_color = (53,115,255)

car_width = 58

screen = pygame.display.set_mode((display_width,display_height))
pygame.display.set_caption('Fast:10 Your Seatbelts')
clock = pygame.time.Clock()

#car image
carImg = pygame.image.load('car1.jpg')
carImg = pygame.transform.scale(carImg,(car_width,91))
posX=370
posY=480
#background image
backgroundImg= pygame.image.load('python road.png')


def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: "+str(count), True, white)
    screen.blit(text,(0,0))

def things(thingx, thingy, thingr,color):
    pygame.draw.circle(screen, color, [thingx, thingy], thingr)

def car(x,y):
    screen.blit(carImg,(x,y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width/2),(display_height/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(2)

    game_loop()
    
    

        
def crash():
    message_display('You Crashed')
    
def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)

    x_change = 0

    thing_startx = random.randrange(158,700)
    thing_starty = -600
    thing_speed = 4
    thing_radius = 40
    
    thingCount = 1

    dodged = 0

    gameExit = False

    while not gameExit:
        screen.blit(backgroundImg,(0,0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        if x <= 158:
            x = 158
        elif x >= 600:
            x = 600
            
        # things(thingx, thingy, thingr, color)
        things(thing_startx, thing_starty, thing_radius, block_color)


        
        thing_starty += thing_speed
        car(x,y)
        things_dodged(dodged)

        if x > display_width - car_width or x < 0:
            crash()

        if thing_starty > display_height:
            thing_starty = 0 - thing_radius
            thing_startx = random.randrange(0,display_width)
            dodged += 1
            thing_speed += 1
            thing_radius += dodged

        if y < thing_starty+thing_radius:
            print('y crossover')

            if x > thing_startx and x < thing_startx + thing_radius or x+car_width > thing_startx and x + car_width < thing_startx+thing_radius:
                print('x crossover')
                crash()
        
        pygame.display.update()
        clock.tick(60)

game_loop()
pygame.quit()
quit()
