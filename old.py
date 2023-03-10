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
    
    if valid == False:
        raise Exception("no valid path for snake")