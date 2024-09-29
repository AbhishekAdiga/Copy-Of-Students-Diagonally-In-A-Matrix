m,n = map(int,input().split())
matrix = [input().split() for _ in range(m)]
#print(matrix)

copied_students = []

for i in range(m):
  for j in range(n):
    if(matrix[i][j] == "C"):
      copied_students.append((i,j))

#print(copied_students)

copy_of_matrix = [ row[:] for row in matrix]

directions = [(-1,-1),(-1,1),(1,-1),(1,1)]

for i,j in copied_students:
  for dx,dy in directions:
    new_index_of_i,new_index_of_j = i + dx, j + dy
    if(0 <= new_index_of_i < m and 0 <= new_index_of_j < n):
      copy_of_matrix[new_index_of_i][new_index_of_j] = "C"

for row in copy_of_matrix:
  print(" ".join(row))
