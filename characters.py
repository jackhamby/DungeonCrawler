from random import *
import pygame, time


import world, settings, utilities




class HealthPack:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.random_spawn()
        self.color = utilities.getRandomColor()
        self.living = True

        # Stats
        self.healing = 20
    
    def render(self):
        if (self.living):
            world.screen.blit(settings.health_pack_icon,(self.xPos, self.yPos))

    def die(self):
        self.living = False
        del world.health_packs[world.health_packs.index(self)]


    def random_spawn(self):
        sRoom = world.rooms[randint(0, len(world.rooms) - 1)]
        while(True):
            self.xPos = randint(sRoom.xPos, sRoom.xPos + sRoom.width)
            self.yPos = randint(sRoom.yPos, sRoom.yPos + sRoom.height)   
            if (sRoom.xPos <= self.xPos and 
                sRoom.yPos <= self.yPos and
                self.xPos + self.width <= sRoom.xPos + sRoom.width and
                self.yPos + self.height <= sRoom.yPos + sRoom.height):
                return
            print('found bad start position x:' + str(self.xPos) + ' y:' + str(self.yPos))
    

class ArrowPack:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.random_spawn()
        self.color = utilities.getRandomColor()
        self.living = True

        # Stats
        self.count = 20
    
    def render(self):
        if (self.living):
            world.screen.blit(settings.arrow_pack_icon,(self.xPos, self.yPos))

    def die(self):
        self.living = False
        del world.arrow_packs[world.arrow_packs.index(self)]


    def random_spawn(self):
        sRoom = world.rooms[randint(0, len(world.rooms) - 1)]
        while(True):
            self.xPos = randint(sRoom.xPos, sRoom.xPos + sRoom.width)
            self.yPos = randint(sRoom.yPos, sRoom.yPos + sRoom.height)   
            if (sRoom.xPos <= self.xPos and 
                sRoom.yPos <= self.yPos and
                self.xPos + self.width <= sRoom.xPos + sRoom.width and
                self.yPos + self.height <= sRoom.yPos + sRoom.height):
                return
            print('found bad start position x:' + str(self.xPos) + ' y:' + str(self.yPos))



class SpeedPack:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.random_spawn()
        self.color = utilities.getRandomColor()
        self.living = True

        # Stats
        self.boost = 1
    
    def render(self):
        if (self.living):
            world.screen.blit(settings.speed_pack_icon,(self.xPos, self.yPos))

    def die(self):
        self.living = False
        del world.speed_packs[world.speed_packs.index(self)]


    def random_spawn(self):
        sRoom = world.rooms[randint(0, len(world.rooms) - 1)]
        while(True):
            self.xPos = randint(sRoom.xPos, sRoom.xPos + sRoom.width)
            self.yPos = randint(sRoom.yPos, sRoom.yPos + sRoom.height)   
            if (sRoom.xPos <= self.xPos and 
                sRoom.yPos <= self.yPos and
                self.xPos + self.width <= sRoom.xPos + sRoom.width and
                self.yPos + self.height <= sRoom.yPos + sRoom.height):
                return
    


















##### ------------------------------------------------------------------------- #####
##### ------------------------------------------------------------------------- #####
##### ------------------------------------------------------------------------- #####

class Bat:
    def __init__(self):
        self.width = 20
        self.height = 20
        self.random_spawn()
        self.color = utilities.getRandomColor()
        self.axis = randint(0, 1) # 0: horizontal, 1: vertical
        self.dir = choice([1, -1])
        self.living = True

        # Stats
        self.speed = 1
        self.damage = 5
        self.health = 10

    def render(self):
        if (self.living):
            pygame.draw.rect(world.screen, self.color , pygame.Rect(self.xPos, self.yPos, self.width, self.height))


    def random_spawn(self):
        sRoom = world.rooms[randint(0, len(world.rooms) - 1)]
        while(True):
            self.xPos = randint(sRoom.xPos, sRoom.xPos + sRoom.width)
            self.yPos = randint(sRoom.yPos, sRoom.yPos + sRoom.height)   
            if (sRoom.xPos <= self.xPos and 
                sRoom.yPos <= self.yPos and
                self.xPos + self.width <= sRoom.xPos + sRoom.width and
                self.yPos + self.height <= sRoom.yPos + sRoom.height):
                return
            print('found bad start position x:' + str(self.xPos) + ' y:' + str(self.yPos))
    
    def die(self):
        self.living = False
        del world.bats[world.bats.index(self)]

    def fly(self):
        if(self.axis): # horixontal motion
            self.move_x(self.dir)
        else:
            self.move_y(self.dir)

    def move_x(self, direction):
        if (not self.detect_wall(self.xPos + (direction * self.speed), self.yPos)):
            self.xPos += (direction) * self.speed
        else:
            self.dir *= -1
            self.move_x(self.dir)

    def move_y(self, direction):
        if (not self.detect_wall(self.xPos, self.yPos + (direction * self.speed))):
            self.yPos += (direction) * self.speed
        else:
            self.dir *= -1
            self.move_y(self.dir)
    
    def detect_wall(self, xPosition, yPosition):

        if (self.detect_corner(xPosition, yPosition)
            and self.detect_corner(xPosition + self.width, yPosition)
            and self.detect_corner(xPosition + self.width, yPosition + self.height)
            and self.detect_corner(xPosition, yPosition + self.height)):
            return False

        return True

    def detect_corner(self, xCoord, yCoord):
        for room in world.rooms:
            # room.pDimensions()

            if (xCoord >= room.xPos and xCoord <= room.xPos + room.width
                and yCoord >= room.yPos and yCoord <= room.yPos + room.height
                and xCoord >= 0 and xCoord <= settings.screenWidth
                and yCoord >= 0 and yCoord <= settings.screenHeight):
                return True

##### ------------------------------------------------------------------------- #####
##### ------------------------------------------------------------------------- #####
##### ------------------------------------------------------------------------- #####

class Arrow:
    def __init__(self, xPosition, yPosition, direction):
        self.width = 5
        self.height = 17
        self.color = (0, 0, 0)
        self.xPos = xPosition
        self.yPos = yPosition
        self.dir = direction
        self.flying = True

        # Stats 
        self.damage = 10
        self.speed = 5

    def render(self):
        self.detect_monster(self.xPos, self.yPos)
        if (self.flying):
            if (self.dir[0] == 1):
                self.width, self.height = self.height, self.width
                world.screen.blit(pygame.transform.rotate(settings.arrow_projectile_up_icon, -90),(self.xPos, self.yPos))
            elif (self.dir[0] == -1):
                self.width, self.height = self.height, self.width
                world.screen.blit(pygame.transform.rotate(settings.arrow_projectile_up_icon, 90),(self.xPos, self.yPos))
            elif (self.dir[1] == 1):
                world.screen.blit(pygame.transform.rotate(settings.arrow_projectile_up_icon, 180),(self.xPos, self.yPos))              
            elif (self.dir[1] == -1):
                world.screen.blit(settings.arrow_projectile_up_icon,(self.xPos, self.yPos))

    def fly(self):
        self.move_x(self.dir[0])
        self.move_y(self.dir[1])

    def die(self):
        self.flying = False
        print('breaking arrow')
        if (self in world.projectiles):
            del world.projectiles[world.projectiles.index(self)]

    def move_x(self, direction):
        if (not self.detect_wall(self.xPos + (direction * self.speed), self.yPos)):
            self.xPos += (direction) * self.speed
        else:
            self.die()

    def move_y(self, direction):           
        if (not self.detect_wall(self.xPos, self.yPos + (direction * self.speed))):
            self.yPos += (direction) * self.speed
        else:
            self.die()
    
    def detect_wall(self, xPosition, yPosition):
        for room in world.rooms:
            if (room.xPos <= self.xPos and 
                room.yPos <= self.yPos and
                self.xPos + self.width <= room.xPos + room.width and
                self.yPos + self.height <= room.yPos + room.height):
                return False
        return True

    def detect_monster(self, xCoord, yCoord):
        for i, bat in enumerate(world.bats):
            if (bat.xPos + bat.width <= xCoord or # adventuer is to right of
                xCoord + self.width <= bat.xPos or # adventer is to left of
                yCoord + self.height <= bat.yPos or # adventurer is above
                bat.yPos + bat.height <= yCoord): # adventurer is below
                continue
            else:
                bat.health -= self.damage
                if (bat.health <= 0):
                    bat.die()
                self.die()
                return True
        return False

##### ------------------------------------------------------------------------- #####
##### ------------------------------------------------------------------------- #####
##### ------------------------------------------------------------------------- #####

class Adventurer:
    def __init__(self):
        self.width = 20
        self.height = 40
        self.get_start_position()
        self.color = (255, 255, 255)
        self.living = True


        # Stats
        self.health = 100
        self.speed = 2
        self.arrow_count = 50


    def in_room(self, xPosition, yPosition, room=None):
        if (room):
            if (room.xPos <= xPosition and 
                room.yPos <= yPosition and
                xPosition + self.width <= room.xPos + room.width and
                yPosition + self.height <= room.yPos + room.height):
                return True
            return False
        else:
            for room in world.rooms:
                 if (room.xPos <= xPosition and 
                    room.yPos <= yPosition and
                    xPosition + self.width <= room.xPos + room.width and
                    yPosition + self.height <= room.yPos + room.height):
                    return True
            return False


    def render(self):
        self.detect_monster(self.xPos, self.yPos)
        self.detect_health_pack(self.xPos, self.yPos)
        self.detect_arrow_pack(self.xPos, self.yPos)
        self.detect_speed_pack(self.xPos, self.yPos)
        self.detect_trap_door(self.xPos, self.yPos)
        if (self.living):
            pygame.draw.rect(world.screen, self.color , pygame.Rect(self.xPos, self.yPos, self.width, self.height))


    def move_x(self, direction):
        if (self.in_room(self.xPos + (direction * self.speed), self.yPos)):
            self.xPos += (direction) * self.speed

    def move_y(self, direction):
        if (self.in_room(self.xPos, self.yPos + (direction * self.speed))):
            self.yPos += (direction) * self.speed
    
    def detect_trap_door(self, xCoord, yCoord):
        for room in world.rooms:
            if (room.door.xPos + room.door.width <= xCoord or # adventuer is to right of
                xCoord + self.width <= room.door.xPos or # adventer is to left of
                yCoord + self.height <= room.door.yPos or # adventurer is above
                room.door.yPos + room.door.height <= yCoord): # adventurer is below
                continue
            else:
                # Enter Trap door
                room.door.enter(self)

    def detect_monster(self, xCoord, yCoord):
        for bat in world.bats:
            if (bat.xPos + bat.width <= xCoord or # adventuer is to right of
                xCoord + self.width <= bat.xPos or # adventer is to left of
                yCoord + self.height <= bat.yPos or # adventurer is above
                bat.yPos + bat.height <= yCoord): # adventurer is below
                continue
            else:
                # Take damage from bat
                self.health -= bat.damage
                if (self.health <= 0):
                    self.die()
                return True
        return False

    def detect_health_pack(self, xCoord, yCoord):
        for health_pack in world.health_packs:
            if (health_pack.xPos + health_pack.width <= xCoord or # adventuer is to right of
                xCoord + self.width <= health_pack.xPos or # adventer is to left of
                yCoord + self.height <= health_pack.yPos or # adventurer is above
                health_pack.yPos + health_pack.height <= yCoord): # adventurer is below
                continue
            else:
                # Gain health from pack
                self.health += health_pack.healing
                health_pack.die()
                return True
                
    def detect_arrow_pack(self, xCoord, yCoord):
        for arrow_pack in world.arrow_packs:
            if (arrow_pack.xPos + arrow_pack.width <= xCoord or # adventuer is to right of
                xCoord + self.width <= arrow_pack.xPos or # adventer is to left of
                yCoord + self.height <= arrow_pack.yPos or # adventurer is above
                arrow_pack.yPos + arrow_pack.height <= yCoord): # adventurer is below
                continue
            else:
                # Gain arrows from pack
                self.arrow_count += arrow_pack.count
                arrow_pack.die()
                return True
    def detect_speed_pack(self, xCoord, yCoord):
        for speed_pack in world.speed_packs:
            if (speed_pack.xPos + speed_pack.width <= xCoord or # adventuer is to right of
                xCoord + self.width <= speed_pack.xPos or # adventer is to left of
                yCoord + self.height <= speed_pack.yPos or # adventurer is above
                speed_pack.yPos + speed_pack.height <= yCoord): # adventurer is below
                continue
            else:
                # Gain arrows from pack
                self.speed += speed_pack.boost
                speed_pack.die()
                return True

    def die(self):
        self.living = False

    def get_start_position(self):
        # Choose random room
        sRoom = world.rooms[randint(0, len(world.rooms) - 1)]
        # Fit hero into room
        while(True):
            self.xPos = randint(sRoom.xPos, sRoom.xPos + sRoom.width)
            self.yPos = randint(sRoom.yPos, sRoom.yPos + sRoom.height)   
            if (self.in_room(self.xPos, self.yPos, sRoom)):
                return
 
    def attack_projectile(self, direction):
        if (self.arrow_count > 0):      
            arrow = Arrow(self.xPos, self.yPos, direction)
            world.projectiles.append(arrow)
            self.arrow_count -= 1
        




















##### ------------------------------------------------------------------------- #####
##### ------------------------------------------------------------------------- #####
##### ------------------------------------------------------------------------- #####



class TrapDoor:
    def __init__(self, room):
        self.location = room.id
        self.destination = -1
        self.width = 20
        self.height = 20
        self.color = (0, 0, 0)
        self.xPos = randint(room.xPos, room.xPos + room.width - self.width)
        self.yPos = randint(room.yPos, room.yPos + room.height - self.height)  

    def render(self):
        if (self.destination):
            pygame.draw.rect(world.screen, self.color , pygame.Rect(self.xPos, self.yPos, self.width, self.height))

    def enter(self, character):
        if (not self.destination):
            return
        print('entering door from room ' + str(self.location) +  ' to room ' + str(self.destination))
        for room in world.rooms:
            if (room.id == self.destination):
                destinationRoom = room

        # Try rendering hero below door
        character.xPos = destinationRoom.door.xPos
        character.yPos = destinationRoom.door.yPos + destinationRoom.door.height + 10
        if (character.in_room(character.xPos, character.yPos, destinationRoom)):
            return
  
        # Try above
        character.xPos = destinationRoom.door.xPos
        character.yPos = destinationRoom.door.yPos - character.height - 10
        if (character.in_room(character.xPos, character.yPos,destinationRoom)):
            return

        # Try right
        character.xPos = destinationRoom.door.xPos + room.width + 10
        character.yPos = destinationRoom.door.yPos
        if (character.in_room(character.xPos, character.yPos,destinationRoom)):
            return

        # Try left
        character.xPos = destinationRoom.door.xPos - character.width - 10
        character.yPos = destinationRoom.door.yPos
        if (character.in_room(character.xPos, character.yPos,destinationRoom)):
            return







##### ------------------------------------------------------------------------- #####
##### ------------------------------------------------------------------------- #####
##### ------------------------------------------------------------------------- #####


class Room: 
    def __init__(self, wdth, hght, xPosition, yPosition):
        self.width = wdth
        self.height = hght
        self.color = (205,133,63)
        self.id = randint(0, 1000)
        self.xPos = xPosition
        self.yPos = yPosition
        self.door = TrapDoor(self)
    
    def render(self):
        pygame.draw.rect(world.screen, self.color , pygame.Rect(self.xPos, self.yPos, self.width, self.height))

    def pDimensions(self):
        print('\n')
        print('\n')
        print('(' + str(self.xPos) + ', ' + str(self.yPos) + ')  ---------- (' + str(self.xPos + self.width) + ', ' + str(self.yPos) + ') '  )
        print('\n')
        print('\n')
        print('(' + str(self.xPos) + ', ' + str(self.yPos + self.height) + ')  ---------- (' + str(self.xPos + self.width) + ', ' + str(self.yPos + self.height) + ') '  )

        print()
    

##### ------------------------------------------------------------------------- #####
##### ------------------------------------------------------------------------- #####
##### ------------------------------------------------------------------------- #####
