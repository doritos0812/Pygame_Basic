import pygame
import random
import os
#################################################
# Basic Initialization (have to)
pygame.init() # Initialize

# Screen Set
screen_width = 480  # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("똥 피하기") # Game title

# FPS
clock = pygame.time.Clock()
##################################################

# 1. User Game Initialization (BackGround, Images, Graph, Speed, Font etc..)

current_path = os.path.dirname(__file__) # return current file path
image_path = os.path.join(current_path, "Images")

background = pygame.image.load(os.path.join(image_path, "Backgr.png"))

man = pygame.image.load(os.path.join(image_path, "man.png"))
man_size = man.get_rect().size # load size
man_width = man_size[0]
man_height = man_size[1]
man_x_pos = (screen_width - man_width) // 2 # 화면 가로의 중간에 위치
man_y_pos = screen_height - man_height # 화면 세로의 맨 아래에 위치




crap = pygame.image.load(os.path.join(image_path, "crap.png"))
crap_size = crap.get_rect().size # load size
crap_width = crap_size[0]
crap_height = crap_size[1]
crap_x_pos = random.randrange(0, (screen_width - crap_width))
crap_y_pos = 0 # 화면 세로의 맨 아래에 위치

crap2 = pygame.image.load(os.path.join(image_path, "crap.png"))
crap2_size = crap2.get_rect().size # load size
crap2_width = crap2_size[0]
crap2_height = crap2_size[1]
crap2_x_pos = random.randrange(0, (screen_width - crap2_width))
crap2_y_pos = -320 

# Move Graph
to_x = 0
to_y = 0

# Char Speed
man_speed = 10
crap_speed = 10
crap2_speed = 10

# Set Font
game_font = pygame.font.Font(None, 40) # 폰트 생성 (폰트, 크기)

# Time Count
start_ticks = pygame.time.get_ticks()



running = True
while running:
    dt = clock.tick(60) # Set Screen FPS
    # print("FPS : " + str(clock.get_fps()))

    # 2. Event Process (keyboard or mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= man_speed
            elif event.key == pygame.K_RIGHT:
                to_x += man_speed
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
                
    # 3. man Position Def

    man_x_pos += to_x
    crap_y_pos += crap_speed
    crap2_y_pos += crap2_speed


    if (crap_y_pos > screen_height):
        crap_y_pos = 0
        crap_x_pos = random.randrange(0, screen_width - crap_width)

    if (crap2_y_pos > screen_height):
        crap2_y_pos = 0
        crap2_x_pos = random.randrange(0, screen_width - crap2_width)

    # 4. Collision Check

    if man_x_pos < 0:
        man_x_pos = 0
    elif man_x_pos > screen_width - man_width:
        man_x_pos = screen_width - man_width

    man_rect = man.get_rect()
    man_rect.left = man_x_pos
    man_rect.top = man_y_pos

    crap_rect = crap.get_rect()
    crap_rect.left = crap_x_pos
    crap_rect.top = crap_y_pos

    crap2_rect = crap2.get_rect()
    crap2_rect.left = crap2_x_pos
    crap2_rect.top = crap2_y_pos

    # 충돌 체크
    if man_rect.colliderect(crap_rect):
        print("충돌!!")
        running = False
    
    if man_rect.colliderect(crap2_rect):
        print("충돌!!")
        running = False


    # 5. Print on Screen

    screen.blit(background, (0, 0))
    screen.blit(man, (man_x_pos, man_y_pos))
    screen.blit(crap, (crap_x_pos, crap_y_pos))
    screen.blit(crap, (crap2_x_pos, crap2_y_pos))
    
    # Timer
    total_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms

    timer = game_font.render("You've Survived " + str(int(total_time)) + " sec!!", True, (0, 0, 0)) # 출력할 글자, True, 글자색상
    
    screen.blit(timer, (10, 10))


    pygame.display.update()
    
pygame.quit()
