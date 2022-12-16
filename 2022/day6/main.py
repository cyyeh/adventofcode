# https://adventofcode.com/2022/day/6


def has_marker(buffer: str) -> bool:
    if len(set(buffer)) == len(buffer):
        return True

    return False

result = -1

with open('input.txt') as f:
    chars = f.read()
    buffer = chars[:4]

    if has_marker(buffer):
        result = 4

    if result == -1:
        for (i, char) in enumerate(chars[4:]):
            buffer = buffer[1:] + char
            if has_marker(buffer):
                result = i + 4 + 1
                break

# part 1: How many characters need to be processed before the first start-of-packet marker is detected?
print(result)


result = -1

with open('input.txt') as f:
    chars = f.read()
    buffer = chars[:14]

    if has_marker(buffer):
        result = 14

    if result == -1:
        for (i, char) in enumerate(chars[14:]):
            buffer = buffer[1:] + char
            if has_marker(buffer):
                result = i + 14 + 1
                break

# part 2: How many characters need to be processed before the first start-of-message marker is detected?
print(result)