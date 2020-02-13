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
    chosen_indices = fully_randomized(slices_to_order, pizzas.copy())
    write_output('./outputs' + data + '.out', chosen_indices)


def fully_randomized(slices_to_order, pizzas):
    current_size = 0
    chosen_indices = []
    while current_size < slices_to_order:
        pizza = random.choice(pizzas)
        if pizza.size + current_size <= slices_to_order:
            current_size += pizza.size
            chosen_indices.append(pizza.index)
            pizzas.remove(pizza)
        else:
            break
    sorted_pizzas = sorted(pizzas, key=lambda x: x.size)
    for pizza in sorted_pizzas:
        if current_size + pizza.size <= slices_to_order:
            current_size += pizza.size
            chosen_indices.append(pizza.index)
    return chosen_indices


def write_output(output_name, pizzas):
    with open(output_name, 'w') as f:
        f.write(str(len(pizzas)) + '\n')
        f.write(str.join(' ', [str(pizza) for pizza in pizzas]))


if __name__ == '__main__':
    main()
