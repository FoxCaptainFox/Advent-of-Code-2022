from Utils import read_data

def calculate_points_1(description):
    shape_2 = description.split(" ")[1]
    if shape_2 == "X":
        result = 1
    elif shape_2 == "Y":
        result = 2
    elif shape_2 == "Z":
        result = 3
    
    if description == "A X" or description == "B Y" or description == "C Z":
        result += 3
    elif  description == "A Y" or description == "B Z" or description == "C X":
        result += 6

    return result

def calculate_points_2(description):
    shape_1 = description.split(" ")[0]
    if shape_1 == "A":
        result = 2
    elif shape_1 == "B":
        result = 3
    elif shape_1 == "C":
        result = 1
    
    shape_2 = description.split(" ")[1]
    if shape_2 == "Y":
        result += 3
    elif shape_2 == "Z":
        result += 6
    
    return result


data = read_data(2, as_int=False)
print(sum([calculate_points_1(x) for x in data]))
print([calculate_points_2(x) for x in data])
