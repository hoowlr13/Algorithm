from collections import deque
N, M = list(map(int, input().split()))
nums = list(map(int, input().split()))

q = deque(range(1, N+1))

answer = 0
for n in nums:
    idx = q.index(n)

    # 왼쪽으로 뽑는게 더 가까울 때
    if idx <= len(q) // 2:
        q.rotate(-idx)
        answer += idx
    # 오른쪽으로 뽑는게 더 가까울 때
    else:
        q.rotate((len(q)-idx))
        answer += (len(q)-idx)

    q.popleft()

print(answer)