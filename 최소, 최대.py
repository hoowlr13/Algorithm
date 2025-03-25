from bisect import bisect_left, bisect_right
import sys
import math
from collections import deque, defaultdict
# input = sys.stdin.readline
repeat = int(input())
N = list(map(int, input().split()))
print(f"{min(N)} {max(N)}")