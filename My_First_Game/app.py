import pygame                                                                                          # Importing the required packages.
import game_config as gc                                                                               # Importing the required packages.

from pygame import display, event, image                                                               # Importing the required packages.
from time import sleep                                                                                 # Importing the required packages.
from animal import Animal                                                                              # Importing the required packages.

def find_index_from_xy(x, y):
    row = y // gc.IMAGE_SIZE                                                                           # Finding row index.
    col = x // gc.IMAGE_SIZE                                                                           # Finding column index.
    index = row * gc.NUM_TILES_SIDE + col                                                              # Net index of an image.
    return row, col, index

pygame.init()                                                                                          # Initialising Pygame interface.
display.set_caption('My First Game')                                                                   # Setting the name to be displayed on top of the game window.
screen = display.set_mode((gc.SCREEN_SIZE, gc.SCREEN_SIZE))                                            # Initialize a window or screen for display.
matched = image.load('other_assets/matched.png')                                                       # Loading a specific image to be displayed.
running = True                                                                                         # Setting the game to loop to run.
tiles = [Animal(i) for i in range(0, gc.NUM_TILES_TOTAL)]                                              # Arranging the animals in the grid.
current_images_displayed = []                                                                          # Creating a list to contain the currently displayed images.

while running:
    current_events = event.get()                                                                       # Gets all the events that have occurred till that step.

    for e in current_events:
        if e.type == pygame.QUIT:                                                                      # Checking whether the user has exited the game or not.
            running = False

        if e.type == pygame.KEYDOWN:                                                                   # Checking for key press.
            if e.key == pygame.K_ESCAPE:                                                               # Checking whether the pressed key is escape or not.
                running = False

        if e.type == pygame.MOUSEBUTTONDOWN:                                                           # Checking for mouse click.
            mouse_x, mouse_y = pygame.mouse.get_pos()                                                  # Getting the mouse position to determine which image has been clicked.
            row, col, index = find_index_from_xy(mouse_x, mouse_y)                                     # Getting the mouse position to determine which image has been clicked.
            if index not in current_images_displayed:                                                  # Checking if the same has been clicked more than once.
                if len(current_images_displayed) > 1:
                    current_images_displayed = current_images_displayed[1:] + [index]
                else:
                    current_images_displayed.append(index)                                             # If the image isn't present then it's index is appended.

    # Display animals
    screen.fill((255, 255, 255))                                                                       # Creating a white screen.

    total_skipped = 0                                                                                  # Initialising count.

    for i, tile in enumerate(tiles):
        current_image = tile.image if i in current_images_displayed else tile.box                      # If the image is present on the screen then it is matched otherwise a box is displayed.
        if not tile.skip:
            screen.blit(current_image, (tile.col * gc.IMAGE_SIZE + gc.MARGIN, tile.row * gc.IMAGE_SIZE + gc.MARGIN))  # Displaying the image in the given grid box.
        else:
            total_skipped += 1                                                                         # Skipping if the images don't match.

    display.flip()                                                                                     # Updating the display.

    # Check for matches
    if len(current_images_displayed) == 2:                                                             # If there are two images currently being displayed on the screen.
        idx1, idx2 = current_images_displayed
        if tiles[idx1].name == tiles[idx2].name:                                                       # if both the images being displayed are same.
            tiles[idx1].skip = True                                                                    # Skipping that tile for the rest of the game.
            tiles[idx2].skip = True                                                                    # Skipping that tile for the rest of the game.
            sleep(0.2)                                                                                 # Show blank screen for 0.2 seconds.
            screen.blit(matched, (0, 0))                                                               # Display matched message
            display.flip()                                                                             # Updating the display in order to display the matched image.
            sleep(0.5)                                                                                 # Show blank screen for 0.5 seconds.
            current_images_displayed = []                                                              # Emptying the image dictionary for the next iteration to give the desired output.

    if total_skipped == len(tiles):                                                                    # Checking whether the skips done is equal to the tiles.
        running = False                                                                                # Stopping the game loop.

print('Goodbye!')                                                                                      # Game exit message.
