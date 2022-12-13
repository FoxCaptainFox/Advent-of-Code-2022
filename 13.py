import json
from utils import read_file

DECODER_1 = [[2]]
DECODER_2 = [[6]]


class PacketOrder:
    CORRECT_ORDER = 0
    INCORRECT_ORDER = 1
    UNKNOWN_ORDER = 2


def compare_packets(left, right):
    if isinstance(left, int) and isinstance(right, int):
        if left < right:
            return PacketOrder.CORRECT_ORDER
        if left > right:
            return PacketOrder.INCORRECT_ORDER
        else:
            return PacketOrder.UNKNOWN_ORDER

    if isinstance(left, int):
        left = [left]
    if isinstance(right, int):
        right = [right]

    min_length = min(len(left), len(right))
    for i in range(min_length):
        order_of_i_elements = compare_packets(left[i], right[i])
        if order_of_i_elements == PacketOrder.UNKNOWN_ORDER:
            continue
        else:
            return order_of_i_elements

    if len(left) < len(right):
        return PacketOrder.CORRECT_ORDER
    if len(left) > len(right):
        return PacketOrder.INCORRECT_ORDER
    else:
        return PacketOrder.UNKNOWN_ORDER


data = read_file(13)
packet_pairs = [
    [json.loads(pair_part) for pair_part in pair.split("\n")]
    for pair in data.split("\n\n")
]
result = 0
for pair_index in range(len(packet_pairs)):
    if (
        compare_packets(packet_pairs[pair_index][0], 
                        packet_pairs[pair_index][1])
        == PacketOrder.CORRECT_ORDER
    ):
        result += pair_index + 1

print(result)

packets = ([json.loads(line) for line in data.split("\n") if line != ""] +
           [DECODER_1, DECODER_2])
# Bubble sort
for i in range(len(packets)):
    for j in range(0, len(packets) - i - 1):
        order = compare_packets(packets[j], packets[j + 1])
        if (order == PacketOrder.INCORRECT_ORDER):
            packets[j], packets[j + 1] = (packets[j + 1], packets[j])

print((packets.index(DECODER_1) + 1) * (packets.index(DECODER_2) + 1))
