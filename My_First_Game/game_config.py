import os                                                                        # Importing the required packages.

IMAGE_SIZE = 128                                                                 # Size of every image.
SCREEN_SIZE = 512                                                                # Size of screen.
NUM_TILES_SIDE = 4                                                               # Setting the number of images per row.
NUM_TILES_TOTAL = 16                                                             # Setting the number of images in total.
MARGIN = 8                                                                       # Setting the gap between each image.

ASSET_DIR = 'assets'                                                             # Folder from which the images are to be imported.
ASSET_FILES = [x for x in os.listdir(ASSET_DIR) if x[-3:].lower() == 'png']      # Importing files which end with extension'png' i.e. images.
assert len(ASSET_FILES) == 8                                                     # Checking the number of images imported.
