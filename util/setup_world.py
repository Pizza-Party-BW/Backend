from util.generator import MapWorld
from adventure.models import Player

new_map = MapWorld()
new_map.generate_map(10, 10)
for x in range(0, len(new_map.grid)):
    for y in range(0, len(new_map.grid[x])):
        room = new_map.grid[x][y]
        room.save()

players = Player.objects.all()
for p in players:
    p.currentRoom = new_map.grid[0][0].id
    p.save()
