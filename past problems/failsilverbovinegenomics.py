# https://usaco.org/index.php?page=viewproblem2&cpid=739

with open('cownomics.in', 'r') as file:
    n, m = map(int, file.readline().split())
    bspot = [file.readline().strip() for _ in range(n)]
    bnormal = [file.readline().strip() for _ in range(n)]
file.close()

count = 0
for i in range(m):
    for j in range(i+1, m):
        for l in range(j+1, m):
            tspot = set()
            tnormal = set()
            # print(i, j, l)
            for x in range(3):
                spot = bspot[x]
                normal = bnormal[x]
                tspot.add((spot[i], spot[j], spot[l]))
                tnormal.add((normal[i], normal[j], normal[l]))
            flag = False
            for f in range(n):
                for k in range(n):
                     if bspot[f][i]==bnormal[k][i] and bspot[f][j]==bnormal[k][j] and bspot[f][k]==bnormal[k][l]:
                        flag = True
                if flag:
                    break
            else:
                count += 1        
        
with open('cownomics.out', 'w') as file:
    file.write(str(count))
file.close
