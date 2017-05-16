def bomber(field):
    if len(field) < 1:
        return 0

    h = len(field)
    w = len(field[0])
    max_enemies = 0

    for row in range(h):
        for col in range(w):

            if field[row][col] == "0":
                cur_max = 0
                cur_row = row
                cur_col = col

                while cur_row >= 0:
                    if field[cur_row][col] == "W":
                        break
                    if field[cur_row][col] == "E":
                        cur_max += 1
                    cur_row -= 1

                cur_row = row

                while cur_row < h:
                    if field[cur_row][col] == "W":
                        break
                    if field[cur_row][col] == "E":
                        cur_max += 1
                    cur_row += 1

                cur_row = row

                while cur_col >= 0:
                    if field[row][cur_col] == "W":
                        break
                    if field[row][cur_col] == "E":
                        cur_max += 1
                    cur_col -= 1

                cur_col = col

                while cur_col < w:
                    if field[row][cur_col] == "W":
                        break
                    if field[row][cur_col] == "E":
                        cur_max += 1
                    cur_col += 1

                if cur_max > max_enemies:
                    max_enemies = cur_max

    return max_enemies