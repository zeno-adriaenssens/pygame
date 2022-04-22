from re import X
import pygame

def main():
    pygame.init()
    state = State()
    global surface
    screen_size = (1920, 1080)
    surface = create_main_surface(screen_size)
    while (True):
        update(state)
        render_frame(state, surface)

def update(state):
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                State.decrement_x(state)
            if event.key == pygame.K_UP:
                State.decrement_y(state)
            if event.key == pygame.K_DOWN:
                State.increment_y(state)
            if event.key == pygame.K_RIGHT:
                State.increment_x(state)
    State.render(state)

def render_frame(state, surface):
    #clock = pygame.time.Clock()
    surface.fill((0,0,0))
    State.render(state)
    pygame.display.flip()

def create_main_surface(size):
    return pygame.display.set_mode(size)


class State:
    def __init__(self):
        self.x = 960
        self.y = 540

    def increment_x(self):
        self.x += 25

    def decrement_x(self):
        self.x -= 25

    def increment_y(self):
        self.y += 25

    def decrement_y(self):
        self.y -= 25
    
    def render(self):
        pygame.draw.circle(surface, (0,0,255), (50+self.x,50+self.y), 50)

main()

