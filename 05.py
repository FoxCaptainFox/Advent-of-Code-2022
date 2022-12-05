from itertools import zip_longest
import re
import copy
from utils import read_data

data = read_data(5)
data_separator_index = data.index('')

crates_data = [list(x) for x in data[:data_separator_index - 1]]
crates_data_transposed_filtered_and_reversed = [
    list(filter(lambda j: j is not None and j != " ", i))[::-1]
    for i in zip_longest(*crates_data)
]
crates_stacks_1 = crates_data_transposed_filtered_and_reversed[1::4]
crates_stacks_2 = copy.deepcopy(crates_stacks_1)

for instruction_line in data[data_separator_index + 1:]:
    instruction = [int(number) for number
        in re.split("move | from | to ", instruction_line) if number != '']

    for _ in range(instruction[0]):
        crate = crates_stacks_1[instruction[1] - 1].pop()
        crates_stacks_1[instruction[2] - 1].append(crate)

    crates = crates_stacks_2[instruction[1] - 1][-instruction[0]:]
    del crates_stacks_2[instruction[1] - 1][-instruction[0]:]
    crates_stacks_2[instruction[2] - 1] += crates

print(''.join([stack[-1] for stack in crates_stacks_1]))
print(''.join([stack[-1] for stack in crates_stacks_2]))
