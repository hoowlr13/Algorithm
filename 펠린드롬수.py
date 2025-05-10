from bisect import bisect_left, bisect_right
import sys
import math
from collections import deque
# input = sys.stdin.readline
# print = sys.stdout.write
count = 0
check = True
def pellindrom(N,count):
    length = len(N)
    for i in range(length // 2):
        if N[i] != N[length -1 - i]:
            return False
    
    return True
    
while True:
    N = list(map(int, input()))
    if N[0] == 0 and len(N) == 1:
        break
    elif pellindrom(N, count):
        print("yes")
    else:
        print("no")