import pygame
import time
import random

pygame.init()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (200, 0, 0)
bright_red = (255, 0, 0)
blue = (0, 0, 200)
green = (0, 200, 0)
bright_green = (0, 255, 0)
grey = (128, 128, 128)

carImg = pygame.image.load('images/racecar.png')
car_width = 73
car_height = 82

road_width = 500

high_score = 0
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Car gameeee')
clock = pygame.time.Clock()

def things_dodged(count):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Dodged: " + str(count), True, black)
    gameDisplay.blit(text, (0, 0))
    text = font.render("High Score: " + str(high_score), True, blue)
    gameDisplay.blit(text, (0, 20))

def things(thingx, thingy, thingw, thingh, color):
    pygame.draw.rect(gameDisplay, color, [thingx, thingy, thingw, thingh])

def car(x, y):
    gameDisplay.blit(carImg, (x, y))

def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text, x, y):
    largeText = pygame.font.Font('freesansbold.ttf', 80)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = (x, y)
    gameDisplay.blit(TextSurf, TextRect)

    pygame.display.update()


def crash(count, max_score):
    message_display("You Crashed", display_width / 2, display_height / 2 - 80)
    message_display("Your Score : " + str(count), display_width / 2, display_height / 2)
    message_display("High Score : " + str(max_score), display_width / 2, display_height / 2 + 80)
    
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)
        button("Play Again",150,450,150,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)



def button(msg, x, y, w, h, inactive_color, active_color, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+w > mouse[1] > y:
        pygame.draw.rect(gameDisplay, active_color, (x,y,w,h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, inactive_color, (x,y,w,h))
        
    smallText = pygame.font.Font("freesansbold.ttf",20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ( ( x + ( w / 2 )), ( y + ( h / 2 )) )
    gameDisplay.blit(textSurf, textRect)

def quitgame():
    pygame.quit()
    quit()

pause=False

def paused():
    
    global pause
    pause = True
    largeText = pygame.font.Font("freesansbold.ttf",115)
    textSurf, textRect = text_objects("Paused", largeText)
    textRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(textSurf, textRect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        #gameDisplay.fill(white)
        button("Conitnue!",150,450,100,50,green,bright_green,unpause)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)

def unpause():
    global pause
    pause = False

def game_intro():
    intro = True

    pause = False
    while intro:
        for event in pygame.event.get():
            #print(event)
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        largeText = pygame.font.Font('freesansbold.ttf',75)
        TextSurf, TextRect = text_objects("The Getaway Car", largeText)
        TextRect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(TextSurf, TextRect)
        
        button("GO!",150,450,100,50,green,bright_green,game_loop)
        button("Quit",550,450,100,50,red,bright_red,quitgame)
        pygame.display.update()
        clock.tick(15)


def game_loop():
    gameExit = False
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    delta_x = 0
    #delta_y = 0

    cop_car_x = random.randrange(0, display_width)
    cop_car_y = -600
    cop_car_speed = 4
    cop_car_width = 60
    cop_car_height = 80
    cop_car_count = 1

    scale_factor = 0.1

    road_boundary_left_x = []
    road_boundary_y = []
    road_boundary_width = 10
    road_boundary_height = 60
    road_boundary_blocks = int(display_width / road_boundary_height)
    dodged = 0
    road_boundary_left_x = [100 for i in range(road_boundary_blocks)]
    road_boundary_y = [i * road_boundary_height for i in range(road_boundary_blocks)]

    global high_score

    while not gameExit:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    delta_x = -5
                if event.key == pygame.K_RIGHT:
                    delta_x = 5

                if event.key == pygame.K_UP:
                    delta_y = -5
                if event.key == pygame.K_DOWN:
                    delta_y = 5
                
                if event.key == pygame.K_p:
                    paused()

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    delta_x = 0
                #if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    #delta_y = 0

        x += delta_x
        #y += delta_y
        gameDisplay.fill(white)

        things(cop_car_x, cop_car_y, cop_car_width, cop_car_height, red)
        things(cop_car_x, cop_car_y + int(cop_car_height/3), cop_car_width, int(cop_car_height/3), blue)
        cop_car_y += int(cop_car_speed)

        car(x, y)
        things_dodged(dodged)

        crash_flag = False
        for i in range(road_boundary_blocks):
            things(road_boundary_left_x[i], road_boundary_y[i], road_boundary_width, road_boundary_height, black)
            things(road_boundary_left_x[i] + road_width, road_boundary_y[i], road_boundary_width, road_boundary_height, black)
            if y < road_boundary_y[i] + road_boundary_height and y + car_height > road_boundary_y[i]:
                if (x > road_boundary_left_x[i] and x < road_boundary_left_x[i] + road_boundary_width) or \
                    (x + car_width > road_boundary_left_x[i] and x + car_width < road_boundary_left_x[i] + \
                            road_boundary_width):
                    crash_flag = True
                if (x > road_boundary_left_x[i] + road_width and x < road_boundary_left_x[i] + road_width + road_boundary_width) or \
                    (x + car_width > road_boundary_left_x[i] + road_width and x + car_width < road_boundary_left_x[i] + \
                            road_width + road_boundary_width):
                    crash_flag = True

        for i in range(road_boundary_blocks - 1, 0, -1):
            road_boundary_left_x[i] = road_boundary_left_x[i-1]
            #print(str(i) + " " + str(road_boundary_left_x[i]) + " " + str(road_boundary_left_x[i-1]))

        left_pos = road_boundary_left_x[0] - int(scale_factor * road_boundary_width)
        right_pos = road_boundary_left_x[0] + int(scale_factor * road_boundary_width)
        if (road_boundary_left_x[0] - road_boundary_width) < 0:
            left_pos = 0
        if (road_boundary_left_x[0] + road_boundary_width) > (display_width - road_width):
            right_pos = road_boundary_left_x[0] - 1

        road_boundary_left_x[0] = random.randrange(left_pos, right_pos + 1)

        if cop_car_y > display_height:
            cop_car_y = 0 - cop_car_height
            cop_car_x = random.randrange(int(road_boundary_left_x[0] + 2 * road_boundary_width), \
                    int(road_boundary_left_x[0] + road_width - cop_car_width - 2 * road_boundary_width))
            dodged += 1
            #cop_car_speed += scale_factor * cop_car_speed
            cop_car_speed += 1
            scale_factor += 0.05
            cop_car_width += 0.5

        if dodged > high_score:
            high_score = dodged

        if x > display_width - car_width or x < 0: #or y > display_height - car_height or y < 0:
            crash_flag = True

        if y < cop_car_y + cop_car_height and y + car_height > cop_car_y:
            if (x > cop_car_x and x < cop_car_x + cop_car_width) or \
                (x + car_width > cop_car_x and x + car_width < cop_car_x + cop_car_width):
                crash_flag = True


        if crash_flag:
            crash(dodged, high_score)

        pygame.display.update()
        clock.tick(60)

    pygame.quit()
    quit()

game_intro()
