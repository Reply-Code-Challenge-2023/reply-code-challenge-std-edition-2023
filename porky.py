snakes = []
columns = 0
rows = 0
num_snakes = 0
matrix = []
wormhole_coords = []

with open("tests/00-example.txt") as topo_file:
    count = 0
    for line in topo_file:
        variables = line[:-1].split(" ")
        if count == 0:
            columns = variables[0]
            rows = variables[1]
            num_snakes = variables[2]
        elif count == 1:
            for n in range(int(num_snakes)):
                snakes.append(variables[n])
        else:
            row = []
            for n in range(int(columns)):
                row.append(variables[n])
                if variables[n] == "*":
                    wormhole_coords.append((count - 2, n))
            matrix.append(row)

        count += 1

max_snake = max(snakes)
dps = []
for bound in range(1, max_snake + 1):
    if bound == 1:
        dp = list(
            map(lambda x: list(map(lambda y: 0 if y == "*" else int(y), x)), matrix)
        )
    else:
        dp = [[0] * columns for _ in rows]
        for row in range(len(matrix)):
            for col in range(len(matrix[row])):
                optimal_path = max(
                    dps[bound - 1][row - 1][col],
                    dps[bound - 1][row + 1][col],
                    dps[bound - 1][row][col - 1],
                    dps[bound - 1][row][col + 1],
                )

    dps.append(dp)

print(matrix)
print(dps[0])
