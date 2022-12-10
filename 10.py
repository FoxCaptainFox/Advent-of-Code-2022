from utils import read_data

SPRITE_LENGTH = 3
LIT_PIXEL = "█"
DARK_PIXEL = " "

data = read_data(10)
x = 1
cycle_number = 0
signal_strength_sum = 0
screen_content = ""

for instruction in data:
    if instruction == "noop":
        instruction_cycles = 1
        instruction_v = 0
    elif instruction.split(" ")[0] == "addx":
        instruction_cycles = 2
        instruction_v = int(instruction.split(" ")[1])
    else:
        raise ValueError(f"Unsupported instruction: {instruction}")

    for i in range(1, instruction_cycles + 1):
        cycle_number += 1

        if cycle_number % 40 == 20:
            signal_strength_sum += x * cycle_number

        screen_content += LIT_PIXEL \
                          if x <= (cycle_number) % 40 <= x + SPRITE_LENGTH - 1 \
                          else DARK_PIXEL
        if cycle_number % 40 == 0:
            screen_content += "\n"

    x += instruction_v

print(signal_strength_sum)
print(screen_content)
