import pygame
#################################################
# Basic Initialization (have to)
pygame.init() # Initialize

# Screen Set
screen_width = 480  # 가로
screen_height = 640 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("Game Title") # Game title

# FPS
clock = pygame.time.Clock()
##################################################

# 1. User Game Initialization (BackGround, Images, Graph, Speed, Font etc..)

running = True
while running:
    dt = clock.tick(60) # Set Screen FPS
    # print("FPS : " + str(clock.get_fps()))

    # 2. Event Process (keyboard or mouse)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # 3. Character Position Def

    # 4. Collision Check

    # 5. Print on Screen

    pygame.display.update()
    
pygame.quit()
