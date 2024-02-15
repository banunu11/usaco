# http://www.usaco.org/index.php?page=viewproblem2&cpid=568

with open('speeding.in', 'r') as file:
    n, m = map(int, file.readline().strip().split())
    road = []*100
    cow = []*100
    for l in range(n):
        length, speed =  map(int, file.readline().strip().split())
        road.extend([speed] * length)
    for c in range(m):
        length, speed =  map(int, file.readline().strip().split())
        cow.extend([speed] * length)
file.close()

ans = 0
for x in range(100):
    ans = max(ans, cow[x] - road[x])

with open('speeding.out', 'w') as file:
    file.write(str(ans))
file.close()
