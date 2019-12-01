"""
Advent of code 2019: Day 1, task 2
"""
with open("input.txt", "r") as file:
    TOTAL_FUEL = 0
    for line in file:
        MASS = float(line)
        NEXT_FUEL = MASS // 3 - 2
        TOTAL_FUEL += NEXT_FUEL
        while NEXT_FUEL > 0:
            NEXT_FUEL = NEXT_FUEL // 3 - 2
            if NEXT_FUEL >= 0:
                TOTAL_FUEL += NEXT_FUEL
    print(f"Total fuel required: {TOTAL_FUEL}")
