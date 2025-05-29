class Map:
    def __init__(self, tile_set, grid, tile_size):
        self.tile_set = tile_set
        self.grid = grid
        self.tile_size = tile_size

    def draw_map(self, window):

        for row_index, row in enumerate(self.grid):

            for column_index, tile in enumerate(row):
                window.blit(self.tile_set[tile]["image"], (column_index * self.tile_size, row_index * self.tile_size))