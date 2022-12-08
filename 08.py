import numpy as np
from utils import read_data


def get_viewing_distance(trees, viewing_height):
    return min([index for index, height in enumerate(trees, start=1) if height >= viewing_height], default=len(trees))


data = np.array(read_data(8, output_type=int, as_separate_characters=True))

is_tree_visible = np.full_like(data, False)
for i in range(len(data)):
    for j in range(len(data[0])):
        is_tree_visible[i, j] = np.all(data[:i, j] < data[i, j]) or \
                                np.all(data[i + 1:, j] < data[i, j]) or \
                                np.all(data[i, :j] < data[i, j]) or \
                                np.all(data[i, j + 1:] < data[i, j])

print(np.concatenate(is_tree_visible).sum())

scenic_scores = np.full_like(data, 0)
for i in range(len(data)):
    for j in range(len(data[0])):
        scenic_scores[i, j] = get_viewing_distance(list(reversed(data[:i, j])), data[i, j]) * \
                              get_viewing_distance(data[i + 1:, j], data[i, j]) * \
                              get_viewing_distance(list(reversed(data[i, :j])), data[i, j]) * \
                              get_viewing_distance(data[i, j + 1:], data[i, j])
print(np.max(scenic_scores))
