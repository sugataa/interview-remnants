# def get_number_of_islands(binaryMatrix):
#   total_islands = 0
#   for i in range(len(binaryMatrix)):
#     for j in range(len(binaryMatrix[i])):
#       if binaryMatrix[i][j] == 1:
#         total_islands += 1
#         _get_number_of_islands(binaryMatrix, i, j)
#   return total_islands
#
# def _get_number_of_islands(binaryMatrix, i, j):
#   if (-1 < i < len(binaryMatrix)) and (-1 < j < len(binaryMatrix[i])):
#     if binaryMatrix[i][j] == 0:
#       return
#     else:
#       binaryMatrix[i][j] = 0
#       _get_number_of_islands(binaryMatrix, i, j-1)
#       _get_number_of_islands(binaryMatrix, i-1, j)
#       _get_number_of_islands(binaryMatrix, i, j+1)
#       _get_number_of_islands(binaryMatrix, i+1, j)

def get_number_of_islands(binaryMatrix):
  total_islands = 0
  for i in range(len(binaryMatrix)):
    for j in range(len(binaryMatrix[i])):
      if binaryMatrix[i][j] == 1:
        total_islands += 1
        print('hitting a 1 ---->', (i, j))
        print(binaryMatrix)
        _get_number_of_islands(binaryMatrix, i, j)
  return total_islands

def _get_number_of_islands(binaryMatrix, i, j):
  queue = [(i,j)]
  while queue:
    vertex = queue.pop(0)
    vertex_x = vertex[0]
    vertex_y = vertex[1]
    binaryMatrix[vertex_x][vertex_y] = 0
    for val in [(vertex_x, vertex_y-1), (vertex_x-1, vertex_y), (vertex_x, vertex_y+1), (vertex_x+1, vertex_y)]:
        if (-1 < val[0] < len(binaryMatrix)) and (-1 < val[1] < len(binaryMatrix[0])) and binaryMatrix[val[0]][val[1]] == 1:
            queue.append(val)


binaryMatrix = [ [0,    1,    0,    1,    0],
                 [0,    0,    1,    1,    1],
                 [1,    0,    0,    1,    0],
                 [0,    1,    1,    0,    0],
                 [1,    0,    1,    0,    1] ]

print(get_number_of_islands(binaryMatrix))
