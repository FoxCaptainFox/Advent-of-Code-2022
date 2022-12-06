from utils import read_data


def get_message_start_index(data, sliding_window_size):
    for i in range(sliding_window_size, len(data)):
        sliding_window = data[i - sliding_window_size : i]
        if len(sliding_window) == len(set(sliding_window)):
            return i


data = read_data(6)[0]
print(get_message_start_index(data, 4))
print(get_message_start_index(data, 14))
