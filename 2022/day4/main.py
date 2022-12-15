# https://adventofcode.com/2022/day/4


def assign_sections(line: str) -> list[tuple[int]]:
    first_section, second_section = line.split(',')
    return [
        tuple(map(int, first_section.split('-'))),
        tuple(map(int, second_section.split('-')))
    ]

def is_fully_contained(first: tuple[int], second: tuple[int]) -> bool:
    if (
        second[0] <= first[0] <= second[1] and
        second[0] <= first[1] <= second[1]
    ) or (
        first[0] <= second[0] <= first[1] and
        first[0] <= second[1] <= first[1]
    ):
        return True

    return False

def is_overlapped(first: tuple[int], second: tuple[int]) -> bool:
    if is_fully_contained(first, second):
        return True
    elif (
        second[1] >= first[1] >= second[0]
    ) or (
        first[0] <= second[1] <= first[1]
    ):
        return True

    return False

fully_contained_pairs = 0

with open('input.txt') as f:
    for line in f.readlines():
        first_sections, second_sections = assign_sections(line.strip())
        if is_fully_contained(first_sections, second_sections):
            fully_contained_pairs += 1

# part 1: In how many assignment pairs does one range fully contain the other?
print(fully_contained_pairs)


overlapped_pairs = 0

with open('input.txt') as f:
    for line in f.readlines():
        first_sections, second_sections = assign_sections(line.strip())
        if is_overlapped(first_sections, second_sections):
            overlapped_pairs += 1

# part2: In how many assignment pairs do the ranges overlap?
print(overlapped_pairs)