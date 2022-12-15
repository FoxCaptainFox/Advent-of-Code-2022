import re
from utils import read_data

Y_TO_CHECK = 2000000

data = read_data(15)
readings = [[int(s) for s in re.findall(r'[-?\d]+', entry)] for entry in data]

beacon_at_y_to_check = {}
for reading in readings:
    sensor_x, sensor_y, beacon_x, beacon_y = reading
    if beacon_y == Y_TO_CHECK:
        beacon_at_y_to_check[beacon_x] = True
    reading_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    y_difference = abs(sensor_y - Y_TO_CHECK)
    if reading_distance < y_difference:
        continue
    x_difference = reading_distance - y_difference
    for x in range(sensor_x - x_difference, sensor_x + x_difference + 1):
        if x in beacon_at_y_to_check and beacon_at_y_to_check[x]:
            continue
        beacon_at_y_to_check[x] = False

print(list(beacon_at_y_to_check.values()).count(False))
