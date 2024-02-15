# http://www.usaco.org/index.php?page=viewproblem2&cpid=831

with open(r"tttt.in") as file:
    cows = [list(file.readline().strip()) for j in range(3)]
    file.close()

# 8 times
indi = 0
team = 0

# straight across
def stra(char):
    for i in range(3):
        if cows[i][0] == char:
            if cows[i][0] == cows[i][1] and cows[i][0] == cows[i][2]:
                return True
            else:
                return False   

def strat(char, chra): 
    if cows[i][0] == char and cows[i][1] == chra:    
        if (cows[i][0] == cows[i][1] and cows[i][0] != cows[i][2]) or (cows[i][0] == cows[i][2] and cows[i][0] != cows[i][1]) or (cows[i][1] == cows[i][2] and cows[i][1] != cows[i][0]):
            team += 1

# straight down
for x in range(3):
    if cows[0][x] == cows[1][x] and cows[0][x] == cows[2][x]:
        indi += 1
    if (cows[0][x] == cows[1][x] and cows[0][x] != cows[2][x]) or (cows[0][x] == cows[2][x] and cows[0][x] != cows[1][x]) or (cows[1][x] == cows[2][x] and cows[1][x] != cows[0][x]):
        team += 1

# left diagonal
if cows[0][0] == cows[1][1] and cows[0][0] == cows[2][2]:
    indi += 1
if (cows[0][0] == cows[1][1] and cows[0][0] != cows[2][2]) or (cows[0][0] == cows[2][2] and cows[0][0] != cows[1][1]) or (cows[1][1] == cows[2][2] and cows[1][1] != cows[0][0]):
    team += 1

# right diagonal
if cows[0][2] == cows[1][1] and cows[0][2] == cows[2][0]:
    indi += 1
if (cows[0][2] == cows[1][1] and cows[0][2] != cows[2][0]) or (cows[0][2] == cows[2][0] and cows[0][2] != cows[1][1]) or (cows[1][1] == cows[2][0] and cows[1][1] != cows[0][2]):
    team += 1

for i in range(65, 91):
    pass

with open('tttt.out', 'w') as file:
    file.write(f"{str(indi)}\n{str(team)}")
file.close()


# stopped, i know how to do it now but too much code changes to do
