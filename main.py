import pygame
import random

pygame.init()


# "Drawing" information to be accessed as needed, several different functions will require this information
class DrawInformation:
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    GREEN = (0, 255, 0)
    RED = (255, 0, 0)
    BACKGROUND_COLOR = WHITE

    BAR_COLORS = [
        (128, 128, 128),
        (160, 160, 160),
        (192, 192, 192)
    ]

    FONT = pygame.font.SysFont('Calibri', 30)
    LARGE_FONT = pygame.font.SysFont('Calibri', 40)
    SIDE_PADDING = 100
    TOP_PADDING = 150

    def __init__(self, width, height, lst):
        # Width depends on number of bars/values in the list
        # Height depends on the range of values in the list
        self.width = width
        self.height = height

        self.window = pygame.display.set_mode((width, height))
        pygame.display.set_caption("Sorting Algorithm Visualizer")

        self.set_list(lst)

    # Dynamically set width/height
    def set_list(self, lst):
        self.lst = lst
        self.max_val = max(lst)
        self.min_val = min(lst)

        # each bar is comprised of equally sized "blocks"
        self.block_width = round((self.width - self.SIDE_PADDING) / len(lst))
        # total drawable area divide by the number of bars
        self.block_height = round((self.height - self.TOP_PADDING) / (self.max_val - self.min_val))
        # total drawable area, divide by the range of values (1, 1000) = 1000 total units
        # the max range determines the units of all other bars
        self.start_x = self.SIDE_PADDING // 2


def draw(draw_info):
    draw_info.window.fill(draw_info.BACKGROUND_COLOR) # "resetting" the window before update

    control_panel = draw_info.FONT.render(
        "R - Reset | SPACE - Start Sorting | A - Ascending | D - Descending", 1, draw_info.BLACK)

    # x coord - window width/2 - textwidth/2
    # hard coded y coord
    draw_info.window.blit(control_panel, (draw_info.width/2 - control_panel.get_width()/2, 5))

    sorting_panel = draw_info.FONT.render(
        "I - Insertion Sort | B - Bubble Sort", 1, draw_info.BLACK)
    draw_info.window.blit(sorting_panel, (draw_info.width/2 - sorting_panel.get_width()/2, 35))

    draw_list(draw_info)
    pygame.display.update()


def draw_list(draw_info):
    lst = draw_info.lst

    for i, val in enumerate(lst):
        # calculate, x/y coordinate for the bar
        # *** review 30:00
        x = draw_info.start_x + i * draw_info.block_width
        y = draw_info.height - (val - draw_info.min_val) * draw_info.block_height

        # determine color
        color = draw_info.BAR_COLORS[i % 3]

        # draw
        pygame.draw.rect(draw_info.window, color, (x, y, draw_info.block_width, draw_info.height))


def generate_starting_list(n, min_val, max_val):
    lst = []

    for _ in range(n):
        val = random.randint(min_val, max_val)
        lst.append(val)

    return lst


def main():
    run = True
    clock = pygame.time.Clock()

    n = 50
    min_val = 0
    max_val = 100
    sorting = False
    ascending = True

    lst = generate_starting_list(n, min_val, max_val)
    draw_info = DrawInformation(800, 600, lst)

    while run:
        clock.tick(60)

        draw(draw_info)
        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # x out window
                run = False
            if event.type != pygame.KEYDOWN:
                continue

            # Key presses
            # *** add in some way to indicate what current option we are on
            if event.key == pygame.K_r:  # press r to regenerate list
                lst = generate_starting_list(n, min_val, max_val)
                draw_info.set_list(lst)
                sorting = False
            elif event.key == pygame.K_SPACE and sorting == False: # space to sort
                sorting = True
            elif event.key == pygame.K_a and not sorting:
                ascending = True
            elif event.key == pygame.K_d and not sorting:
                ascending = False

# *** display some sort of time taken for efficiency comparison
# *** allow user input of parameters
    pygame.quit()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pychar`m`/
