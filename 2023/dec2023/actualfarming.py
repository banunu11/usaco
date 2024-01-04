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
    if n == 1:
        print(0)
    elif all(d == growth[0] for d in growth):
        print('-1')
    else:
        max_growth = max(growth)
        max_height = max(height)
        max_index = height.index(max_height)

        if all(a <= b for a, b in zip(height, height[1:])):
            print(0)
        elif all(d == max_growth for d in growth):
            print(-1)
        else:
            days_to_reach_max_height = (max_height - height[max_index] + max_growth - 1) // max_growth
            total_days = max(days_to_reach_max_height, 0) + max_index
            print(total_days)
# index pos 
