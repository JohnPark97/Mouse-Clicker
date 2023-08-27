import pygame
import random
from Square import Square

pygame.init()
pygame.font.init()

# Create the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Mouse Destroyer")
pygame.mouse.set_visible(False)

clock = pygame.time.Clock()
FPS = 60

# Colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0 , 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)


pointer = pygame.Surface((5, 5))
pointer.fill(RED)
pointer_mask = pygame.mask.from_surface(pointer)

squares = []

myfont = pygame.font.SysFont('Comic Sans MS', 30)

def generate_square():
    rand_coord = (random.randint(0, SCREEN_WIDTH), random.randint(0, SCREEN_HEIGHT))
    square = Square(rand_coord[0], rand_coord[1], pygame.Surface((50, 50)), BLUE)
    
    squares.append(square)

def draw_squares():
    for square in squares:
        screen.blit(square.surface, (square.x, square.y))

def handle_collision(mouse_pos, score: int):
    for square in squares:
        if pointer_mask.overlap(square.mask, (square.x - mouse_pos[0], square.y - mouse_pos[1])) and pygame.mouse.get_pressed()[0]:
            squares.remove(square)
            score += 1
            break
    return score

def display_score(score: int):
    textsurface = myfont.render('Score: ' + str(score), False, (0, 0, 0))
    screen.blit(textsurface,(0,0))


def main():
    #game loop
    running = True
    frame = 0
    score = 0
    
    while running:
        clock.tick(FPS)
        screen.fill(WHITE)

        mouse_pos = pygame.mouse.get_pos()

        if frame % FPS == 0:
            generate_square()
        
        draw_squares()
        screen.blit(pointer, (mouse_pos)) 

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        score = handle_collision(mouse_pos, score)
        display_score(score)
        pygame.display.update()

        frame += 1

    pygame.quit()

if __name__ == "__main__":
    main()