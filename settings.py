import world, generate, characters, pygame, os

base_img_url = os.path.dirname(os.path.realpath(__file__))
health_pack_icon = pygame.image.load(f'{base_img_url}/images/health_pack.png')
speed_pack_icon = pygame.image.load(f'{base_img_url}/images/speed_pack.png')
arrow_pack_icon = pygame.image.load(f'{base_img_url}/images/arrow_pack.png')
arrow_projectile_up_icon = pygame.image.load(f'{base_img_url}/images/arrow_projectile_up.png')

level = 1
screenWidth = 1000
screenHeight = 700
roomCount = 5
monsterCount = 2


def increment_level():
    global level, roomCount, monsterCount
    level += 1
    roomCount += 3
    monsterCount += 3
    world.rooms = generate.generateRooms()
    world.bats = []
    for i in range(0, monsterCount):
        world.bats.append(characters.Bat())
    world.health_packs = generate.generate_health_packs()
    world.arrow_packs = generate.generate_arrow_packs()
    world.speed_packs = generate.generate_speed_packs()
    world.projectiles = []
    world.adventurer.get_start_position()
