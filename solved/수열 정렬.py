"""예제 입력 1 
3
2 3 1

a[0] = 2 = b[p[0]]
a[1] = 3 = b[p[1]]
a[2] = 1 = b[p[2]] = 요게 제일 처음으로 들어가기-> b[0]이 되야함. -> p[2] = 0
b를 기준으로 1 2 3 이렇게 배열하라. 
인거니 b[p[2]] = 1,  p[2] = 0이 되어야함
이렇게 간다면?
p[0] = 1
p[1] = 2
이니 p[0] ~ p[2]의 값은 1, 2, 0이다.

예제 출력 1 
1 2 0

"""

N = int(input())
A = list(map(int, input().split()))
sequence = {}
for a in range(0, len(A)):
    sequence[a] = A[a] # key = P-idx, value = A-value

sorted_seq = sorted(sequence.items(), key= lambda item: (item[1], item[0]))

answer = [0] * N
for new_idx in range(N):
    answer[sorted_seq[new_idx][0]] = new_idx
print(*answer)
    
