from Utils import read_data
import numpy as np


def get_common_item_priority_sum(groups):
    common_items = [
        list(set.intersection(*[set(list) for list in group]))[0] for group in groups
    ]
    common_item_priorities = [
        ord(badge) - 96 if badge.islower()  # a -> 1,  z- > 26
        else ord(badge) - 38                # A -> 27, Z -> 52
        for badge in common_items
    ]
    return sum(common_item_priorities)


backpacks = read_data(as_int=False)

backpacks_sections = [
    [backpack[: len(backpack) // 2], backpack[len(backpack) // 2 :]]
    for backpack in backpacks
]
print(get_common_item_priority_sum(backpacks_sections))

groups_backpacks = np.array(backpacks).reshape(-1, 3)
print(get_common_item_priority_sum(groups_backpacks))
