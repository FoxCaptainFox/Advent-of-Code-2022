from Utils import read_data

def get_top_n_elven_supplies_sum(n):
    data = read_data()
    summed_array = [0]
    for value in data:
        if value is None:
            summed_array.append(0)
        else:
            summed_array[-1] += value
    summed_array.sort()
    return sum(summed_array[-n:])


print(get_top_n_elven_supplies_sum(1))
print(get_top_n_elven_supplies_sum(3))
