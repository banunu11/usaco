n = int(input())
patch = list(map(int,input().split()))
start = [0]*n
extra = [0]*n
start[0] = patch[0] - 0
for i in range(1, n):
    start[i] = patch[i] - patch[i-1]
extra[0] = abs(patch[0] - 0)
for j in range(1, n):
    extra[j] = abs(start[j] - start[j-1])
print(sum(extra))

