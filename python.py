from bisect import bisect_left, bisect_right
import sys
import math
from collections import deque
# input = sys.stdin.readline
# print = sys.stdout.write
# limit_number = 5000000
# sys.setrecursionlimit(limit_number) # 재귀제한 해제

N = int(input())
for i in range(1, N+1):
    print("*" * i)