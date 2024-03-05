# https://usaco.org/index.php?page=viewproblem2&cpid=712
# semi help

with open('circlecross.in', 'r') as file:
    li = [c for c in file.readline()]
file.close()

start = [-1]*26
end = [-1]*26
for x in range(65, 91):
    for index, value in enumerate(li):
        if value is chr(x):
            if start[x-65] == -1:
                start[x-65] = index
            else:
                end[x-65] = index

count = 0
for i in range(26): 
    for j in range(26):
        # print(start[i], start[j], end[i], end[j])  and start[i] < end[j]
        if start[i] < start[j] and start[j] < end[i] and end[i] < end[j] and start[i] < end[j]:
            count += 1

with open('circlecross.out', 'w') as file:
    file.write(str(count))   
file.close()