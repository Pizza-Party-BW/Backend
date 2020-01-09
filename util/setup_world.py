from util.generator import MapWorld
from adventure.models import Player

new_map = MapWorld()
new_map.generate_map(10, 10)
print(new_map)
players = Player.objects.all()
for p in players:
    p.currentRoom = new_map.grid[0][0].id
    p.save()
