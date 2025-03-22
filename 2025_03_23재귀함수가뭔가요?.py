from bisect import bisect_left, bisect_right
import sys
import math
from collections import deque
# input = sys.stdin.readline
# print = sys.stdout.write
# limit_number = 5000000
# sys.setrecursionlimit(limit_number) # 재귀제한 해제
# 깊이 들어간후 return되면 chat_bot뒤의 코드가 순차적으로 실행
# (2, 1) (2, 2) (2, 3) => (2, 3) (2, 2) (2, 1) 뒷코드 출력
repeat = int(input())
c = 0
check = False
print("어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.")
def chat_bot(N, count):
    under_bar = "____" * count
    if N == 0:   
        print(f"{under_bar}\"재귀함수가 뭔가요?\"")
        print(f"{under_bar}\"재귀함수는 자기 자신을 호출하는 함수라네\"")
        print(f"{under_bar}라고 답변하였지.")

        return
    print(f"{under_bar}\"재귀함수가 뭔가요?\"")
    print(f"{under_bar}\"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.")
    print(f"{under_bar}마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.")
    print(f"{under_bar}그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어.\"")
    chat_bot(N-1, count+1)
    print(f"{under_bar}라고 답변하였지.")


chat_bot(repeat, c) 
"""
어느 한 컴퓨터공학과 학생이 유명한 교수님을 찾아가 물었다.
"재귀함수가 뭔가요?"
"잘 들어보게. 옛날옛날 한 산 꼭대기에 이세상 모든 지식을 통달한 선인이 있었어.
마을 사람들은 모두 그 선인에게 수많은 질문을 했고, 모두 지혜롭게 대답해 주었지.
그의 답은 대부분 옳았다고 하네. 그런데 어느 날, 그 선인에게 한 선비가 찾아와서 물었어."
"""
