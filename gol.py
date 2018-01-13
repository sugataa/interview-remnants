def game_of_life(game_seed):
    result_array = [x[:] for x in [[0] * len(game_seed)] * len(game_seed)]
    for i in range(len(game_seed)):
        for j in range(len(game_seed)):
            neighbour_sum = sum_of_neighbors(i, j, game_seed)
            result_array[i][j] = reduce_coord(i, j, game_seed, neighbour_sum)
    return result_array

def sum_of_neighbors(x, y, game_state):
    counter = 0
    for i in range(-1, 2):
        for j in range(-1, 2):
            if valid_coord(x+i, y+j, len(game_state)):
                counter += game_state[x+i][y+j]
    return counter - game_state[x][y]

def valid_coord(x, y, boundary):
    return (boundary > x > -1) and (boundary > y > -1)

def reduce_coord(i, j, game_state, neighbour_sum):
    if game_state[i][j] == 1 and (neighbour_sum == 2 or neighbour_sum == 3):
        return 1
    elif game_state[i][j] == 0 and (neighbour_sum == 3):
        return 1
    return 0


if __name__ == "__main__":
    seed = [
          [0,0,1,0,0,0,0,0,0],
          [0,0,0,1,0,0,0,0,0],
          [0,1,1,1,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]
        ]
    tenth_state = [
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,1,0,0,0],
          [0,0,0,1,0,1,0,0,0],
          [0,0,0,0,1,1,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0],
          [0,0,0,0,0,0,0,0,0]
        ]
    temp = game_of_life(seed)
    # print(temp)
    for i in range(9):
        temp = game_of_life(temp)

    for i in temp:
        print(i)
    print(temp == tenth_state)
