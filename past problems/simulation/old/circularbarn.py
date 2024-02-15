# http://www.usaco.org/index.php?page=viewproblem2&cpid=616

with open('cbarn.in', 'r') as file:
    n = int(file.readline().strip())
    cow = [0]*(n)
    for i in range(n):
        cow[i] = int(file.readline().strip())
file.close()

small = float('inf')
for m in range(n):
    total = 0
    for x in range(n-1):
        total += cow[x+1] * (x+1)
    cow.append(cow[0])
    cow.pop(0)
    print(total)
    small = min(small, total)

# print(small)
with open('cbarn.out', 'w') as file:
    file.write(str(small))
file.close()
