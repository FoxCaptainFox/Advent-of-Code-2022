import re
from utils import read_data

Y_TO_CHECK = 2000000

data = read_data(15)
readings = [[int(s) for s in re.findall(r'[-?\d]+', entry)] for entry in data]

# beacon_at_y_to_check = {}
# for reading in readings:
#     sensor_x, sensor_y, beacon_x, beacon_y = reading
#     if beacon_y == Y_TO_CHECK:
#         beacon_at_y_to_check[beacon_x] = True
#     reading_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
#     y_difference = abs(sensor_y - Y_TO_CHECK)
#     if reading_distance < y_difference:
#         continue
#     x_difference = reading_distance - y_difference
#     for position_x in range(sensor_x - x_difference, sensor_x + x_difference + 1):
#         if position_x in beacon_at_y_to_check and beacon_at_y_to_check[position_x]:
#             continue
#         beacon_at_y_to_check[position_x] = False
# 
# print(list(beacon_at_y_to_check.values()).count(False))


# foo = {}
# for reading_1 in readings:
#     sensor_x_1, sensor_y_1, beacon_x_1, beacon_y_1 = reading_1
#     reading_distance_1 = abs(sensor_x_1 - beacon_x_1) + abs(sensor_y_1 - beacon_y_1)
#     for reading_2 in readings:
#         sensor_x_2, sensor_y_2, beacon_x_2, beacon_y_2 = reading_2
#         reading_distance_2 = abs(sensor_x_2 - beacon_x_2) + abs(sensor_y_2 - beacon_y_2)
# 
#         distance_between_1_and_2 = abs(sensor_x_1 - sensor_x_2) + abs(sensor_y_1 - sensor_y_2)
#         if distance_between_1_and_2 == reading_distance_1 + reading_distance_2 + 1:
#             # add 1
#             for x_change in range( - reading_distance_1 - 1, sensor_x_1 + reading_distance_1 + 1 + 1):
#                 foo[(sensor_x_1 + x_change, sensor_y_1 + (reading_distance_1 - x_change))] = True
#                 foo[(sensor_x_1 + x_change, sensor_y_1 - (reading_distance_1 - x_change))] = True
#             # add 2

limit = 4000000
bar = set()
for reading in readings:
    sensor_x, sensor_y, beacon_x, beacon_y = reading
    reading_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
    for x_change in range( - reading_distance - 1, sensor_x + reading_distance + 1 + 1):
        position_x = sensor_x + x_change
        position_y_1 = sensor_y + (reading_distance - x_change)
        position_y_2 = sensor_y - (reading_distance - x_change)
        if 0 <= position_x <= limit and 0 <= position_y_1 <= limit:
            # bar.add((position_x, position_y_1))
            position_scanned = False
            for reading_2 in readings:
                sensor_x_2, sensor_y_2, beacon_x_2, beacon_y_2 = reading_2
                reading_distance_2 = abs(sensor_x_2 - beacon_x_2) + abs(sensor_y_2 - beacon_y_2)
                distance_from_sensor_to_position = abs(sensor_x_2 - position_x) + abs(sensor_y_2 - position_y_1)
                if distance_from_sensor_to_position <= reading_distance_2:
                    position_scanned = True
            if not position_scanned:
                print(f"Found {position_x} {position_y_1} {position_x * 4000000 + position_y_1}")
        if 0 <= position_x <= limit and 0 <= position_y_2 <= limit:
            # bar.add((position_x, position_y_2))
            position_scanned = False
            for reading_2 in readings:
                sensor_x_2, sensor_y_2, beacon_x_2, beacon_y_2 = reading_2
                reading_distance_2 = abs(sensor_x_2 - beacon_x_2) + abs(sensor_y_2 - beacon_y_2)
                distance_from_sensor_to_position = abs(sensor_x_2 - position_x) + abs(sensor_y_2 - position_y_2)
                if distance_from_sensor_to_position <= reading_distance_2:
                    position_scanned = True
            if not position_scanned:
                f = open("temp.txt", "a")
                f.write(f"Found {position_x} {position_y_2} {position_x * 4000000 + position_y_2}\n")
                f.close()
                print(f"Found {position_x} {position_y_2} {position_x * 4000000 + position_y_2}")

#for position_x, poistion_y in bar:
#    position_scanned = False
#    for reading in readings:
#        sensor_x, sensor_y, beacon_x, beacon_y = reading
#        reading_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
#        distance_from_sensor_to_position = abs(sensor_x - position_x) + abs(sensor_y - poistion_y)
#        if distance_from_sensor_to_position <= reading_distance:
#            position_scanned = True
#    if not position_scanned and 0 <= position_x <= limit and 0 <= poistion_y <= limit:
#        print(f"Found {position_x} {poistion_y} {position_x * 4000000 + poistion_y}")

print("You should see it")
# for position_y in range(LIMIT + 1):
#     print(f"Scanning y position {position_y}")
#     beacon_at_y_to_check = [None] * (LIMIT + 1)
#     for reading in readings:
#         sensor_x, sensor_y, beacon_x, beacon_y = reading
#         if beacon_y == position_y:
#             beacon_at_y_to_check[beacon_x] = True
#         reading_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
#         y_difference = abs(sensor_y - position_y)
#         if reading_distance < y_difference:
#             continue
#         x_difference = reading_distance - y_difference
#         for position_x in range(sensor_x - x_difference, sensor_x + x_difference + 1):
#             if LIMIT + 1 <= position_x:
#                 continue
#             if beacon_at_y_to_check[position_x]:
#                 continue
#             beacon_at_y_to_check[position_x] = False
#     if None in beacon_at_y_to_check:
#         print(f"Found {beacon_at_y_to_check.index(None)} {position_y}")
    

# for position_x in range(LIMIT + 1):
#     print(f"Scanning x position {position_x}")
#     for poistion_y in range(LIMIT + 1):
#         position_scanned = False
#         for reading in readings:
#             sensor_x, sensor_y, beacon_x, beacon_y = reading
#             reading_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
#             distance_from_sensor_to_position = abs(sensor_x - position_x) + abs(sensor_y - poistion_y)
#             if distance_from_sensor_to_position <= reading_distance:
#                 position_scanned = True
#         if not position_scanned:
#             print(f"Found {position_x} {poistion_y}")
# 
# 
# Matrix = [[None for _ in range(LIMIT)] for _ in range(LIMIT)]
# print("That's okay")
# for reading in readings:
#     sensor_x, sensor_y, beacon_x, beacon_y = reading
#     if beacon_y == Y_TO_CHECK:
#         beacon_at_y_to_check[beacon_x] = True
#     reading_distance = abs(sensor_x - beacon_x) + abs(sensor_y - beacon_y)
#     y_difference = abs(sensor_y - Y_TO_CHECK)
#     if reading_distance < y_difference:
#         continue
#     x_difference = reading_distance - y_difference
#     for position_x in range(sensor_x - x_difference, sensor_x + x_difference + 1):
#         if position_x in beacon_at_y_to_check and beacon_at_y_to_check[position_x]:
#             continue
#         beacon_at_y_to_check[position_x] = False
