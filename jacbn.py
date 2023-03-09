snakes = []
cols = 0
rows = 0
num_snakes = 0
matrix = []
wormholes = []

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
                optimal_path, direction = max(choices, key=lambda x: x[0])
                
                dp[row][col] = optimal_path + (0 if matrix[row][col] == '*' else int(matrix[row][col]))
                dp_path[row][col] = direction
    dps.append(dp)
    dps_path.append(dp_path)

for r in dps[1]:
    print(r)

for l in dps_path[1]:
    print(l)