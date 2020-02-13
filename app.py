from typing import List
import time
import numpy as np
import random


class Pizza:
    def __init__(self, index, size):
        self.index = index
        self.size = size


# OPENED_FILE = "./a_example.in"
# OPENED_FILE = "./b_small.in"
# OPENED_FILE = "./c_medium.in"
OPENED_FILE = "./d_quite_big.in"
# OPENED_FILE = "./e_also_big.in"
ALL_FILES = ["./a_example.in", "./b_small.in", "./c_medium.in", "./d_quite_big.in",
             "./e_also_big.in"]


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
    chosen_indices = throw_stuff_in_then_pull_stuff_out(slices_to_order, pizzas.copy())
    write_output('./outputs' + data.replace(".in", ".out"), chosen_indices)


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


def throw_stuff_in_then_pull_stuff_out(target: int, pizzas: List[Pizza]):
    best_solution = [0, set()]  # slice count, taken pizza indices
    current_solution = [0, set()]
    attempts = 0
    while attempts < 100_000:
        random_pizza: Pizza = random.choice(pizzas)
        together = current_solution[0] + random_pizza.size
        if together > target or random_pizza in current_solution[1]:
            attempts += 1
            if random.random() < 0.1:  # 10% chance
                # take out an existing pizza
                existing_pizza: Pizza = random.choice(tuple(current_solution[1]))
                current_solution[1].remove(existing_pizza)
                current_solution[0] -= existing_pizza.size
            continue
        current_solution[0] = together
        current_solution[1].add(random_pizza)
        if current_solution[0] > best_solution[0]:
            best_solution = current_solution
    print(f"got: {best_solution[0]}")
    return [p.index for p in best_solution[1]]


def write_output(output_name, pizzas):
    with open(output_name, 'w') as f:
        f.write(str(len(pizzas)) + '\n')
        f.write(str.join(' ', [str(pizza) for pizza in pizzas]))


if __name__ == '__main__':
    main()
