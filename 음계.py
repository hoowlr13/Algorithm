from bisect import bisect_left, bisect_right
import sys
import math
from collections import deque, defaultdict
# input = sys.stdin.readline

ascending = [1,2,3,4,5,6,7,8]
descending = [8,7,6,5,4,3,2,1]
N = list(map(int, input().split()))
if N == ascending:
    print("ascending")
elif N == descending:
    print("descending")
else:
    print("mixed")