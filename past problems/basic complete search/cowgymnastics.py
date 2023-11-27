# http://www.usaco.org/index.php?page=viewproblem2&cpid=963

def charword(word):
    alpha = [0]*26
    for o in word:
        alpha[ord(o)-ord("a")] += 1
    return alpha

# loop over words
with open(r"C:\Users\Cheryl\Desktop\academic ish\Others\computer science things\USACO\basic complete search\gymnastics.in") as gym:
    k, j = gym.readline().split()
    # n = int(gym.readline(),split)
    # words = [gym.readline().split() for j in range(n)]
    # gym.close()

# full = [0]*26
# for w, m in words:
#     a, b = charword(w), charword(m)
#     for i in range(26):
#         full[i] += max(a[i], b[i])

# with open("gymnastics.out", "w") as written:
#     for i in full:
#         written.write(str(i) + '\n')
#     written.close()

print(k, j)


