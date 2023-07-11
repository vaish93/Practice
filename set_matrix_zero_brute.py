"""
1  1   1  1

1  0   0  1

1  0   1  1

"""

matrix = [[1,1,1,1],[1,0,0,1],[1,0,1,1]]
rows = len(matrix)
cols = len(matrix[0])

def myrow(matrix,rows,cols,i):
                for a in  range(cols):
                    if matrix[i][a] !=0:
                        matrix[i][a]=-1
def mycols(matrix,rows,cols,j):
                for b in range(rows):
                    if matrix[b][j] != 0:
                        matrix[b][j]=-1

for i in range(rows):
    for j in range(cols):
        if matrix[i][j]==0:
            myrow(matrix,rows,cols,i)
            mycols(matrix,rows,cols,j)


for a1 in range(rows):
    for b1 in range(cols):
        if matrix[a1][b1]== -1:
            matrix[a1][b1]=0

print(matrix)

