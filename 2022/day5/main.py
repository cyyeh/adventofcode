# https://adventofcode.com/2022/day/5


stacks = None

def create_stacks(line: list[str], stacks: list[list[str]]) -> list[list[str]]:
    i_th = 0
    for (i, char) in enumerate(line):
        if char.isalpha():
            stacks[i_th].append(char)
        if (i + 1) % 4 == 0:
            i_th += 1

    return stacks

def parse_strategy(strategy: list[str]) -> tuple[int]:
    crate_num = int(strategy[1])
    source_stack_idx = int(strategy[3]) - 1
    dest_stack_idx = int(strategy[5]) - 1

    return (crate_num, source_stack_idx, dest_stack_idx)

def execute_strategy(stacks: list[list[str]], crate_num: int, source_stack_idx: int, dest_stack_idx: int) -> list[list[str]]:
    moved_crates = []
    for _ in range(crate_num):
        moved_crates.append(stacks[source_stack_idx].pop())
    stacks[dest_stack_idx] += moved_crates

    return stacks

def get_top_crates(stacks: list[list[str]]) -> str:
    top_crates = ''
    for stack in stacks:
        top_crates += stack[-1]
    return top_crates

with open('input.txt') as f:
    for line in f.readlines():
        if 'move' not in line:
            if stacks is None:
                stacks = [[] for _ in range((len(line) + 1) // 4)]
            stacks = create_stacks(list(line), stacks)

            if line == '\n':
                stacks = [list(reversed(stack)) for stack in stacks]
        else:
            strategy = line.split(' ')
            crate_num, source_stack_idx, dest_stack_idx = parse_strategy(strategy)
            stacks = execute_strategy(stacks, crate_num, source_stack_idx, dest_stack_idx)
    top_crates = get_top_crates(stacks)

# part 1: After the rearrangement procedure completes, what crate ends up on top of each stack?
print(top_crates)

def execute_strategy_v2(stacks: list[list[str]], crate_num: int, source_stack_idx: int, dest_stack_idx: int) -> list[list[str]]:
    moved_crates = stacks[source_stack_idx][-crate_num:]
    stacks[source_stack_idx] = stacks[source_stack_idx][:-crate_num]
    stacks[dest_stack_idx] += moved_crates

    return stacks

stacks = None

with open('input.txt') as f:
    for line in f.readlines():
        if 'move' not in line:
            if stacks is None:
                stacks = [[] for _ in range((len(line) + 1) // 4)]
            stacks = create_stacks(list(line), stacks)

            if line == '\n':
                stacks = [list(reversed(stack)) for stack in stacks]
        else:
            strategy = line.split(' ')
            crate_num, source_stack_idx, dest_stack_idx = parse_strategy(strategy)
            stacks = execute_strategy_v2(stacks, crate_num, source_stack_idx, dest_stack_idx)
    top_crates = get_top_crates(stacks)

# part 2: After the rearrangement procedure completes, what crate ends up on top of each stack?
print(top_crates)