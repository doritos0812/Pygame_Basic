import pygame

pygame.init() # Initialize

# Screen Set
screen_width = 480 # 가로
screen_height = 600 # 세로
screen = pygame.display.set_mode((screen_width, screen_height))

# Title
pygame.display.set_caption("Hmini Game") # Game title

# FPS
clock = pygame.time.Clock()

# BackGround
background = pygame.image.load("C:/Users/dorit/anaconda3/data/Pygame_Example/pygame_basic/bg.png")

# load Character
character = pygame.image.load("C:/Users/dorit/anaconda3/data/Pygame_Example/pygame_basic/Charac.png")
character_size = character.get_rect().size # load size
character_width = character_size[0]
character_height = character_size[1]
character_x_pos = (screen_width - character_width) // 2 # 화면 가로의 중간에 위치
character_y_pos = screen_height - character_height # 화면 세로의 맨 아래에 위치

# Move Graph
to_x = 0
to_y = 0

# Char Speed
character_speed = 0.6

# Enemy Char
enemy = pygame.image.load("C:/Users/dorit/anaconda3/data/Pygame_Example/pygame_basic/Enemy.png")
enemy_size = enemy.get_rect().size # load size
enemy_width = enemy_size[0]
enemy_height = enemy_size[1]
enemy_x_pos = (screen_width - enemy_width) // 2  # 화면 가로의 중간에 위치
enemy_y_pos = (screen_height - enemy_height) // 2  # 화면 세로의 맨 아래에 위치

# Set Font
game_font = pygame.font.Font(None, 40) # 폰트 생성 (폰트, 크기)

# Total Time
total_time = 10

# Time Count
start_ticks = pygame.time.get_ticks()




# Event roop
running = True
while running:
    dt = clock.tick(60) # Set Screen FPS

    # print("FPS : " + str(clock.get_fps()))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                to_x -= character_speed
            elif event.key == pygame.K_RIGHT:
                to_x += character_speed
            elif event.key == pygame.K_UP:
                to_y -= character_speed
            elif event.key == pygame.K_DOWN:
                to_y += character_speed
            
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                to_x = 0
            elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                to_y = 0

    character_x_pos += to_x * dt
    character_y_pos += to_y * dt
    
    # 경계 지정 
    if character_x_pos < 0:
        character_x_pos = 0
    elif character_x_pos > screen_width - character_width:
        character_x_pos = screen_width - character_width

    if character_y_pos < 0:
        character_y_pos = 0
    elif character_y_pos > screen_height - character_height:
        character_y_pos = screen_height - character_height

    # 충돌 처리
    character_rect = character.get_rect()
    character_rect.left = character_x_pos
    character_rect.top = character_y_pos

    enemy_rect = enemy.get_rect()
    enemy_rect.left = enemy_x_pos
    enemy_rect.top = enemy_y_pos

    # 충돌 체크
    if character_rect.colliderect(enemy_rect):
        print("충돌!!")
        running = False




    screen.blit(background, (0, 0))

    screen.blit(enemy, (enemy_x_pos, enemy_y_pos))
    screen.blit(character, (character_x_pos, character_y_pos))
    
    # Timer
    elapsed_time = (pygame.time.get_ticks() - start_ticks) / 1000 # ms

    timer = game_font.render(str(float(total_time - elapsed_time)), True, (0, 0, 0)) # 출력할 글자, True, 글자색상
    
    screen.blit(timer, (10, 10))

    # 0 sec = quit
    if total_time - elapsed_time <= 0:
        print("Time Out!!")
        running = False
    
    pygame.display.update()
    
pygame.time.delay(2000)
# pygame quit
pygame.quit()
