# https://adventofcode.com/2022/day/8


def tree_visible(
    coord: tuple[int, int],
    trees_matrix: list[list[int]]
) -> bool:
    x, y = coord
    width, height = len(trees_matrix[0]), len(trees_matrix)

    # check top
    top_visible = True
    for i in range(y):
        if trees_matrix[x][i] >= trees_matrix[x][y]:
            top_visible = False
            break
    if top_visible:
        return True

    # check right
    right_visible = True
    for i in range(x+1, width):
        if trees_matrix[i][y] >= trees_matrix[x][y]:
            right_visible = False
            break
    if right_visible:
        return True

    # check left
    left_visible = True
    for i in range(x):
        if trees_matrix[i][y] >= trees_matrix[x][y]:
            left_visible = False
            break
    if left_visible:
        return True

    # check bottom
    bottom_visible = True
    for i in range(y+1, height):
        if trees_matrix[x][i] >= trees_matrix[x][y]:
            bottom_visible = False
            break
    if bottom_visible:
        return True

    return False

total_visible_trees = 0

with open('input.txt') as f:
    lines = f.readlines()
    trees_matrix = [
        list(map(int, line.strip()))
        for line in lines
    ]

width, height = len(trees_matrix[0]), len(trees_matrix)
total_visible_trees += (width * height - (width - 2) * (height - 2))

for (i, row) in enumerate(trees_matrix):
    if i == 0 or i == height - 1:
        continue
    for (j, tree) in enumerate(row):
        if j == 0 or j == width - 1:
            continue
        if tree_visible((j, i), trees_matrix):
            total_visible_trees += 1

# part 1: Consider your map; how many trees are visible from outside the grid?
print(total_visible_trees)


def scenic_score(
    coord: tuple[int, int],
    trees_matrix: list[list[int]]
) -> int:
    x, y = coord
    width, height = len(trees_matrix[0]), len(trees_matrix)

    # check top
    top_score = 0
    for i in range(y-1, -1, -1):
        top_score += 1
        if trees_matrix[x][i] >= trees_matrix[x][y]:
            break

    # check right
    right_score = 0
    for i in range(x+1, width):
        right_score += 1
        if trees_matrix[i][y] >= trees_matrix[x][y]:
            break

    # check left
    left_score = 0
    for i in range(x-1, -1, -1):
        left_score += 1
        if trees_matrix[i][y] >= trees_matrix[x][y]:
            break

    # check bottom
    bottom_score = 0
    for i in range(y+1, height):
        bottom_score += 1
        if trees_matrix[x][i] >= trees_matrix[x][y]:
            break

    return top_score * right_score * left_score * bottom_score

scenic_scores = [0]

for (i, row) in enumerate(trees_matrix):
    if i == 0 or i == height - 1:
        continue
    for (j, tree) in enumerate(row):
        if j == 0 or j == width - 1:
            continue
        
        scenic_scores.append(scenic_score((j, i), trees_matrix))

# part 2: Consider each tree on your map. What is the highest scenic score possible for any tree?
print(max(scenic_scores))