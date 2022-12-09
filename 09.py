from utils import read_data

DIRECTION = {
    "U": [0, 1],
    "D": [0, -1],
    "L": [-1, 0],
    "R": [1, 0],
}


def get_route_length(commands, knot_number):
    rope_knot_coordinates = [[0, 0] for _ in range(knot_number)]
    tail_route = {tuple(rope_knot_coordinates[-1])}

    for command in commands:
        command_direction = DIRECTION[command.split(" ")[0]]
        command_length = int(command.split(" ")[1])

        for _ in range(command_length):
            rope_knot_coordinates[0] = [
                head_coordinate + change_by_coordinate
                for head_coordinate, change_by_coordinate
                in zip(rope_knot_coordinates[0], command_direction)
            ]
            for knot_index in range(1, len(rope_knot_coordinates)):
                potential_difference = [
                    this_knot_coordinate - previous_knot_coordinate
                    for this_knot_coordinate, previous_knot_coordinate
                    in zip(rope_knot_coordinates[knot_index], rope_knot_coordinates[knot_index-1])
                ]
                real_difference = [
                    0 if difference_by_coordinate == 0
                        or abs(difference_by_coordinate) < abs(max(potential_difference, key=abs))
                      else difference_by_coordinate / abs(difference_by_coordinate)
                    for difference_by_coordinate in potential_difference
                ]
                rope_knot_coordinates[knot_index] = [
                    previous_knot_coordinate + difference_by_coordinate
                    for previous_knot_coordinate, difference_by_coordinate
                    in zip(rope_knot_coordinates[knot_index-1], real_difference)
                ]
            tail_route.add(tuple(rope_knot_coordinates[-1]))

    return len(tail_route)


data = read_data(9)
print(get_route_length(data, 2))
print(get_route_length(data, 10))
