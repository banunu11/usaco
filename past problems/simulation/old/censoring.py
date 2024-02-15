# http://www.usaco.org/index.php?page=viewproblem2&cpid=526

with open('censor.in', 'r') as file:
    s = file.readline().strip()
    t = file.readline().strip()
file.close()

a = ''
for i in s:
    a += i
    if t == a[-len(t):]:
        a = a[:-len(t)]

with open('censor.out', 'w') as file:
    file.write(a)
file.close()
