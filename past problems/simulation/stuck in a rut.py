# http://www.usaco.org/index.php?page=viewproblem2&cpid=1061

with open(r"past problems\simulation\stdin.in") as stuck:
    #n = no of cows
    n = int(stuck.readline())
    order = [stuck.readline().split() for j in range(n)]
    stuck.close()

count = []

for i in range(n):
    for x in range(n):
        if i != x:
            if order[i][0] != order[x][0]:
                pass 
            else:
                print(False, order[i][0], order[x][0])

# with open("stdin.out", "w") as written:
#     for i in range(n):
#         written.write(count[n])
#     written.close()
