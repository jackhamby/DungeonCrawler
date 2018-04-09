import settings, characters, math
from random import *
import pygame, time
# INPUT: 2 Room objects, room1 and room2
# OUTPUT: a boolean, True if the rooms
# do not overlap, False if otherwise
def validRooms(room1, room2):

    if (room1.xPos > room2.xPos + room2.width or # to the right of
        room2.xPos > room1.xPos + room1.width or # to the let of
        room1.yPos > room2.yPos + room2.height or #below
        room2.yPos > room1.yPos + room1.height): # above
        return True
    else:
        return False


# INPUT: none
# OUTPUT: a Room object that lies within
# the boundary of the screen
def generateRoom():
    width = randint(100, 600)
    height = randint(100, 600)
    return characters.Room(width, height, randint(0, settings.screenWidth - width), randint(0, settings.screenHeight - height))


def generate_health_packs():
    health_packs = []
    health_pack_count = math.ceil(settings.level / 2)
    for i in range(0, health_pack_count):
        health_packs.append(characters.HealthPack())
    return health_packs

def generate_arrow_packs():
    arrow_packs = []
    arrow_pack_count = math.ceil((settings.level + 1) / 2)
    for i in range(0, arrow_pack_count):
        arrow_packs.append(characters.ArrowPack())
    return arrow_packs

def generate_speed_packs():
    speed_packs = []
    speed_pack_count = math.ceil((settings.level + 1) / 2)
    for i in range(0, speed_pack_count):
        speed_packs.append(characters.SpeedPack())
    return speed_packs



# INPUT: none
# OUTPUT: a list of Room objects with no
# overlapping rooms
def generateRooms():
    # Generate roomCount rooms
    rooms = []
    k = 0
    attempts = 10000
    while( k < settings.roomCount):
        print('attempting ' + str(attempts))
        if (attempts < 0):
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            print('\n')
            print('FAILED NUMBER OF ATTEMPTS' + str(attempts))
            return generateRooms()
        # Generating the first room
        if (len(rooms) == 0):
            room = generateRoom()
            rooms.append(room)
            # print('appended room: 0, id: '+ str(room.id))
            k += 1

        # Generating later rooms
        else:
            room = generateRoom()
            attempts -= 1
            prevRoomCount = len(rooms)
            for i in range(0, prevRoomCount):
                rm = rooms[i]
                # print('COMPARING, id: ' + str(rm.id) + 'id: ' + str(room.id) )
                
                if (not validRooms(rm, room)):
                    # print('room count: ' + str(len(rooms)))
                    # print('INVALID, id: ' + str(rm.id) + 'id: ' + str(room.id) )
                    break

                else:
                    # print('VALID, id: ' + str(room.id) )
                    # print('room count: ' + str(len(rooms)))

                    if (i == prevRoomCount - 1):
                        rooms.append(room)
                        k += 1

    roomIds = []
    for room in rooms:
        roomIds.append(room.id)
    shuffle(roomIds)
    for i, room in enumerate(rooms):
        if (i == len(rooms) - 1):
            room.door.destination = rooms[0].id
        else:
            # print('searching for door ' + str(i))
            room.door.destination = rooms[i + 1].id
    return rooms


    # adventurer = Adventurer()
