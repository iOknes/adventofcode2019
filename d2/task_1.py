"""
Advent of code 2019: Day 2, task 1
"""

import numpy as np

file = open("input.txt", "r")
file = np.array(file.readlines()[0].split(",")).astype("int")

file[1] = 12
file[2] = 2

ptr = 0

while True:
    print(ptr)
    if file[ptr] == 1:
        file[file[ptr + 3]] = file[file[ptr + 1]] + file[file[ptr + 2]]
        ptr += 4
    elif file[ptr] == 2:
        file[file[ptr + 3]] = file[file[ptr + 1]] * file[file[ptr + 2]]
        ptr += 4
    elif file[ptr] == 99:
        print("Halt code reached. Finished with:")
        print(file[0])
        exit()
    else:
        raise Exception("Opcode error!")
