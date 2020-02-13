import numpy as np

if __name__ == '__main__':
    data = './e_also_big.in'
    with open(data, 'r') as f:
        lines = f.readlines()
    first_line_parts = lines[0].split(' ')
    slices_to_order = int(first_line_parts[0])
    pizza_types = int(first_line_parts[1])
    pizza_sizes = np.array(lines[1].split(' '), dtype=int)
    print(pizza_sizes)

def write_output(output_name, pizzas):
    with open(output_name, 'w') as f:
        f.write(len(pizzas))
        f.write(str.join(' ', pizzes))
