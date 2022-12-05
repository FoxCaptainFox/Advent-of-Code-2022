import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
DIRECTORY_NAME = "Data"


def read_data(file_number, output_type=str):
    result = []
    file_name = os.path.join(
        __location__, f"{DIRECTORY_NAME}/{format(file_number, '02d')}.txt"
    )

    with open(file_name) as file:
        while line := file.readline():
            line = line.rstrip()
            try:
                number = output_type(line)
                result.append(number)
            except ValueError:
                result.append(None)
    return result
