
t = int(input())
for z in range(t):
    n = int(input())
    hay = list(map(int, input().split()))
    if n == 1:
        print(hay[0], end='')
    if n == 2:
        if hay[0] == hay[1]:
            print(hay[0], end='')
        elif hay[0] != hay[1]:
            print(-1, end='')
    fin = set()
    for i in range(0, len(hay)-2):
        if (hay[i] == hay[i+1] and hay[i+1] != hay[i+2]) or (hay[i+2] == hay[i+1] and hay[i+2] != hay[i]):
            fin.add(hay[i+1])
        elif hay[i] == hay[i+2] and (hay[i] != hay[i+1]):
            fin.add(hay[i])
        elif hay[i] == hay[i+2] and hay[i] == hay[i+1]:
            fin.add(hay[i])
    if len(fin) == 0 and n != 2:
        print(-1, 'sd')
    else:
        if z != t-1:
            print(' '.join(map(str, fin)))
        else: 
            print(' '.join(map(str, fin)), end='')
