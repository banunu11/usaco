# https://codeforces.com/problemset/problem/1535/B

from math import gcd

for z in range(int(input())):
    c = 0
    n = int(input())
    a = list(map(lambda x: int(x), input().split(" ")))
    for i in range(n):
        for j in range(i+1, n):
            if gcd(a[i], 2*a[j]) > 1 or gcd(2*a[i], a[j]) > 1:
                c += 1

    print(c)
