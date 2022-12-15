# https://adventofcode.com/2022/day/3

priorities = 0

def priority(item: str) -> int:
    if item.islower():
        return ord(item) - ord('a') + 1
    else:
        return ord(item) - ord('A') + 27

with open('input.txt') as f:
    for line in f.readlines():
        rucksack = list(line.strip())
        first_compartment, second_compartment = rucksack[:len(rucksack)//2], rucksack[len(rucksack)//2:]
        common_item = set(first_compartment).intersection(set(second_compartment))
        priorities += priority(next(iter(common_item)))

# part 1: Find the item type that appears in both compartments of each rucksack. What is the sum of the priorities of those item types?
print(priorities)


rucksacks = []
priorities = 0

with open('input.txt') as f:
    for (i, line) in enumerate(f.readlines()):
        rucksack = line.strip()
        rucksacks.append(set(rucksack))
        if (i + 1) % 3 == 0:
            common_item = rucksacks[0].intersection(rucksacks[1]).intersection(rucksacks[2])
            priorities += priority(next(iter(common_item)))

            rucksacks = []

# part 2: Find the item type that corresponds to the badges of each three-Elf group. What is the sum of the priorities of those item types?
print(priorities)