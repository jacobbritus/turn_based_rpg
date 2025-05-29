import pygame
from player import Player
from map import Map
from map_making import grass_map
from map_making import grass_tile_set

window_width = 600
window_height = 500
sprite_pixels = 64
tiles_wide = round(window_width / 16)
tiles_high = round(window_height / 16)

player = Player(
    sprite = pygame.transform.scale(pygame.image.load("caterpie.png"), (sprite_pixels, sprite_pixels)),
    pixels = sprite_pixels,
    spawn_coordinates= [0, 0],
    speed = 4

)
grass_overworld = Map(
    grass_tile_set,
    grass_map(tiles_wide, tiles_high),
    16
)



pygame.init()
window = pygame.display.set_mode((window_width, window_height))
clock = pygame.time.Clock()

while True:
    window.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()


    grass_overworld.draw_map(window)
    player.controls(window_width, window_height)

    player.draw_player(window)
    clock.tick(60)

    pygame.display.update()