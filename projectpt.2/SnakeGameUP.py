# Importing pygame and random Modules
import pygame
import random

# Initiating Pygame
pygame.init()

# Creating Window Dimensions
window_x = 800
window_y = 800

# Setting Window Title and Initiating the Clock
pygame.display.set_caption('SnakeGamePlus2.0 By Nicholas Dill')
game_window = pygame.display.set_mode((window_x, window_y))
fps = pygame.time.Clock()

# Setting the Speed of the Snake
snake_speed = 15

# Initiating Sound Effects
death_noise = pygame.mixer.Sound('audio/Small Glass Pane Shatter.mp3')
point_noise = pygame.mixer.Sound('audio/Beep Short .mp3')


# Function for Quiting the Game
def end_game():
    pygame.quit()
    quit()


# Alternative Function for Fonts
def alt_ob(text, font):
    text_surface = font.render(text, True, pygame.Color('red'))
    return text_surface, text_surface.get_rect()


# Function for Fonts
def text_ob(text, font):
    text_surface = font.render(text, True, pygame.Color('white'))
    return text_surface, text_surface.get_rect()


# Initiating the Buttons
def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if x+w > mouse[0] > x and y+h > mouse[1] > y:
        pygame.draw.rect(game_window, ac, (x, y, w, h))
        if click[0] == 1 and action is not None:
            action()
    else:
        pygame.draw.rect(game_window, ic, (x, y, w, h))
    button_font = pygame.font.Font('font/Computerfont.ttf', 50)
    text_surf, text_rect = text_ob(msg, button_font)
    text_rect.center = ((x+(w/2)), (y+(h/2)))
    game_window.blit(text_surf, text_rect)


# Initiating the Unpausing Function
def unpaused():
    global pause
    pygame.mixer.music.unpause()
    pause = False


# Initiating the Pausing Function
def paused():
    pygame.mixer.music.pause()
    pause_font = pygame.font.Font('font/ka1.ttf', 60)
    text_surf, text_rect = text_ob('Paused', pause_font)
    text_rect.center = ((window_x/2), (window_y/4))
    game_window.blit(text_surf, text_rect)

    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        button("Continue", 50, 550, 275, 100, pygame.Color('dark green'), pygame.Color('green'), unpaused)
        button("Quit", 480, 550, 275, 100, pygame.Color('dark red'), pygame.Color('red'), end_game)
        pygame.display.update()
        fps.tick(snake_speed)


# Initiating the Score Function
def show_points():
    point_font = pygame.font.Font('font/DISPLAY FREE TFB.ttf', 30)
    point_surface = point_font.render('Your Score : ' + str(points), True, pygame.Color('white'))
    point_rect = point_surface.get_rect()
    game_window.blit(point_surface, point_rect)


# Function for When a Game Over Occurs
def game_over():
    pygame.mixer.Sound.play(death_noise)
    pygame.mixer.music.stop()
    game_font = pygame.font.Font('font/ka1.ttf', 30)
    text_surf, text_rect = alt_ob('Game Over! Your Score is: ' + str(points), game_font)
    text_rect.center = ((window_x/2), (window_y/4))
    game_window.blit(text_surf, text_rect)

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        button("Try Again?", 50, 550, 275, 100, pygame.Color('dark green'), pygame.Color('green'), main)
        button("Quit", 480, 550, 275, 100, pygame.Color('dark red'), pygame.Color('red'), end_game)
        pygame.display.update()
        fps.tick(snake_speed)


# Function for Displaying the Main Menu Screen
def menu():
    start = True
    while start:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_window.fill(pygame.Color('black'))
        menu_font = pygame.font.Font('font/Digital System.ttf', 100)
        text_surf, text_rect = text_ob("Snake Game Plus!", menu_font)
        text_rect.center = ((window_x/2), (window_y/4))
        game_window.blit(text_surf, text_rect)

        button("Let's Snake!", 50, 550, 275, 100, pygame.Color('dark green'), pygame.Color('green'), main)
        button("Quit", 480, 550, 275, 100, pygame.Color('dark red'), pygame.Color('red'), end_game)
        button("Instructions", 260, 670, 275, 100, pygame.Color('gold'), pygame.Color('yellow'), instruction)

        pygame.display.update()
        fps.tick(snake_speed)


# Function for Displaying the Instructions Screen
def instruction():
    direct = True
    while direct:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
        game_window.fill(pygame.Color('black'))
        instruction_font = pygame.font.Font('font/ka1.ttf', 25)
        instruction_one = instruction_font.render('How to play: ', True, pygame.Color('white'))
        instruction_two = instruction_font.render('Use The ARROW Keys to Move Your Snake!', True, pygame.Color('white'))
        instruction_three = instruction_font.render('Collect Apples to Score Points!', True, pygame.Color('white'))
        instruction_four = instruction_font.render('Press The ESCAPE Key to Pause the Game!', True, pygame.Color('white'))
        instruction_five = instruction_font.render('Try Not to Hit Yourself or Any Walls ', True, pygame.Color('white'))
        instruction_six = instruction_font.render("or It's Game Over!", True, pygame.Color('white'))
        instruction_seven = instruction_font.render('Good Luck!', True, pygame.Color('white'))
        game_window.blit(instruction_one, (300, 0))
        game_window.blit(instruction_two, (50, 40))
        game_window.blit(instruction_three, (100, 70))
        game_window.blit(instruction_four, (30, 100))
        game_window.blit(instruction_five, (70, 130))
        game_window.blit(instruction_six, (250, 160))
        game_window.blit(instruction_seven, (300, 190))

        button("Let's Snake!", 30, 550, 300, 100, pygame.Color('dark green'), pygame.Color('green'), main)
        button("Quit", 480, 550, 300, 100, pygame.Color('dark red'), pygame.Color('red'), end_game)

        pygame.display.update()
        fps.tick(snake_speed)


# Function for the Main Gameplay Section of the Game
def main():
    global pause
    pygame.mixer.music.load('audio/A Night Alone - TrackTribe.mp3')
    pygame.mixer.music.play(-1)
    snake_speed = 15
    done = False

    window_x = 800
    window_y = 800
    snake_pos = [100, 50]
    snake_body = [[100, 50], [90, 50], [80, 50], [70, 50]]

    food_pos = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]
    food_spawn = True

    direction = 'RIGHT'
    change_to = direction

    global points
    points = 0
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
                pygame.quit()
                quit()
# Initiating the Button Presses
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    change_to = 'UP'
                if event.key == pygame.K_DOWN:
                    change_to = 'DOWN'
                if event.key == pygame.K_LEFT:
                    change_to = 'LEFT'
                if event.key == pygame.K_RIGHT:
                    change_to = 'RIGHT'
                if event.key == pygame.K_ESCAPE:
                    pause = True
                    paused()
                if event.key == pygame.K_r:
                    pygame.time.delay(-1000)
                    main()
                if event.key == pygame.K_q:
                    pygame.quit()
                    quit()

        if change_to == 'UP' and direction != 'DOWN':
            direction = 'UP'
        if change_to == 'DOWN' and direction != 'UP':
            direction = 'DOWN'
        if change_to == 'LEFT' and direction != 'RIGHT':
            direction = 'LEFT'
        if change_to == 'RIGHT' and direction != 'LEFT':
            direction = 'RIGHT'

        if direction == 'UP':
            snake_pos[1] -= 10
        if direction == 'DOWN':
            snake_pos[1] += 10
        if direction == 'LEFT':
            snake_pos[0] -= 10
        if direction == 'RIGHT':
            snake_pos[0] += 10

# Initiating What Happens When an Apple is Collected
        snake_body.insert(0, list(snake_pos))
        if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
            points += 1
            pygame.mixer.Sound.play(point_noise)
            food_spawn = False
        else:
            snake_body.pop()

        if not food_spawn:
            food_pos = [random.randrange(1, (window_x // 10)) * 10, random.randrange(1, (window_y // 10)) * 10]

        food_spawn = True
        game_window.fill(pygame.Color('black'))

        for pos in snake_body:
            pygame.draw.rect(game_window, pygame.Color('green'), pygame.Rect(pos[0], pos[1], 10, 10))

        pygame.draw.rect(game_window, pygame.Color('red'), pygame.Rect(food_pos[0], food_pos[1], 10, 10))

        if snake_pos[0] < 0 or snake_pos[0] > window_x - 10:
            game_over()
        if snake_pos[1] < 0 or snake_pos[1] > window_y - 10:
            game_over()

        for block in snake_body[1:]:
            if snake_pos[0] == block[0] and snake_pos[1] == block[1]:
                game_over()

        show_points()
        pygame.display.update()
        fps.tick(snake_speed)


# Calling the Functions at Start of Game
menu()
main()
pygame.quit()
quit()
