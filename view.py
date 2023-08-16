import pygame
import random

def print_text(screen, algorithms_name, selected_option):
    for i, option in enumerate(algorithms_name):
        text_color = (0, 0, 0) if i == selected_option else (100, 100, 100)
        font = pygame.font.Font(None, 36)
        text = font.render(option, True, text_color)
        screen.blit(text, (50, 50 + i * 50))

def print_charts(screen, array, colored):
    for i, value in enumerate(array):
        x = 400 + 20 * i
        y1 = 900
        y2 = 900 - 16 * value
        color = (250, 0, 0) if i in colored else (150, 150, 150)
        pygame.draw.line(screen, color, (x, y1), (x, y2), 10)
    return 0

def print_step(screen, array, colored):
    screen.fill((255, 255, 255))
    print_charts(screen, array, colored)
    pygame.display.flip()
    pygame.time.wait(10)

def shuffle(array):
    new_array = [-1 for _ in range(len(array))]
    for value in array:
        idx = random.randint(0, len(array) - 1)
        while new_array[idx] != -1:
            idx = random.randint(0, len(array) - 1)
        new_array[idx] = value
    return new_array