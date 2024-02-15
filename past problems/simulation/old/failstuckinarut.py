# http://www.usaco.org/index.php?page=viewproblem2&cpid=1061

t = int(input().strip())
ncow = []
ecow = []
id = 0
cowpos = []
for l in range(t):
    d, x, y = input().strip().split()
    x, y = int(x), int(y)
    if d == 'N':
        ncow.append((x,y,id))
    else:
        ecow.append((x,y,id))
    cowpos.append((x,y))
    id += 1

# 0 is north stop
# so collide[1] is the one that is stopping
collide = []
for n in ncow:
    for e in ecow:
        cx,cy = n[0] - e[0], e[1] - n[1]
        if cx > cy and cy > 0: 
            collide.append([cx, e[2], n[2], 1])
        elif cx < cy and cx > 0:
            collide.append([cy, n[2], e[2], 0])
collide.sort()
# collide0-3, time, stopcowpos, causecowpos, north or east
ans = [-1]*t
for co in collide:
    # if both cows r still moving then stopcow stopped
    if ans[co[2]] == -1 and ans[co[1]] == -1 :
        ans[co[1]]  = co[0]
    # if the causecow is not moving anymore then stopcow continue, check if causecow can still stop others
    elif ans[co[2]] != -1 and ans[co[1]] == -1:
        if co[3]:
            start = (cowpos[co[2]][1])
            end = (cowpos[co[2]][1]+ans[co[2]])
            if cowpos[co[1]][1] >= start and cowpos[co[1]][1] <= end:
                ans[co[1]] = co[0]
        else:
            start = (cowpos[co[2]][1])
            end = (cowpos[co[2]][1]+ans[co[2]])
            if cowpos[co[1][0]] >= start and cowpos[co[1]][0] <= end:
                ans[co[1]] = co[0]

for a in ans:
    if a == -1:
        print('Infinity')
    else:
        print(a)