import os

__location__ = os.path.realpath(os.path.join(os.getcwd(), os.path.dirname(__file__)))
DIRECTORY_NAME = "Data"

def _convert_value(value, output_type):
    try:
        return output_type(value)
    except ValueError:
        return None

def read_data(file_number, output_type=str, as_separate_characters=False):
    result = []
    file_name = os.path.join(
        __location__, f"{DIRECTORY_NAME}/{format(file_number, '02d')}.txt"
    )

    with open(file_name) as file:
        while line := file.readline():
            line = line.rstrip()
            if as_separate_characters:
                result.append([_convert_value(ch, output_type) for ch in line])
            else:
                result.append(_convert_value(line, output_type))
    return result
