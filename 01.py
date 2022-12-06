from utils import read_data

def get_top_n_elven_supplies_sum(data, n):
    summed_array = [0]
    for value in data:
        if value is None:
            summed_array.append(0)
        else:
            summed_array[-1] += value
    summed_array.sort()
    return sum(summed_array[-n:])


data = read_data(1, output_type=int)
print(get_top_n_elven_supplies_sum(data, 1))
print(get_top_n_elven_supplies_sum(data, 3))
