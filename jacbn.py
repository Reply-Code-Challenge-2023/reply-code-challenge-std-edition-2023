snakes = []
cols = 0
rows = 0
num_snakes = 0
matrix = []
wormholes = []


def checkForOverlap(possible_path_index, dps_path, row, col, rows, cols, paths, wormholes):
    i = len(dps_path)
    visited = []
    r = row
    c = col
    valid = False
    
    print(possible_path_index, len(paths), len(direction))
    print(paths[possible_path_index], direction[possible_path_index])
    
    while (c, r) not in visited:
        if i > 1:
            visited.append((c, r))
            m = dps_path[i-1]
            # print(r, c)
            # print(len(m), len(m[0]))
            direction = m[r][c]
    
            if len(direction[possible_path_index]) > 2:
                index = int(direction[possible_path_index][1:-1])
                c, r = wormholes[index]
            else:
                if direction[0][0] == 'U':
                    c = (c - 1) % cols
                elif direction[0][0] == 'D':
                    c = (c + 1) % cols
                elif direction[0][0] == 'L':
                    r = (r - 1) % rows
                elif direction[0][0] == 'R':
                    r = (r + 1) % rows
                else:
                    raise Exception(f"Unknown direction: {direction[0]}")
        i -= 1
        if i <= 1:
            valid = (c, r) not in visited
            break
        if valid:
            break
    
    if valid == False:
        raise Exception("no valid path for snake")

with open("tests/00-example.txt") as topo_file:
    count = 0
    for line in topo_file:
        variables = line[:-1].split(" ")
        if count == 0:
            cols = int(variables[0])
            rows = int(variables[1])
            num_snakes = int(variables[2])
        elif count == 1:
            for n in range(int(num_snakes)):
                snakes.append(int(variables[n]))
        else:
            row = []
            for n in range(int(cols)):
                row.append(variables[n])
                if variables[n] == "*":
                    wormholes.append((n, count-2))
            matrix.append(row)

        count += 1


print(wormholes)

max_snake = max(snakes)
dps = []
dps_path = []
for bound in range(1, max_snake + 1):
    if bound == 1:
        dp = list(map(lambda x: list(map(lambda y: 0 if y == "*" else int(y), x)), matrix))
        dp_path = [['' for _ in range(cols)] for _ in range(rows)]
    else:
        dp = [[0 for _ in range(cols)] for _ in range(rows)]
        dp_path = [['' for _ in range(cols)] for _ in range(rows)]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                                       
                adjacent_wormholes = []
                possible_next = []
                
                # for each adjacent cell, check if it's a wormhole
                for cell in [(col, (row-1)%rows, 'U '), (col, (row+1)%rows, 'D '), ((col-1)%cols, row, 'L '), ((col+1)%cols, row, 'R ')]:
                    if (cell[0], cell[1]) in wormholes:
                        adjacent_wormholes.append(cell)
                    # we can always go up/down/left/right
                    possible_next.append(cell)
                        
                for adj in adjacent_wormholes:
                    for i, w in enumerate(wormholes):
                        possible_next.append((w[0], w[1], f"{adj[2]}{i} "))
                    
                # remove duplicates (can there actually be any??)
                possible_next = list(set(possible_next))
                prev = dps[bound - 2]
                
                choices = [(prev[y % rows][x % cols], direction) for x, y, direction in possible_next]
                paths, direction = zip(*sorted(choices, key=lambda x: x[0]))
                
                # paths[0] is optimal, but we can't always take the optimal path because it might overlap itself
                
                # check for overlaps:
                
                assert len(paths) == len(direction)
                
                for possible_path_index in range(len(paths)):
                    if not checkForOverlap(possible_path_index, dps_path, row, col, rows, cols, paths, wormholes):
                        continue
                    else:
                        best_choice_index = paths[possible_path_index]
                    
                
                dp[row][col] = paths[best_choice_index] + (0 if matrix[row][col] == '*' else int(matrix[row][col]))
                dp_path[row][col] = direction
    dps.append(dp)
    dps_path.append(dp_path)

for r in dps[1]:
    print(r)

for l in dps_path[1]:
    print(l)
    
    
