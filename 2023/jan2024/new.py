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
    fin = []
    for i in range(0, n-2):
        if (hay[i] == hay[i+1] and hay[i+1] != hay[i+2]) or (hay[i+2] == hay[i+1] and hay[i+2] != hay[i]):
            fin.append(hay[i+1])
        elif hay[i] == hay[i+2] and (hay[i] != hay[i+1]):
            fin.append(hay[i])
        elif hay[i] == hay[i+2] and hay[i] == hay[i+1]:
            fin.append(hay[i])
    if len(fin) == 0:
        print(-1)
    else:
        if z != t-1:
            print(' '.join(map(str, final)))
        else: 
            print(' '.join(map(str, final)), end='')


        #     last = [str(s) for s in fin]
        #     print(' '.join(last))
        # else:
        #     last = [str(s) for s in fin]
        #     print(' '.join(last))


            # max

    # count = 0
        # currnum = 1
        # maxc = float('inf')
        # mode = []
        # fin.sort()
        # if len(fin) > 1 and -1 in fin:
        #     fin.remove(-1)
        # for d in fin:
        #     if d == currnum:
        #         count += 1
        #     else:
        #         if count > maxc:
        #             maxc = count
        #         elif:
        #             mode.append(str(currnum))
        #         currnum += 1