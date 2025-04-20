'''Write a Python program that writes out a table of the function 
sin(x) vs. x, where x is tabulated between 0 and 2 with a thousand 
entries. Follow the basic Python program structure, including a main 
program function.
'''

import math
from tabulate import tabulate

def main():
    num_entries = 1000
    x_start = 0
    x_end = 2
    step = (x_end - x_start) / (num_entries - 1)

    table = []

    for i in range(num_entries):
        x = x_start + i * step
        sin_x = math.sin(x)
        table.append([round(x, 6), round(sin_x, 6)])

    headers = ["x", "sin(x)"]
    print(tabulate(table, headers=headers, tablefmt="grid"))

if __name__ == "__main__":
    main()