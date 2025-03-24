from bisect import bisect_left, bisect_right
import sys
import math
from collections import deque
# input = sys.stdin.readline
# print = sys.stdout.write
# limit_number = 5000000
# sys.setrecursionlimit(limit_number) # 재귀제한 해제

N,M = list(map(int, input().split()))
if N > M:
    print(">")
elif N < M:
    print("<")
else:
    print("==")