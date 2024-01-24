# http://www.usaco.org/index.php?page=viewproblem2&cpid=807

with open("teleport.in", 'r') as file:
    a, b, x, y = map(int, file.readline().strip().split())

base = abs(a-b)
transport = abs(min(a,b) - min(x,y)) + abs(max(a,b) - max(x,y))

ans = min(base, transport)

with open("teleport.out", "w") as file:
    file.write(str(ans))

file.close()