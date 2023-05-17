# By: Tim Tarver
# Moving Objects Game

# Import all needed modules

import pygame
import sys
import random

# Initialize the constructor for
# the game

pygame.init()
resolution = (720, 720)

# Initialize the random objects
# for the game

random_object_1 = random.randint(125, 255)
random_object_2 = random.randint(0, 255)
random_object_3 = random.randint(0, 255)

# Create Main Window

window = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()

# Set Colors of the Game

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)

# Store the colors in a list
# to randomize the game

color_list = [red, green, blue]
game_heading_r1 = 0
game_heading_r2 = 0
game_heading_r3 = 254
game_heading_r4 = 254

# Assign a color to the main player

player_1 = blue

# Create the shade of the
# Start Page

start_light_shade = (169, 169, 169)
start_dark_shade = (100, 100, 100)

start = white

# Create the Dimensions of the Game

width = window.get_width()
height = window.get_height()

# Create the position of the objects

initial_x = 40
initial_y = height/2

# Change positions of the Enemies

x = 300
y = 290
width_1 = 100
height_1 = 40
enemy_size = 50

# Font of Game

font_style = pygame.font.SysFont('Corbel', 35)
start_text = font_style.render('Start', True, white)
options_text = font_style.render('Options', True, white)
exit_text = font_style.render('Exit', True, white)
game_heading = font_style.render('Welcome to Moving Blocks Game!', True,
                                 (random_object_3, random_object_2, random_object_1))

# Locations of Enemy Objects

x_1 = random.randint(width/2, width)
y_1 = random.randint(100, height/2)
x_2 = 40
y_2 = 40
object_speed = 12

count = 0
red_green_blue = random.choice(color_list)

enemy_position = [width, random.randint(50, height-50)]
enemy_position_1 = [random.randint(width, width+100), random.randint(50, height-100)]

# Create the Game Over Function

def game_over_function():

    while True:

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.quit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if 100 < mouse_1[0] < 140 and height - 100 < mouse_1[1] < height - 80:
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    if width - 180 < mouse_1[0] < width - 100 and height - 100 < mouse_1[1] < height - 80:
                        game_function(initial_x, initial_y, object_speed, count)
                
        window.fill((65, 25, 64))
        font_style = pygame.font.SysFont('Corbel', 60)
        font_style_1 = pygame.font.SysFont('Corbel', 25)
        game_over = font_style.render('Try Again Cuh!', True, white)
        game_exit = font_style_1.render('Exit', True, white)
        restart = font_style_1.render('Restart', True, white)
        mouse_1 = pygame.mouse.get_pos()

        if 100 < mouse_1[0] < 140 and height - 100 < mouse_1[1] < height - 80:
            pygame.draw.rect(window, start_light_shade, [100, height - 100, 40, 20])
        else:
            pygame.draw.rect(window, start_dark_shade, [100, height - 100, 40, 20])

        if width - 180 < mouse_1[0] < width - 100 and height - 100 < mouse_1[1] < height - 80:
            pygame.draw.rect(window, start_light_shade, [width - 180, height - 100, 80, 20])
        else:
            pygame.draw.rect(window, start_dark_shade, [width - 180, height - 100, 80, 20])

        window.blit(game_exit, (100, height - 100))
        window.blit(restart, (width - 180, height - 100))
        window.blit(game_over, (width / 2 - 150, 295))

        pygame.display.update()

# Create main Game Function
# for the entire Game

def game_function(initial_x, initial_y, object_speed, count):

    while True:
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        keys = pygame.key.get_pressed()
        
        if keys[pygame.K_UP]:
            initial_y -= 30

        if keys[pygame.K_DOWN]:
            initial_y += 30

        window.fill((65, 25, 64))
        clock.tick(object_speed)

        rectangle = pygame.draw.rect(window, player_1,
                                     [initial_x, initial_y, 40, 40])

        font_style = pygame.font.SysFont('Corbel', 35)
        exit_2 = font_style.render("Exit", True, white)

        # If mouse hovers over exit button, change color shades
        # before clicking.
        
        mouse = pygame.mouse.get_pos()
        if width - 100 < mouse[0] < width and 0 < mouse[1] < 40:
            pygame.draw.rect(window, start_light_shade, [width - 100, 0, 100, 40])
        else:
            pygame.draw.rect(window, start_dark_shade, [width - 100, 0, 100, 40])

        if width - 100 < mouse[0] < width and 0 < mouse[1] < 40:
            if event.type == pygame.MOUSEBUTTON:
                pygame.quit()
        
        # Location of enemies, position movement and collision
        # detection of player with the enemies in game play.

        if enemy_position[0] > 0 and enemy_position[0] <= width:
            enemy_position[0] -= 10
        else:
            if enemy_position[1] <= 40 or enemy_position[1] >= height - 40:
                enemy_position[1] = height / 2
            if enemy_position_1[1] <= 40 or enemy_position_1[1] >= height - 40:
                enemy_position_1[1] = random.randint(40, height - 40)
            enemy_position[1] = random.randint(enemy_size, height - enemy_size)
            enemy_position[0] = width

        # Defect Might be under here
        
        if initial_x <= enemy_position[0] <= initial_x + 40 and initial_y >= enemy_position[1] >= initial_y - 40:
            game_over_function()

        if initial_y <= enemy_position[1] + enemy_size <= initial_y + 40 and initial_x <= enemy_position[0] >= initial_x + 40:
            game_over_function()

        pygame.draw.rect(window, red, [enemy_position[0],
                                       enemy_position[1], enemy_size, enemy_size])             

        if enemy_position_1[0] > 0 and enemy_position_1[0] <= width + 100:
            enemy_position_1[0] -= 10

        else:
            if enemy_position_1[1] <= 40 or enemy_position_1[1] >= height - 40:
                enemy_position_1[1] = height / 2
            enemy_position_1[1] = random.randint(enemy_size, height -  40)
            enemy_position_1[0] = width + 100

        if initial_x <= enemy_position_1[0] <= initial_x + 40 and initial_y >= enemy_position_1[1] >= initial_y - 40:
            enemy_position_1[0] = width + 100
            enemy_position_1[1] = random.randint(40, height - 40)
            count += 1
            object_speed += 1

        if initial_y <= enemy_position_1[1] + enemy_size <= initial_y + 40 and initial_x <= enemy_position_1[0] <= initial_x + 40:
            enemy_position_1[0] = width + 100
            enemy_position_1[1] = random.randint(40, height - 40)
            count += 1
            object_speed += 1

            if count >= 45:
                object_speed = 60

        # Defect might be under here
        
        if initial_y <= 18 or initial_y >= height - 18:
            game_over_function()

        if enemy_position_1[0] <= 0:
            game_over_function()

        pygame.draw.rect(window, blue, [enemy_position_1[0],
                                        enemy_position_1[1], enemy_size, enemy_size])    

        score_1 = font_style.render('Score:', True, white)
        window.blit(score_1, (width - 120, height - 40))
        window.blit(exit_2, (width - 80, 0))
        pygame.display.update()
        
# Develop Introduction Page of the Game

def introduction(game_heading_r1, game_heading_r2, game_heading,
                 exit_text, options_text, start_text):

    introduction = True
    
    while introduction:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        window.fill((65, 25, 64))

        # Location of Buttons on Introduction Page
        
        mouse = pygame.mouse.get_pos()
        if x < mouse[0] < x + width_1 and y < mouse[1] < y + height_1:
            pygame.draw.rect(window, start_light_shade, [x, y, width_1, height_1])
        else:
            if x < mouse[0] < x + width_1 + 40 and y + 70 < mouse[1] < y + 70 + height_1:
                pygame.draw.rect(window, start_light_shade, [x, y+70, width_1+40, height_1])
            else:
                if x < mouse[0] < width_1 + x and y + 140 < mouse[1] < y + 140 + height_1:
                    pygame.draw.rect(window, start_light_shade, [x, y+140, width_1, height_1])
                else:
                    pygame.draw.rect(window, start_dark_shade, [x, y, width_1, height_1])
                    pygame.draw.rect(window, start_dark_shade, [x, y+70, width_1+40, height_1])
                    pygame.draw.rect(window, start_dark_shade, [x, y+140, width_1, height_1])
                    
        if event.type == pygame.MOUSEBUTTONDOWN:
            if x < mouse[0] < x + width_1 and y < mouse[1] < y + height_1:
                game_function(initial_y, initial_x, object_speed, count)

        if event.type == pygame.MOUSEBUTTONDOWN:
            if x < mouse[0] < width_1 + x and y + 140 < mouse[1] < y + 140 + height_1:
                pygame.quit()

        font_style = pygame.font.SysFont('Corbel', 35)
        start_text = font_style.render('Start', True, white)
        options_text = font_style.render('Options', True, white)
        exit_text = font_style.render('Exit', True, white)
        game_heading = font_style.render('Welcome to the Moving Blocka Game!', True,
                                        (random_object_1, game_heading_r1, game_heading_r2))

        window.blit(game_heading, (312, 50))
        window.blit(start_text, (312, 295))
        window.blit(options_text, (312, 365))
        window.blit(exit_text, (312, 435))
        clock.tick(60)
        pygame.display.update()
        
    
introduction(game_heading_r1, game_heading_r2, game_heading,
             exit_text, options_text, start_text)


















