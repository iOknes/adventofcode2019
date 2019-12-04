"""
Advent of Code 2019: Day 3, task 1
"""

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

path_1 = set(create_path(inst_1))
path_2 = set(create_path(inst_2))
intersect = list(path_1.intersection(path_2))
#print(intersect)
for i in range(len(intersect)):
    intersect[i] = cab_dist(intersect[i])
intersect.sort()

print(intersect[2])
