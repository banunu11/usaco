# http://www.usaco.org/index.php?page=viewproblem2&cpid=735

with open('lostcow.in', 'r') as file:
    x, y = map(int, file.readline().split())

count = 0
now = x

if x != y:
    for i in range(9*(abs(x-y))):
        temp = now
        if (i+1)%2:
            now = x+2**i
        else:
            now = x-2**i
        print(now, temp)
        if (y <= now and x < y) or (y >= now and x > y):
            count += abs(y - temp)
            break 
        count += abs(now-temp)

with open('lostcow.out', 'w') as file:
    file.write(str(count))
