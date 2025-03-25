from bisect import bisect_left, bisect_right
import sys
import math
from collections import deque, defaultdict
# input = sys.stdin.readline
N = int(input())
j = 1
for i in range(j, N+1):
    space = " " * (N-i)
    star = "*" * i
    print(f"{space+star}")