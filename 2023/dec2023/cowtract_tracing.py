def mincows(n, line):
    min_infected = float('inf')
    for i in range(n):
        count = 0
        blob = [False] *n
        for j in range(n):
            blob[j] = True
            count += 1
            if j == 0 and blob[j+1] == False:
                blob[j+1] = True
                print(j, 'if')
            elif j == n-1:
                blob[j-1] = True
                print(j, 'elif')
            else:
                print(j, 'else')
                blob[j+1] = True
                blob[j-1] = True
            print(count)
        min_infected = min(min_infected, count)
    return min_infected


# Read input
# n = int(input())
# state = list(map(int, input().strip()))
# bool_list = [bool(int(num)) for num in state]

n = 5
bool_list = [True, True, True, True, True]
# Output result
print(mincows(n, bool_list))
