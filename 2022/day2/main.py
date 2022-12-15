# https://adventofcode.com/2022/day/2


def strategy_score(strategy: str) -> int:
    if strategy == 'X':  # Rock
        return 1
    elif strategy == 'Y':  # Paper
        return 2
    elif strategy == 'Z':  # Scissors
        return 3
    else:
        raise ValueError(f'Unknown strategy: {strategy}')

def round_score(your_strategy: str, opponent_strategy: str) -> int:
    if (
        (your_strategy == 'X' and opponent_strategy == 'C') or
        (your_strategy == 'Y' and opponent_strategy == 'A') or
        (your_strategy == 'Z' and opponent_strategy == 'B')
    ):
        return 6  # win
    elif (
        (your_strategy == 'X' and opponent_strategy == 'A') or
        (your_strategy == 'Y' and opponent_strategy == 'B') or
        (your_strategy == 'Z' and opponent_strategy == 'C')
    ):
        return 3  # draw
    else:
        return 0  # lost

score = 0

with open('input.txt') as f:
    for line in f.readlines():
        opponent_strategy, your_strategy = line.strip().split(' ')
        score += (
            strategy_score(your_strategy) +
            round_score(your_strategy, opponent_strategy)
        )

# part 1: What would your total score be if everything goes exactly according to your strategy guide?
print(score)


score = 0

def decrypt_strategy(round_result: str, opponent_strategy: str) -> str:
    if round_result == 'X':  # lost
        if opponent_strategy == 'A':
            return 'Z'
        elif opponent_strategy == 'B':
            return 'X'
        elif opponent_strategy == 'C':
            return 'Y'
        else:
            raise ValueError(f'Unknown opponent_strategy: {opponent_strategy}')
    elif round_result == 'Y':  # draw
        if opponent_strategy == 'A':
            return 'X'
        elif opponent_strategy == 'B':
            return 'Y'
        elif opponent_strategy == 'C':
            return 'Z'
        else:
            raise ValueError(f'Unknown opponent_strategy: {opponent_strategy}')
    elif round_result == 'Z':  # win
        if opponent_strategy == 'A':
            return 'Y'
        elif opponent_strategy == 'B':
            return 'Z'
        elif opponent_strategy == 'C':
            return 'X'
        else:
            raise ValueError(f'Unknown opponent_strategy: {opponent_strategy}')
    else:
        raise ValueError(f'Unknown round_result: {round_result}')

def round_score_v2(round_result) -> int:
    if round_result == 'X':
        return 0  # lost
    elif round_result == 'Y':
        return 3  # draw
    elif round_result == 'Z':
        return 6  # win
    else:
        raise ValueError(f'Unknown round_result: {round_result}')

with open('input.txt') as f:
    for line in f.readlines():
        opponent_strategy, round_result = line.strip().split(' ')
        score += (
            strategy_score(decrypt_strategy(round_result, opponent_strategy)) +
            round_score_v2(round_result)
        )

# part 2: Following the Elf's instructions for the second column, what would your total score be if everything goes exactly according to your strategy guide?
print(score)
