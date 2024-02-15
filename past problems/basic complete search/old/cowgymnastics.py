# http://www.usaco.org/index.php?page=viewproblem2&cpid=963
# needed help

with open('gymnastics.in', 'r') as file:
    k, n = map(int, file.readline().split())
    l = []
    for c in range(k):
        l.append([int(i)-1 for i in file.readline().split()])
file.close()

pairs = 0 
for i in range(n):
    for j in range(n):
        if i == j:
            continue
        for s in l:
            print(s.index(i),s.index(j))
            if s.index(l) > s.index(j):
                break
        else:
            pairs+=1


with open('gymnastics.out', 'w') as file:
    file.write(str(pairs))
file.close()
        


