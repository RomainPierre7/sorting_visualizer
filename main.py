import pygame
from pygame.locals import *
import importlib
import inspect
import view

module = importlib.import_module("algorithms")
algorithms_name = [name for name, obj in inspect.getmembers(module) if inspect.isfunction(obj)]
algorithms_func = [obj for name, obj in inspect.getmembers(module) if inspect.isfunction(obj)]

pygame.init()
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("Sorting visualizer")

selected_option = 0
running = True
algo_running = False
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        elif event.type == KEYDOWN:
            if event.key == K_DOWN:
                selected_option = (selected_option + 1) % len(algorithms_name)
            elif event.key == K_UP:
                selected_option = (selected_option - 1) % len(algorithms_name)
            elif event.key == K_RETURN and not algo_running:
                algo_running = True
                view.shuffle()
                algorithms_func[selected_option]()
                algo_running = False
    
    screen.fill((255, 255, 255))
    
    for i, option in enumerate(algorithms_name):
        text_color = (0, 0, 0) if i == selected_option else (100, 100, 100)
        font = pygame.font.Font(None, 36)
        text = font.render(option, True, text_color)
        screen.blit(text, (50, 50 + i * 50))
    
    pygame.display.flip()

pygame.quit()
