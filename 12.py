import itertools
import math
from utils import read_data

START_MARK = "S"
END_MARK = "E"
LOWEST_MARK = "a"


def get_indexes_2d(array_2d, search_value):
    result = []
    for row_index, row in enumerate(array_2d):
        if search_value in row:
            result.append((row_index, row.index(search_value)))
    return result


def get_passable_neighbors(heights, base_i, base_j):
    neighbors = [
        (base_i, base_j - 1),
        (base_i, base_j + 1),
        (base_i - 1, base_j),
        (base_i + 1, base_j),
    ]
    neighbors_inside_boundary = [
        (i, j) for i, j in neighbors
        if i >= 0 and i < len(heights) and j >= 0 and j < len(heights[0])
    ]
    return [
        (i, j) for i, j in neighbors_inside_boundary
        if heights[i][j] <= heights[base_i][base_j] + 1
    ]


def get_height(mark):
    if mark == START_MARK:
        return 1
    if mark == END_MARK:
        return 26
    return ord(mark) - 96  # a -> 1,  z- > 26


def get_distance(matrix, start_index_i, start_index_j, end_i, end_j):
    # Dijkstra's algorithm

    distance_grid = [[math.inf] * len(matrix[0]) for _ in range(len(matrix))]
    distance_grid[start_index_i][start_index_j] = 0
    queue = list(itertools.product(range(len(matrix)), range(len(matrix[0]))))

    while queue:
        minimum_distance_in_queue = min([distance_grid[i][j] for i, j in queue])
        current_i, current_j = [
            (i, j) for i, j in queue
            if distance_grid[i][j] == minimum_distance_in_queue
        ][0]
        queue.remove((current_i, current_j))

        neighbor_squares = get_passable_neighbors(matrix, current_i, current_j)
        neighbor_squares_in_queue = list(set(neighbor_squares).intersection(queue))

        for neighbor_square_i, neighbor_square_j in neighbor_squares_in_queue:
            old_distance = distance_grid[neighbor_square_i][neighbor_square_j]
            new_distance = distance_grid[current_i][current_j] + 1
            if (new_distance < old_distance):
                distance_grid[neighbor_square_i][neighbor_square_j] = new_distance

    return distance_grid[end_i][end_j]


data = read_data(12, as_separate_characters=True)
end_i, end_j = get_indexes_2d(data, END_MARK)[0]
heights = [[get_height(mark) for mark in mark_row] for mark_row in data]

start_mark_i, start_mark_j = get_indexes_2d(data, START_MARK)[0]
print(get_distance(heights, start_mark_i, start_mark_j, end_i, end_j))

distances_from_lowest_marks = [
    get_distance(heights, start_i, start_j, end_i, end_j)
    for start_i, start_j in get_indexes_2d(data, LOWEST_MARK)
]
print(min(distances_from_lowest_marks))
