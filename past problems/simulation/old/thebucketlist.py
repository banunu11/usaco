# http://www.usaco.org/index.php?page=viewproblem2&cpid=856

with open("blist.in", 'r') as file:
    time = [0]*1001
    largest = 0
    n = int(file.readline())
    for _ in range(n):  
        x,y,z = (map(int, file.readline().strip().split()))
        for i in range(x, y+1):
            time[i] += z
            if time[i] > largest:
                largest = time[i]
file.close()

with open('blist.out', 'w') as file:
    file.write(str(largest))
file.close()
