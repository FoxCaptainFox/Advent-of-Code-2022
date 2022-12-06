import re
from utils import read_data

data = read_data(4)
complete_overlaps = partial_overlaps = 0
for record in data:
    start_1, end_1, start_2, end_2 = [int(number) for number in re.split(",|-", record)]
    if (start_1 <= start_2 <= end_2 <= end_1) or (start_2 <= start_1 <= end_1 <= end_2):
        complete_overlaps += 1
    if not (end_1 < start_2 or end_2 < start_1):
        partial_overlaps += 1

print(complete_overlaps)
print(partial_overlaps)
