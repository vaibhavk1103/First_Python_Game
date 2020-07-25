import random                                                                                                         # Importing the required packages.
import os                                                                                                             # Importing the required packages.
import game_config as gc                                                                                              # Importing the required packages.

from pygame import image, transform                                                                                   # Importing the required packages.

animals_count = dict((a, 0) for a in gc.ASSET_FILES)                                                                  # Creating a dictionary for images in ASSET_FILES.

def available_animals():
    return [animal for animal, count in animals_count.items() if count < 2]                                           # Returning an animal from the dictionary.

class Animal:
    def __init__(self, index):                                                                                        # Memory allocation for the class.
        self.index = index
        self.name = random.choice(available_animals())                                                                # Setting random animals in places.
        self.image_path = os.path.join(gc.ASSET_DIR, self.name)                                                       # Bringing in the images from ASSET_FILES.
        self.row = index // gc.NUM_TILES_SIDE                                                                         # Animals in row.
        self.col = index % gc.NUM_TILES_SIDE                                                                          # Animals in column.
        self.skip = False                                                                                             # Skip if two consecutive pictures don't match.
        self.image = image.load(self.image_path)                                                                      # Loading a certain image.
        self.image = transform.scale(self.image, (gc.IMAGE_SIZE - 2 * gc.MARGIN, gc.IMAGE_SIZE - 2 * gc.MARGIN))      # Transforming the image to fit in well in the grid.
        self.box = self.image.copy()                                                                                  # Creating a copy of the image for further use.
        self.box.fill((200, 200, 200))                                                                                # Creating a box to be used when the pictures don't match.

        animals_count[self.name] += 1
