# http://www.usaco.org/index.php?page=viewproblem2&cpid=1059
import sys

nums = list(map(int, sys.stdin.readline().split()))

m = max(nums)
A = min(nums)
nums.remove(A)
B = min(nums)
C = m - A - B

sys.stdout.write(f'{A} {B} {C}')




