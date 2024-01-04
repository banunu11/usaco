import sys

nm = [int(i) for i in sys.stdin.readline().strip().split(' ')]
cows = [int(i) for i in sys.stdin.readline().strip().split(' ')]
candy = [int(i) for i in sys.stdin.readline().strip().split(' ')]

for m in range(nm[1]):
    height = candy[m]
    for c in range(nm[0]):
        if c == 0:
            if candy[m] > cows[c]:
                largest = cows[c]
                candy[m] -= cows[c]
                cows[c] += candy[m]  
            else:
                largest = cows[c]
                cows[c] += candy[m] 
                candy[m] -= cows[c]                    
        elif largest <= cows[c] and candy[m] > 0:
            candy[m] -= cows[c] - largest
            cows[c] += cows[c] - largest
            largest = cows[c]

for z in range(nm[0]):
    print(cows[z])