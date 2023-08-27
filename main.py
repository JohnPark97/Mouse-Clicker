import pygame
import random
from Square import Square

pygame.init()
pygame.font.init()

# Create the screen
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
Y_OFFSET = 40

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

# Pointer
pointer = pygame.Surface((5, 5))
pointer.fill(RED)
pointer_mask = pygame.mask.from_surface(pointer)

# Squares
SQUARE_SIZE = 50
squares = []

myfont = pygame.font.SysFont('Comic Sans MS', 30)

def generate_square():
    rand_coord = (random.randint(0, SCREEN_WIDTH - SQUARE_SIZE), random.randint(Y_OFFSET, SCREEN_HEIGHT - SQUARE_SIZE))
    square = Square(rand_coord[0], rand_coord[1], pygame.Surface((SQUARE_SIZE, SQUARE_SIZE)), BLUE)
    
    squares.append(square)

def draw_squares():
    for square in squares:
        screen.blit(square.surface, (square.x, square.y))

def handle_collision(mouse_pos, score: int):
    for square in squares:
        if pointer_mask.overlap(square.mask, (square.x - mouse_pos[0], square.y - mouse_pos[1])):
            squares.remove(square)
            score += 1
            break
    return score

def display_score(score: int):
    text_surface = myfont.render('Score: ' + str(score), False, (0, 0, 0))
    screen.blit(text_surface,(0,0))

def display_time():
    time_surface = myfont.render('Time: ' + str(pygame.time.get_ticks()//1000), False, (0, 0, 0))
    screen.blit(time_surface,(SCREEN_WIDTH - 150,0))

def main():
    #game loop
    running = True
    score = 0
    MIN_INTERVAL = 0.1
    INTERVAL = 1
    SPEED_UP_AMOUNT = 0.05
    SPEED_UP_INTERVAL = 5

    GENERATE_SQUARE_EVENT = pygame.USEREVENT + 1
    pygame.time.set_timer(GENERATE_SQUARE_EVENT, INTERVAL * 1000)

    SPEED_UP_EVENT = GENERATE_SQUARE_EVENT + 1
    pygame.time.set_timer(SPEED_UP_EVENT, INTERVAL * SPEED_UP_INTERVAL * 1000)

    generate_square()

    while running:
        clock.tick(FPS)
        screen.fill(WHITE)

        display_time()

        mouse_pos = pygame.mouse.get_pos()
        
        draw_squares()
        screen.blit(pointer, (mouse_pos)) 

        for event in pygame.event.get():
            if event.type == GENERATE_SQUARE_EVENT:
                generate_square()
            if event.type == SPEED_UP_EVENT:
                INTERVAL = max(INTERVAL - SPEED_UP_AMOUNT, MIN_INTERVAL)
                pygame.time.set_timer(SPEED_UP_EVENT, int(INTERVAL * 2 * 1000))
                pygame.time.set_timer(GENERATE_SQUARE_EVENT, int(INTERVAL * 1000))
            if event.type == pygame.MOUSEBUTTONDOWN:
                score = handle_collision(mouse_pos, score)
            
            if event.type == pygame.QUIT:
                running = False

        display_score(score)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()