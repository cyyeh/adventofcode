# https://adventofcode.com/2022/day/7


def execute_command(command: str, current_dir: list[str]):
    if command.startswith('cd'):
        path = command.split(' ')[-1].strip()
        if path == '/':
            current_dir = ['/']
        elif path == '..':
            current_dir = current_dir[:-1]
        else:
            if current_dir[-1] != '/':
                current_dir.append(f'{current_dir[-1]}/{path}')
            else:
                current_dir.append(f'{current_dir[-1]}{path}')
        return current_dir
    elif command.startswith('ls'):
        return current_dir
    else:
        raise ValueError(f'Unknown command: {command}')


'''
{
    [dir]: {
        total_size: int
    },
}
'''
dir_data = {
    '/': {
        'total_size': 0,
    }
}
current_dir = ['/']

with open('input.txt') as f:
    for line in f.readlines()[2:]:
        if line.startswith('$ '):
            current_dir = execute_command(line[2:], current_dir)
        else:
            if current_dir[-1] not in dir_data:
                dir_data[current_dir[-1]] = {
                    'total_size': 0
                }

            if not line.startswith('dir'):
                file_size = int(line.split(' ')[0])
                for path in current_dir:
                    dir_data[path]['total_size'] += file_size
                        

total_size_of_at_most_100000 = sum(
    filter(
        lambda x: x <= 100000,
        map(
            lambda dir: dir['total_size'],
            dir_data.values()
        )
    )
)

# part 1: Find all of the directories with a total size of at most 100000. What is the sum of the total sizes of those directories?
print(total_size_of_at_most_100000)

total_size = dir_data['/']['total_size']

min_disk_size_to_remove = 30000000 - (70000000 - total_size)
size_of_dir_to_be_deleted = min(
    filter(
        lambda x: x >= min_disk_size_to_remove,
        map(
            lambda dir: dir['total_size'],
            dir_data.values()
        )
    )
)

# part 2: Find the smallest directory that, if deleted, would free up enough space on the filesystem to run the update. What is the total size of that directory?
print(size_of_dir_to_be_deleted)