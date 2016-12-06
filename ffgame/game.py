import pygame
from pygame.locals import *
from sys import exit

game_title = 'FF GAME'
res = 800, 600
background_image_filename = 'images/medieval.jpg'
mouse_image_filename = 'images/mouse_cursor.png'

pygame.init()

screen = pygame.display.set_mode(res, 0, 32)
pygame.display.set_caption(game_title)

my_font = pygame.font.SysFont('Arial', 16)

options = {1: 'Create Adventure', 2: 'Create Character', 3: 'Create Party'}

white = (255, 255, 255)
black = (0, 0, 0, 0)

for option in options:
    name_surface = my_font.render(options[option].upper(), True, white, black)
    pygame.image.save(name_surface,
                      'images/options/{option}.png'.format(option=options[option]).lower().replace(' ', '_'))

create_party_filename = 'images/options/create_party.png'
create_adventure_filename = 'images/options/create_adventure.png'
create_character_filename = 'images/options/create_character.png'

background = pygame.image.load(background_image_filename).convert()
mouse_cursor = pygame.image.load(mouse_image_filename).convert_alpha()
create_party = pygame.image.load(create_party_filename).convert_alpha()
create_adventure = pygame.image.load(create_adventure_filename).convert_alpha()
create_character = pygame.image.load(create_character_filename).convert_alpha()

while True:

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            exit()

        screen.blit(background, (0, 0))
        create_adventure_option = screen.blit(create_adventure, (20, 500))
        screen.blit(create_party, (20, 522))
        screen.blit(create_character, (20, 544))

        x, y = pygame.mouse.get_pos()
        x -= mouse_cursor.get_width() / 2
        y -= mouse_cursor.get_height() / 2
        screen.blit(mouse_cursor, (x, y))

    pygame.display.update()
