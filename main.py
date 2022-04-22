import pygame

def main():
    pygame.init()
    render_frame()

def render_frame():
    screen_size = (1920, 1080)
    surface = pygame.display.set_mode(screen_size)

    while (True):
        clock = pygame.time.Clock()
        pygame.draw.circle(surface, (0,0,255), (960,540), 50)
        pygame.display.flip()

def create_main_surface(size):
    return pygame.display.set_mode(size)

main()