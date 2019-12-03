"""
Advent of code 2019: Day 2, task 2
"""

import numpy as np

file = open("input.txt", "r")
file = np.array(file.readlines()[0].split(",")).astype("int")

file_cpy = file.copy()
last_output = 0

for noun in range(0, 100):
    for verb in range(0, 100):
        ptr = 0
        file = file_cpy.copy()
        file[1] = noun
        file[2] = verb
        while True:
            if file[ptr] == 1:
                file[file[ptr + 3]] = file[file[ptr + 1]] + file[file[ptr + 2]]
            elif file[ptr] == 2:
                file[file[ptr + 3]] = file[file[ptr + 1]] * file[file[ptr + 2]]
            elif file[ptr] == 99:
                print("Halt code reached. Finished with:")
                last_output = file[0]
                print(f"@ ptr: {100 * noun + verb}")
                if last_output == 19690720:
                    print(noun * 100 + verb)
                    exit()
                break
            else:
                raise Exception("Opcode error!")
            ptr += 4
print("List exceeded")
