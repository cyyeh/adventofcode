# https://adventofcode.com/2022/day/1


calories_by_elves = []
calories = 0

with open('input.txt') as f:
    for line in f.readlines():
        if line == '\n':
            calories_by_elves.append(calories)
            calories = 0
        else:
            calories += int(line)

# part 1: Find the Elf carrying the most Calories. How many total Calories is that Elf carrying?
print(max(calories_by_elves))

# part 2: Find the top three Elves carrying the most Calories. How many Calories are those Elves carrying in total?
print(sum(sorted(calories_by_elves, reverse=True)[:3]))
