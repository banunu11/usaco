# http://www.usaco.org/index.php?page=viewproblem2&cpid=761

with open('measurement.in', 'r') as file:
    n = int(file.readline().strip())
    champ = []
    for l in range(n):
        champ.append(file.readline().strip().split())
        champ[l][0] = int(champ[l][0])
    champ.sort()
file.close()

fin = {'Bessie': 7, 'Mildred': 7, 'Elsie': 7}
ans = 0
prev = []
for i in range(n):
    fin[champ[i][1]] += int(champ[i][2])
    tea = []
    for key in fin:
        if (fin[key] == temp):
            tea.append(key)
    if tea != prev:
        ans += 1    
    prev = tea

with open('measurement.out', 'w') as file:
    file.write(str(ans))
file.close()
