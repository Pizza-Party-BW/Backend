# from adventure.models import Room
import random


class Map:
    def __init__(self):
        self.grid = []
        self.width = 0
        self.height = 0

    def __repr__(self):
        str = '__' * (self.width - 1)
        str += '\n'
        for y in range(self.height - 1, 0, -1):
            for x in range(0, self.width - 1):
                # if self.grid[x][y].w_to == 0: str += '|'
                # else: str += ' '
                # if self.grid[x][y].n_to == 0: str += '-'
                # else: str += ' '
                if x < 1: str += '|'
                if self.grid[x][y].s_to == 0: str += '_'
                else: str += ' '
                if self.grid[x][y].e_to == 0: str += '|'
                else: str += ' '
            str += '\n'
        return str

    def connected(self, room):
        connected = False
        if room.n_to: connected = True
        if room.s_to: connected = True
        if room.w_to: connected = True
        if room.e_to: connected = True
        return connected

    def find_neighbors(self, room):
        delta = [('w', (-1, 0)),
                 ('e', (1, 0)),
                 ('s', (0, -1)),
                 ('n', (0, 1))
                 ]
        neighbors = []
        for direction, (dx, dy) in delta:
            x2, y2 = room.x + dx, room.y + dy
            if (0 <= x2 < self.width) and (0 <= y2 < self.height):
                neighbor = self.grid[x2][y2]
                if not self.connected(neighbor):
                    neighbors.append((direction, neighbor))
        return neighbors

    def generate_map(self, width, height):
        if width < 1 or height < 1: return False
        from adventure.models import Room
        import random
        self.width = width
        self.height = height
        self.grid = [[Room(x=x, y=y) for y in range(self.height)] for x in range(self.width)]
        # self.grid = [None] * (self.width - 1)
        # for x in range(0, self.width): # fill out the height for every x position, giving you an x,y schema
        #     self.grid[x] = [Room()] * (self.height - 1)
        n = self.width * self.height
        # random starting place
        ix, iy = random.randrange(0, self.width - 1), random.randrange(0, self.height - 1)
        room_stack = []
        current = self.grid[ix][iy]
        nv = 1
        reverse_direction = {'n': 's', 's': 'n', 'w': 'e', 'e': 'w'}
        while nv < n:
            neighbors = self.find_neighbors(current)
            if not neighbors:
                current = room_stack.pop()
                continue

            direction, next = random.choice(neighbors)
            setattr(current, f'{direction}_to', next)
            setattr(next, f'{reverse_direction[direction]}_to', current)
            room_stack.append(current)
            current = next
            nv += 1


map = Map()
map.generate_map(50, 10)
print(map)
