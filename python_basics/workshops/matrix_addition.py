x = [[2,4,6], [1,3,5], [9,8,7]]
y = [[1,2,3], [4,5,6], [7,8,9]]

result = [[0,0,0], [0,0,0], [0,0,0]]

for i in range(len(x)):
    for j in range(len(y)):
        result[i][j] = x[i][j] + y[i][j]
        
print(result)