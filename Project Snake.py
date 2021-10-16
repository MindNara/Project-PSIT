import pygame
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

dis_width = 1000
dis_height = 800

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("A Snake that's not a snake")

bg = pygame.image.load("grass.png").convert()

clock = pygame.time.Clock()

snake_block = 20
snake_speed = 15

font_style = pygame.font.SysFont("bahnschrift", 40)
score_font = pygame.font.SysFont("comicsansms", 30)

# Score เรา
def Your_score(score):
    value = score_font.render("Your Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])

# งูเรา
def our_snake(snake_block, snake_list, colors):
    for x in snake_list:
        pygame.draw.rect(dis, colors, [x[0], x[1], snake_block, snake_block])
    
# message จบ
def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1
    snake_speed = 15

    # ตำแหน่งสเกล
    foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
    
    # random colors
    num = 10
    colors = black
    random_colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

    while not game_over:
        
        while game_close == True:
            dis.blit(bg, [0, 0]) # Background หลัก
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT: # Arrow ซ้าย
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT: # Arrow ขวา
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP: # Arrow บน
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN: # Arrow ล่าง
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(blue) # สี Background
        dis.blit(bg, [0, 0]) # Background หลัก
        pygame.draw.rect(dis, yellow, [foodx, foody, snake_block, snake_block])
        snake_Head = [] # Body ของงู
        snake_Head.append(x1) 
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        if (Length_of_snake - 1) == num:
            colors = random_colors

        our_snake(snake_block, snake_List, colors)
        Your_score(Length_of_snake - 1)

        pygame.display.update()

        # ตำแหน่งการสุ่มแอปเปิ้ล
        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(0, dis_height - snake_block) / 20.0) * 20.0
            Length_of_snake += 1

        if (Length_of_snake - 1) == num:
            colors = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
            num += 10
            snake_speed += 1

        # FPS ของ Snake_Speed(15)
        clock.tick(snake_speed)

    pygame.quit()
    quit()


gameLoop()
