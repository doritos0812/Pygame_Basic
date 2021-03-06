import pygame

pygame.init() # Initialize

# Screen Set
screen_width = 480 # 가로
screen_height = 600 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("Hmini Game") # Game title


# BackGround
background = pygame.image.load("C:/Users/dorit/anaconda3/data/Pygame_Example/pygame_basic/bg.png")

# load Character
character = pygame.image.load("C:/Users/dorit/anaconda3/data/Pygame_Example/pygame_basic/Charac.png")
character_size = character.get_rect().size # load size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) // 2 # 화면 가로의 중간에 위치
character_y_pos = screen_height - character_height # 화면 세로의 맨 아래에 위치



# Event roop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
      
    screen.blit(background, (0, 0))

    screen.blit(character, (character_x_pos, character_y_pos))
    pygame.display.update()
    
# pygame quit
pygame.quit()
