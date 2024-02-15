# https://usaco.org/index.php?page=viewproblem2&cpid=712

with open('circlecross.in', 'r') as file:
    li = [c for c in file.readline()]
file.close()

for i in range(65, 91):
    print(chr(i), li.index(chr(i)))



with open('circlecross.out', 'w') as file:
    pass   
file.close()