import pygame
import random
import numpy as np

pygame.init()
VIDEO_PROF = 150
SCREEN_SIZE = 600
PLAY_FRAME_SIZE = 350
SNAKE_HEAD_IMG = pygame.image.load('images/snake.png')
SNAKE_BODY_IMG = pygame.image.load('images/body.png')
APPLE_IMG = pygame.image.load('images/apple.png')
clock = pygame.time.Clock()


def create_snake(end_game, next_dir, snake_head, snake_body):
    if next_dir == 0:
        snake_head[1] -= 10
    elif next_dir == 1:
        snake_head[0] += 10
    elif next_dir == 2:
        snake_head[1] += 10
    elif next_dir == 3:
        snake_head[0] -= 10

    if (snake_head[0] < 100 or snake_head[0] > 480
        or snake_head[1] < 150 or snake_head[1] > 530):
        end_game = True

    snake_body.insert(0, list(snake_head)) # append at the 0 postion
    snake_body.pop() # pop last element, so the sanek can move forward

    return end_game, snake_head, snake_body



def play(window, snake_head, snake_body, apple_position):
    end_game = False
    next_dir = 0
    # 0 - up, 1 - rigth, 2 - down, 3 - left

    while end_game is not True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                end_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    next_dir = 1
                elif event.key == pygame.K_UP:
                    next_dir = 0
                elif event.key == pygame.K_DOWN:
                    next_dir = 2
                elif event.key == pygame.K_LEFT:
                    next_dir = 3

        end_game, snake_head, snake_body = create_snake(end_game, next_dir, snake_head, snake_body)

        refresh_window(window, snake_head, snake_body, apple_position)



def refresh_window(window, snake_head, snake_body, apple_position):
    window.fill((200, 200, 200))
    pygame.draw.rect(window, (255, 0, 0), (100, 150, 400, 400), 3)

    for position in snake_body[1:]:
        window.blit(SNAKE_BODY_IMG, (position[0], position[1]))

    window.blit(SNAKE_HEAD_IMG, (snake_head[0], snake_head[1]))


    window.blit(APPLE_IMG, (apple_position[0], apple_position[1]))
    pygame.display.update()
    clock.tick(5)



if __name__ == "__main__":
    window = pygame.display.set_mode((SCREEN_SIZE, SCREEN_SIZE))

    snake_head = [300, 300]
    snake_body = [[300, 300], [290, 300, 280, 300]]
    apple_position = [random.randrange(20, 40)*10, random.randrange(20, 40)*10]

    refresh_window(window, snake_head, snake_body, apple_position)

    play(window, snake_head, snake_body, apple_position)

    pygame.quit()
