import sys

t = int(sys.stdin.readline().strip())

for z in range(t):
    n = int(sys.stdin.readline().strip())
    initalheight = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    igrowth = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    iarray = [int(x) for x in sys.stdin.readline().strip().split(' ')]
    triples = zip(iarray, igrowth, initalheight)
    sorted_triples = sorted(triples)
    array, growth, actualheight = map(list, zip(*sorted_triples))   
    height = actualheight
    days = [0]*n
    if n == 1:
        print(0)
    elif all(d == growth[0] for d in growth):
        print('-1')
    else:
        for i in range(n-1, -1, -1):  # iterate from n-1 to 0 (inclusive)
            if i != n-1:  # if it's not the last tree
                # calculate the number of days required for the current tree to exceed the height of the tree to its right
                days_needed = (height[i+1] - height[i] + growth[i]) // growth[i] - 1.
                # store this in the `days` list
                days[i] = max(days[i], days_needed + days[i+1])
    print(max(days))
# index pos 
