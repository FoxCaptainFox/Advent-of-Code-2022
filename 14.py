from utils import read_data

def can_sand_be_placed_in_cave(filled_cave):
    max_depth = max([y for x, y in filled_cave.keys()])

    sand_x, sand_y = (500, 0)
    if (sand_x, sand_y) in filled_cave:
        return False
    filled_cave[(sand_x, sand_y)] = True

    while True:
        if sand_y > max_depth:
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
cave_is_filled = {}

for line in data:
    path = line.split(" -> ")
    for point_index in range(1, len(path)):
        point_1_x, point_1_y = [int(point_coordinate) for point_coordinate in path[point_index - 1].split(",")]
        point_2_x, point_2_y = [int(point_coordinate) for point_coordinate in path[point_index].split(",")]

        for x in range(min(point_1_x, point_2_x), max(point_1_x, point_2_x) + 1):
            for y in range(min(point_1_y, point_2_y), max(point_1_y, point_2_y) + 1):
                cave_is_filled[(x, y)] = True

grain_passed = 0
while can_sand_be_placed_in_cave(cave_is_filled):
    grain_passed += 1

print(grain_passed)
