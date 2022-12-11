from functools import reduce
import math
import re
from utils import read_file


class Monkey(object):
    def __init__(self, id, items,
                 operation_left_part, operation_operator, operation_right_part,
                 test_divisor, positive_test_target_id, negative_test_target_id):
        self.id = id
        self.items = items
        self.operation_left_part = operation_left_part
        self.operation_operator = operation_operator
        self.operation_right_part = operation_right_part
        self.test_divisor = test_divisor
        self.positive_test_target_id = positive_test_target_id
        self.negative_test_target_id = negative_test_target_id
        self.inspection_number = 0

    def add_item(self, item):
        self.items.append(item)

    def inspect_items(self, decrease_worry):
        result = []
        for item in self.items:
            left_part = (item
                         if self.operation_left_part == "old"
                         else int(self.operation_left_part))
            right_part = (item
                          if self.operation_right_part == "old"
                          else int(self.operation_right_part))

            if self.operation_operator == "*":
                item = left_part * right_part
            elif self.operation_operator == "+":
                item = left_part + right_part
            else:
                raise ValueError(
                    f"Unexpected operator: {self.operation_operator}")

            if decrease_worry:
                item = math.floor(item / 3)

            target_id = (self.positive_test_target_id
                         if item % self.test_divisor == 0
                         else self.negative_test_target_id)

            result.append([target_id, item])
            self.inspection_number += 1

        self.items = []
        return result


def get_monkeys(monkey_data):
    monkeys_description = monkey_data.split("\n\n")
    monkey_regex = re.compile(r"""Monkey (\d+):
  Starting items: ([\d\,\ ]+)
  Operation: new = (old|\d+) (\*|\+) (old|\d+)
  Test: divisible by (\d+)
    If true: throw to monkey (\d+)
    If false: throw to monkey (\d+)""", re.MULTILINE)

    monkeys = []
    for monkey in monkeys_description:
        monkey_regex_match = re.match(monkey_regex, monkey)
        monkeys.append(Monkey(
            int(monkey_regex_match.group(1)),
            [int(x) for x in monkey_regex_match.group(2).split(", ")],
            monkey_regex_match.group(3),
            monkey_regex_match.group(4),
            monkey_regex_match.group(5),
            int(monkey_regex_match.group(6)),
            int(monkey_regex_match.group(7)),
            int(monkey_regex_match.group(8))
        ))
    return monkeys


def get_monkey_business_level(these_monkeys, round_number,
                              decrease_worry=True,
                              calculate_precise_worry=True):
    common_test_divisor = reduce(
        lambda x, y: x*y, [m.test_divisor for m in these_monkeys]
    )

    for _ in range(round_number):
        for monkey in these_monkeys:
            thrown_items = monkey.inspect_items(decrease_worry)
            for thrown_item in thrown_items:
                target_monkey = next((m for m in these_monkeys if m.id == thrown_item[0]), None)
                if target_monkey is None:
                    raise ValueError(f"No target monkey found with id = {thrown_item[0]}")

                thrown_item_value = (thrown_item[1] \
                                     if calculate_precise_worry \
                                     else thrown_item[1] % common_test_divisor)
                target_monkey.add_item(thrown_item_value)

    sorted_inspection_numbers = sorted([monkey.inspection_number for monkey in these_monkeys])
    return sorted_inspection_numbers[-1] * sorted_inspection_numbers[-2]


data = read_file(11)
print(get_monkey_business_level(get_monkeys(data), 20))
print(get_monkey_business_level(get_monkeys(data), 10000,
                                decrease_worry=False,
                                calculate_precise_worry=False))
