grid = []
for r in range(20):
    row = [int(x) for x in input().split(' ')]
    grid.append(row)

mx = 0
for i in range(20):
    for j in range(17):
        prod = grid[i][j] * grid[i][j+1] * grid[i][j+2] * grid[i][j+3]
        if prod > mx:
            mx = prod
        prod = grid[j][i] * grid[j+1][i] * grid[j+2][i] * grid[j+3][i]
        if prod > mx:
            mx = prod
            
for i in range(17):
    for j in range(17):
        prod = grid[i][j] * grid[i+1][j+1] * grid[i+2][j+2] * grid[i+3][j+3]
        if prod > mx:
            mx = prod
for i in range(17):
    for j in range(3,20):
        prod = grid[i][j] * grid[i+1][j-1] * grid[i+2][j-2] * grid[i+3][j-3]
        if prod > mx:
            mx = prod
            
print(str(mx))
