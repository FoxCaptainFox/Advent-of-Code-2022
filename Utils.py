import os
import re

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))


def read_data(as_int=True, base=10, by_separate_characacters=False):
    result = []
    file_name = os.path.join(
        __location__, f"data.txt"
    )

    with open(file_name) as file:
        while line := file.readline():
            line = line.rstrip()

            if not as_int:
                result.append(line)
                continue

            if by_separate_characacters:
                number_list = line
            else:
                number_list = re.split("\W+", line)
            
            for number_as_str in number_list:
                try:
                    number = int(number_as_str, base)
                    result.append(number)
                except ValueError:
                    result.append(None)
    return result
