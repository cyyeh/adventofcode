# https://adventofcode.com/2022/day/6


def has_marker(buffer: str) -> bool:
    if len(set(buffer)) == len(buffer):
        return True

    return False

def processed_chars(marker_chars_num: int) -> int:
    result = -1
    with open('input.txt') as f:
        chars = f.read()
        buffer = chars[:marker_chars_num]

        if has_marker(buffer):
            result = marker_chars_num

        if result == -1:
            for (i, char) in enumerate(chars[marker_chars_num:]):
                buffer = buffer[1:] + char
                if has_marker(buffer):
                    result = i + marker_chars_num + 1
                    break
    return result

# part 1: How many characters need to be processed before the first start-of-packet marker is detected?
print(processed_chars(4))

# part 2: How many characters need to be processed before the first start-of-message marker is detected?
print(processed_chars(14))