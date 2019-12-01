"""
Advent of code 2019: Day 1, task 1
"""
with open("input.txt", "r") as file:
    TOTAL_FUEL = 0
    for line in file:
        TOTAL_FUEL += float(line)//3 - 2
    print(f"Total fuel required: {TOTAL_FUEL}")
