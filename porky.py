snakes = []
columns = 0
rows = 0
num_snakes = 0
matrix = []

with open("tests/00-example.txt") as topo_file:
    count = 0
    for line in topo_file:
        vars = line[:-1].split(" ")
        if count == 0:
            columns = vars[0]
            rows = vars[1]
            num_snakes = vars[2]
        elif count == 1:
            for n in range(int(num_snakes)):
                snakes.append(vars[n])
        else:
            row = []
            for n in range(int(columns)):
                row.append(vars[n])
            matrix.append(row)

        count += 1
        print(line[:-1])

max_snake = max(snakes)

print(snakes)
print(matrix)
