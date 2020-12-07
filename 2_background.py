import pygame

pygame.init() #초기화

# 화면 크기 set
screen_width = 480 # 가로
screen_height = 600 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# title
pygame.display.set_caption("Hmini Game") # Game title


# BackGround
background = pygame.image.load("C:/Users/dorit/anaconda3/data/Pygame_Example/pygame_basic/bg.png")

# Event roop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # screen.fill((0, 50, 0))        
    screen.blit(background, (0, 0))

    pygame.display.update()
    
# pygame quit
pygame.quit()
