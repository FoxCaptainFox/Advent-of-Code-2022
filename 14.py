from utils import read_data

def can_sand_be_placed_in_cave(filled_cave, max_depth, floor_exists=False):
    sand_x, sand_y = (500, 0)
    if (sand_x, sand_y) in filled_cave:
        return False
    filled_cave[(sand_x, sand_y)] = True

    while True:
        if sand_y == max_depth:
            if floor_exists:
                return True
            del filled_cave[(sand_x, sand_y)]
            return False
        if (sand_x, sand_y + 1) not in filled_cave:
            del filled_cave[(sand_x, sand_y)]
            sand_x, sand_y = sand_x, sand_y + 1
            filled_cave[(sand_x, sand_y)] = True
            continue
        if (sand_x - 1, sand_y + 1) not in filled_cave:
            del filled_cave[(sand_x, sand_y)]
            sand_x, sand_y = sand_x - 1, sand_y + 1
            filled_cave[(sand_x, sand_y)] = True
            continue
        if (sand_x + 1, sand_y + 1) not in filled_cave:
            del filled_cave[(sand_x, sand_y)]
            sand_x, sand_y = sand_x + 1, sand_y + 1
            filled_cave[(sand_x, sand_y)] = True
            continue
        return True


data = read_data(14)
filled_cave = {}

for line in data:
    path = line.split(" -> ")
    for point_index in range(1, len(path)):
        point_1_x, point_1_y = [int(point_coordinate) for point_coordinate in path[point_index - 1].split(",")]
        point_2_x, point_2_y = [int(point_coordinate) for point_coordinate in path[point_index].split(",")]

        for x in range(min(point_1_x, point_2_x), max(point_1_x, point_2_x) + 1):
            for y in range(min(point_1_y, point_2_y), max(point_1_y, point_2_y) + 1):
                filled_cave[(x, y)] = True

depth_to_check = max([y for x, y in filled_cave.keys()]) + 1

sand_placed = 0
cave_1 = filled_cave.copy()
while can_sand_be_placed_in_cave(cave_1, depth_to_check):
    sand_placed += 1
print(sand_placed)

cave_2 = filled_cave.copy()
sand_placed = 0
while can_sand_be_placed_in_cave(cave_2, depth_to_check, True):
    sand_placed += 1
print(sand_placed)
