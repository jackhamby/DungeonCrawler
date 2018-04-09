import world, generate, characters, pygame

base_img_url = "/Users/jackhamby/games/images/"
health_pack_icon = pygame.image.load('/Users/jackhamby/games/dungeon_crawler/images/health_pack.png')
speed_pack_icon = pygame.image.load('/Users/jackhamby/games/dungeon_crawler/images/speed_pack.png')
arrow_pack_icon = pygame.image.load('/Users/jackhamby/games/dungeon_crawler/images/arrow_pack.png')
arrow_projectile_up_icon = pygame.image.load('/Users/jackhamby/games/dungeon_crawler/images/arrow_projectile_up.png')

# arrow_projectile_down_down = pygame.image.load('/Users/jackhamby/games/game3/images/arrow_projectile2.png')
# arrow_projectile_right_down = pygame.image.load('/Users/jackhamby/games/game3/images/arrow_projectile2.png')
# arrow_projectile_left_down = pygame.image.load('/Users/jackhamby/games/game3/images/arrow_projectile2.png')

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
