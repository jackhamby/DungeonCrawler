from random import *
import pygame, time



_image_library = {}
def get_image(path):
        global _image_library
        image = _image_library.get(path)
        if image == None:
                image = pygame.image.load(base_img_url + path)
                _image_library[path] = image
        return image

    # adventurer = Adventurer()

def getRandomColor():
    return (randint(0, 255),randint(0, 255),randint(0, 255))


