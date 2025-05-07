N = int(input(), 2)
print(format(N, 'o'))
    

""" 시간초과로 실패
from collections import deque
import sys
input = sys.stdin.readline
print = sys.stdout.write

N = list(map(int, input().rstrip()))

if len(N) % 3 != 0:
    N = [0] * (3 - len(N) % 3) + N # O(n)

result = ""
for i in range(0, len(N), 3): # O(n) 길이가 100만이되면 시간초과

    # print(cnt)   
    answer = (N[i] * 4) + (N[i+1] * 2) + (N[i+2] * 1)
    result += str(answer)

print(result)
"""

""" ai정답
import sys 
input = sys.stdin.readline
print = sys.stdout.write

binary = input().rstrip()
# 3의 배수 길이로 패딩
binary = '0' * ((3 - len(binary) % 3) % 3) + binary

# 미리 계산된 결과값 사용
OCTAL = ['0','1','2','3','4','5','6','7']

for i in range(0, len(binary), 3):
    # 직접 계산
    val = (int(binary[i]) << 2) + (int(binary[i+1]) << 1) + int(binary[i+2])
    print(OCTAL[val])"""