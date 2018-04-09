import world, characters, settings, generate, utilities
import pygame, time





pygame.init()
myfont = pygame.font.SysFont("monospace", 15)
winfont = pygame.font.SysFont("monospace", 50)
win_label = winfont.render("YOU WIN", 1, (255,255,0))

done = False


while not done:
    event = pygame.event.poll()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w]:
        world.adventurer.move_y(-1)
    if keys[pygame.K_s]:
        world.adventurer.move_y(1)
    if keys[pygame.K_a]:
        world.adventurer.move_x(-1)
    if keys[pygame.K_d]:
        world.adventurer.move_x(1)
    if keys[pygame.K_RIGHT] and event.type == pygame.KEYDOWN:
        world.adventurer.attack_projectile((1, 0))
    if keys[pygame.K_LEFT] and event.type == pygame.KEYDOWN:
        world.adventurer.attack_projectile((-1, 0))
    if keys[pygame.K_UP] and event.type == pygame.KEYDOWN:
        world.adventurer.attack_projectile((0, -1))
    if keys[pygame.K_DOWN] and event.type == pygame.KEYDOWN:
        world.adventurer.attack_projectile((0, 1))



    #for event in pygame.event.get():
    if event.type == pygame.QUIT:
        done = True

    world.screen.fill(pygame.Color("black")) # erases the entire screen surface
    
    for room in world.rooms:
        room.render()
        room.door.render()
    world.adventurer.render()
    for bat in world.bats:
        bat.render()
        bat.fly()
    for projectile in world.projectiles:
        projectile.render()
        projectile.fly()
    for health_pack in world.health_packs:
        health_pack.render()
    for arrow_pack in world.arrow_packs:
        arrow_pack.render()
    for speed_pack in world.speed_packs:
        speed_pack.render()

    arrow_label = myfont.render("Arrows: " + str(world.adventurer.arrow_count), 1, (255,255,0))
    health_label = myfont.render("Health: " + str(world.adventurer.health), 1, (255,255,0))
    speed_label = myfont.render("Speed:  " + str(world.adventurer.speed), 1, (255,255,0))

    # Arrows
    world.screen.blit(arrow_label, (settings.screenWidth - 110, 20))
    # Health
    world.screen.blit(health_label, (settings.screenWidth - 110, 35))
    # Speed
    world.screen.blit(speed_label, (settings.screenWidth - 110, 50))
    # Win
    if (len(world.bats) == 0):
        if (world.clock == ""):
            world.clock = time.time()

        world.screen.blit(win_label, (settings.screenWidth // 2, settings.screenHeight // 2))
        if (-(world.clock - time.time()) >= 3):
            world.clock = ""
            settings.increment_level()

    pygame.display.flip()