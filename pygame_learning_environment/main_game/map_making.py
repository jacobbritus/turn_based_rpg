import pygame

# converting png_tilesets into usable ones
tileset = pygame.image.load("grass_tileset.png")
rect = pygame.Rect(0, 0, 16, 16)
grass_tile = tileset.subsurface(rect)

grass_tile_set = {
    "GRASS": {
        "image":grass_tile,
        "collision":False
    }
}

def grass_map(tiles_wide, tiles_high):
    map_grid = []
    for i in range(tiles_high + 1):
        map_grid.append((["GRASS"] * tiles_wide))

    return map_grid