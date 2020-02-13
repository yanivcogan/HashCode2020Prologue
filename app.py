from typing import List
import time
import numpy as np
import random


class Pizza:
    def __init__(self, index, size):
        self.index = index
        self.size = size


# OPENED_FILE = "./e_also_big.in"
OPENED_FILE = "./b_small.in"


def main():
    data = OPENED_FILE
    with open(data) as file:
        lines = file.readlines()
    first_line_parts = lines[0].split(' ')
    slices_to_order = int(first_line_parts[0])
    pizza_types = int(first_line_parts[1])
    pizza_sizes = np.array(lines[1].split(' '), dtype=int)
    pizzas = []
    for i, pizza in enumerate(pizza_sizes):
        pizzas.append(Pizza(i, pizza))
    fully_randomized(pizzas.copy())


def fully_randomized(slices_to_order, pizzas):
    current_size = 0

    while current_size<slices_to_order:
        pizza = random.choice(pizzas)
        if pizza + current_size <= slices_to_order:
            current_size += pizza
            sorted_sizes.remove(pizza)
            used_pizzas.add(pizza)
        else:
            break
    for pizza in sorted_sizes:
        if current_size + pizza <= slices_to_order:
            current_size += pizza
            used_pizzas.add(pizza)
    return used_pizzas


def write_output(output_name, pizzas):
    with open(output_name, 'w') as f:
        f.write(len(pizzas))
        f.write(str.join(' ', pizzas))


if __name__ == '__main__':
    main()
