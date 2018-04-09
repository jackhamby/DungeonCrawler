import generate, characters, settings
import pygame, time

screen = pygame.display.set_mode((settings.screenWidth,settings.screenHeight))

# text = font.render("Hello, World", True, (0, settings.screenWidth - 100, screenHeight - 100))
clock = ""
rooms = []
rooms = generate.generateRooms()
adventurer = characters.Adventurer()
projectiles = []
health_packs = generate.generate_health_packs()
speed_packs = generate.generate_speed_packs()
arrow_packs = generate.generate_arrow_packs()

bats = []
for i in range(0, settings.monsterCount):
    bats.append(characters.Bat())
#bat = characters.Bat()
#myfont = pygame.font.SysFont("monospace", 15)