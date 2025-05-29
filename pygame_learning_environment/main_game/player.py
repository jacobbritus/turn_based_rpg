import pygame

class Player:
    def __init__(self, sprite, pixels, spawn_coordinates, speed):
        self.sprite = sprite
        self.width = pixels
        self.height = pixels
        self.x = spawn_coordinates[0]
        self.y = spawn_coordinates[1]
        self.speed = speed
        self.direction = "down"


    # changes the player's coordinates on the screen
    def move(self, x, y, x_bounds, y_bounds):
        self.x += x * self.speed
        self.y += y * self.speed

        if self.x < 0:
            self.x = 0
        if self.y < 0:
            self.y = 0

        if self.x > x_bounds - self.width:
            self.x = x_bounds - self.width
        if self.y > y_bounds - self.height:
            self.y = y_bounds - self.height


    # makes the player move based on which key is pressed
    def controls(self, x_bounds, y_bounds):
        key_pressed = pygame.key.get_pressed()
        if key_pressed[pygame.K_w]:
            self.move(0, -1, x_bounds, y_bounds)
        if key_pressed[pygame.K_s]:
            self.move(0, 1, x_bounds, y_bounds)
        if key_pressed[pygame.K_a]:
            self.move(-1, 0, x_bounds, y_bounds)
        if key_pressed[pygame.K_d]:
            self.move(1, 0, x_bounds, y_bounds)


    def draw_player(self, window):
        window.blit(self.sprite, (self.x, self.y))



