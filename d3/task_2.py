"""
Advent of Code 2019: Day 3, task 2
"""

import numpy as np

X_MOVE = complex(1, 0)
Y_MOVE = complex(0, 1)

def create_path(inst_list):
    path = [complex(0, 0)]
    for i in inst_list:
        if i[0] == "R":
            for j in range(int(i[1:])):
                path.append(path[-1] + X_MOVE)
        if i[0] == "L":
            for j in range(int(i[1:])):
                path.append(path[-1] - X_MOVE)
        if i[0] == "U":
            for j in range(int(i[1:])):
                path.append(path[-1] + Y_MOVE)
        if i[0] == "D":
            for j in range(int(i[1:])):
                path.append(path[-1] - Y_MOVE)
        #print(f"{i.strip():4s} -> {path[-1]}")
    #print("Path done")
    return path

def cab_dist(cpx_num):
    return abs(cpx_num.real) + abs(cpx_num.imag)

infile = open("input.txt", "r")
inst_1 = infile.readline().split(",")
inst_2 = infile.readline().split(",")

path_1 = create_path(inst_1)
path_2 = create_path(inst_2)
path_set_1 = set(path_1)
path_set_2 = set(path_2)
intersect = list(path_set_1.intersection(path_set_2))

print(intersect)
#print(path_1)
#print(path_2)
path_lengths = []
for i in intersect:
    lens = [path_1.index(i), path_2.index(i)]
    print(lens)
    path_lengths.append(sum(lens))
path_lengths.sort()

print(path_lengths)
