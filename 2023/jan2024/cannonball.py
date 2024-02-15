import sys

n, s = map(int, sys.stdin.readline().split())
line = []
brk = [0] * n 
for _ in range(n):
    line.append(list(map(int, sys.stdin.readline().split())))
power = 1
total = 0

# with open('mp.in', 'r') as file:
#     n, s = map(int, file.readline().split())
#     line = []
#     brk = [0] * n 
#     for _ in range(n):
#         line.append(list(map(int, file.readline().split())))
# file.close()

c = 0

while 0 < s <= n and c < 10**6:
    if line[s-1][0] == 1 and abs(power) >= line[s-1][1]:
        if brk[s-1] == 0:
            total += 1
            brk[s-1] = 1 
        s += power
        if s > n:
            break
    elif line[s-1][0] == 0:
        if power < 0:
            power = abs(power) + line[s-1][1]
        else:
            power = -(power + line[s-1][1])
        s += power
    elif line[s-1][0] == 1 and abs(power) < line[s-1][1] and line[s-1][0] != 0:
        s += power
    c += 1  

# or try change num to -1 or not 0 or 1 in first index pos

print(total)

