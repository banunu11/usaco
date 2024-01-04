import sys

t = int(sys.stdin.readline().strip())
n = int(sys.stdin.readline().strip())
initalheight = [int(x) for x in sys.stdin.readline().strip().split(' ')]
igrowth = [int(x) for x in sys.stdin.readline().strip().split(' ')]
iarray = [int(x) for x in sys.stdin.readline().strip().split(' ')]
triples = zip(iarray, igrowth, initalheight)
sorted_triples = sorted(triples)
array, growth, actualheight = map(list, zip(*sorted_triples))

with open(r"2023\dec2023\stdin.in") as stuck:
    t = int(stuck.readline().strip())

# stuck.close()

    for z in range(t):
        n = int(stuck.readline().strip())
        initalheight = [int(x) for x in stuck.readline().strip().split(' ')]
        igrowth = [int(x) for x in stuck.readline().strip().split(' ')]
        iarray = [int(x) for x in stuck.readline().strip().split(' ')]
        triples = zip(iarray, igrowth, initalheight)
        sorted_triples = sorted(triples)
        array, growth, actualheight = map(list, zip(*sorted_triples))
        height = actualheight

        if n == 1:
            print(0)
        elif all(d == growth[0] for d in growth):
            print('-1')
        else:
            day = 0
            while not all(a>b for a,b in zip(height, height[1:])):
                for i in range(n):
                    height[i] += growth[i]
                    print(height)
                day += 1
                    # print((initalheight[z] + growth[z]*x) > (initalheight[z] + growth[z]*x))
            print(day)

# index pos 
