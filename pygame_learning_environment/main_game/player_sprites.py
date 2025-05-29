import pygame

pygame.init()

window_width = 800
window_height = 600
tile_set_width = 128
tile_set_height = 192

sprite_width = 32
sprite_height = 48
x = 0
y = 0

window = pygame.display.set_mode((window_width, window_height))

player_actions = {
    0: [], #down
    1: [], #left
    2: [], #right
    3: [], #up


}
tile_set = pygame.image.load("bug_catcher.png")

rect = pygame.Rect(x, y, sprite_width, sprite_height)
sprite = tile_set.subsurface(rect)

for row_index in range(tile_set_width // sprite_width):
    for column_index in range(tile_set_height // sprite_height):
        rect = pygame.Rect(x, y, sprite_width, sprite_height)
        sprite = tile_set.subsurface(rect)

        player_actions[row_index].append(sprite)







        print(x, y, sprite_width, sprite_height)
        x += 32


    y += 48
    x = 0

print(player_actions)


player_image = player_actions[0][1]


player_x = 0
player_y = 0

while True:
    window.fill((255, 255, 255))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()




    window.blit(player_image, (player_x, player_y))
    pygame.display.update()
