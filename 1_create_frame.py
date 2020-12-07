import pygame

pygame.init() #초기화

# 화면 크기 set
screen_width = 480 # 가로
screen_height = 600 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# 화면 title
pygame.display.set_caption("Hmini Game") # Game title

# Event roop

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    
# pygame quit
pygame.quit()
