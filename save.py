from bisect import bisect_left, bisect_right
import sys
import math
from collections import deque
# input = sys.stdin.readline
# print = sys.stdout.write
N = int(input())
first_hole = []
second_hole = [] * (100 * N) 
thrid_hole = [] * (100 * N)
for i in range(N, 0, -1):
    first_hole.append(i)
      



# idea 2 => 
# 1번순위 = 3번링에 먼저 숫자를 넣는다 
# 단 3번링에 숫자가 있을경우 2번링에 넣는다 그후 3번링에 들어간 숫자들을 2번링에 넣는다
# 3번링이 비어있다면? 3번링에 넣는다 그리고 2번링이 차있다면 2번링을 3번링에 넣는다 
# 여기서 is sort? 인지 검사하여야함함
# 

"""세 개의 장대가 있고 첫 번째 장대에는 반경이 서로 다른 n개의 원판이 쌓여 있다. 
각 원판은 반경이 큰 순서대로 쌓여있다. 이제 수도승들이 
다음 규칙에 따라 첫 번째 장대에서 세 번째 장대로 옮기려 한다.

한 번에 한 개의 원판만을 다른 탑으로 옮길 수 있다.
쌓아 놓은 원판은 항상 위의 것이 아래의 것보다 작아야 한다.
이 작업을 수행하는데 필요한 이동 순서를 출력하는 프로그램을 작성하라.
단, 이동 횟수는 최소가 되어야 한다.

아래 그림은 원판이 5개인 경우의 예시이다."""





"""while True:
    if not first_hole:
        if  not second_hole:
            break
    else:
        current = first_hole.pop()

    while True:
        if  not thrid_hole or current < thrid_hole[-1]:
            thrid_hole.append(current)
        elif not second_hole or current < second_hole[-1]:
            second_hole.append(current)
        elif second_hole[-1] > thrid_hole[-1]:
            current = thrid_hole.pop()
"""
# idea 1 => 재귀적인 방식이 아님
# hole에 원반이 비어있을때 넣는동작 ok 그다음 elif문을 사용해서 원반이 차있다면
# third second의 [-1] 값을 비교해서 낮은값을 pop해서 높은쪽 위로 옮긴다
 