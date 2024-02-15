# http://www.usaco.org/index.php?page=viewproblem2&cpid=917

with open('traffic.in', 'r') as file:
    n  = int(file.readline().strip())
    li = []
    for l in range(n):
        li.append(file.readline().strip().split())
        li[l][1] = int(li[l][1])
        li[l][2] = int(li[l][2])
file.close()

start = [0, float('inf')]
end = [0, float('inf')]

for x in range(n):
    if li[x][0] == 'on':
        end = [end[0]+li[x][1], end[1]+li[x][2]]
        # print(x)
    elif li[x][0] == 'none':
        end = [max(end[0], li[x][1]), min(end[1], li[x][2])]
        # print(x, end[0], li[x][1])
    elif li[x][0] == 'off':
        end = [end[0]-li[x][2], end[1]-li[x][1]]
        if end[0] < 0:
            end[0] = 0
    #     print(x, 'sd')
    # print(end)  

for x in range(n-1, -1, -1):
    if li[x][0] == 'off':
        start = [start[0]+li[x][1], start[1]+li[x][2]]
    elif li[x][0] == 'none':
        start = [max(start[0], li[x][1]), min(start[1], li[x][2])]
    elif li[x][0] == 'on':
        start = [start[0]-li[x][2], start[1]-li[x][1]]
    if start[0] < 0:
            start[0] = 0

with open('traffic.out', 'w') as file:
    file.write(f"{str(start[0])} {str(start[1])}\n")
    file.write(f"{str(end[0])} {str(end[1])}")
file.close()