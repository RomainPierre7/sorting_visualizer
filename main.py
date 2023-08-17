import pygame
from pygame.locals import *
import importlib
import inspect
import view
import threading

module = importlib.import_module("algorithms")
algorithms_name = [name for name, obj in inspect.getmembers(module) if inspect.isfunction(obj)]
algorithms_func = [obj for name, obj in inspect.getmembers(module) if inspect.isfunction(obj)]

n = 50
array = [i for i in range(1, n + 1)]

pygame.init()
screen = pygame.display.set_mode((1500, 1000))
pygame.display.set_caption("Sorting visualizer")

def run_algorithm(algorithm_func, screen):
    global algo_running, array
    algo_running = True
    array = view.shuffle(screen, array)
    array = algorithm_func(screen, array)
    algo_running = False

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
            elif algo_running:
                continue
            elif event.key == K_RETURN and not algo_running:
                algorithm_thread = threading.Thread(target=run_algorithm, args=(algorithms_func[selected_option], screen))
                algorithm_thread.start()
    
    if not algo_running:
        screen.fill((255, 255, 255))
        view.print_text(screen, algorithms_name, selected_option)
        view.print_charts(screen, array, colored=[])
        pygame.display.flip()

pygame.quit()