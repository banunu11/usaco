# https://usaco.org/index.php?page=viewproblem2&cpid=1060
# needed help

n = int(input())
l = [int(v) for v in input().split()]

count = 0
for i in range(n):
    for j in range(i, n):
        total = sum(l[i:j+1])/(j-i+1)
        for index in range(i, j + 1):
            if l[index] == total:
                count += 1
                break
print(count)
