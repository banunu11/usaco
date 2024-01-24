# http://www.usaco.org/index.php?page=viewproblem2&cpid=891

order = []
with open(r"past problems\simulation\old\shell.in") as shell:
    n = int(shell.readline())
    for k in range(n):
        order.append(shell.readline().split())
        for j in range(3):
            order[k][j] = int(order[k][j])
    shell.close()

count = [0 for _ in range(3)]


for x in range(3):
    place = x+1
    for i in range(n):
        print('normal order', place)
        print('before',place, order[i][0], order[i][1])
        if place == order[i][0]:
            place = order[i][1]
        elif place == order[i][1]:
            place = order[i][0]
        print('place and supposed',place, order[i][2])
        print('switched order',order[i])
        if place == order[i][2]:
            count[x] += 1

with open("shell.out", "w") as written:
    written.write(str(max(count)))
    written.close()