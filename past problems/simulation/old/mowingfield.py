# http://www.usaco.org/index.php?page=viewproblem2&cpid=593

with open('mowing.in', 'r') as file:
    n = int(file.readline().strip())
    where = []
    x, y = 0, 0
    for l in range(n):
        d, num =  file.readline().strip().split()
        if d == 'N':
            for i in range(int(num)):
                y += 1
                where.append([x, y])
        elif d == 'E':
            for i in range(int(num)):
                x += 1
                where.append([x, y])
        elif d == 'S':
            for i in range(int(num)):
                y -= 1
                where.append([x, y])
        else:
            for i in range(int(num)):
                x -= 1
                where.append([x, y])
file.close()

ans = float('inf')

for i in range(len(where)):
    for j in range(i+1, len(where)):
        if where[i][0] == where[j][0] and where[i][1] == where[j][1]:
            ans = min(ans, j-i)

with open("mowing.out", "w") as file:
    if ans == float('inf'):
        file.write('-1')
    else:
        file.write(str(ans))    
file.close()