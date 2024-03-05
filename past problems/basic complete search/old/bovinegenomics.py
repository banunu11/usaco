# https://usaco.org/index.php?page=viewproblem2&cpid=736
# semi help

with open('cownomics.in', 'r') as file:
    n, m = map(int, file.readline().split())
    bspot = [file.readline().strip() for _ in range(n)]
    bnormal = [file.readline().strip() for _ in range(n)]
    spot = []
    normal = []
    for a in range(m):
        grp1 = set()
        grp2 = set()
        for b in range(n):
            grp1.add(bspot[b][a])
            grp2.add(bnormal[b][a])
        spot.append(grp1)
        normal.append(grp2)
file.close()

count = 0
for f in range(m):
    if len(spot[f]) == len(spot[f].difference(normal[f])):
    # if len(spot[f].intersection(normal[f])) == 0: also works
        count += 1

with open('cownomics.out', 'w') as file:
    file.write(str(count))
file.close