mat1=[[1,2,3],[4,5,6],[7,8,9]]

for i in range(len(mat1)):
    for j in range(len(mat1)):
        if i+j==2:
            print(i,j)