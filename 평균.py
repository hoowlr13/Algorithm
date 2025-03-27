repeat = int(input())
N = list(map(int, input().split()))
answer = 0
for i in N:
    answer += i /max(N)

print(answer * 100 / len(N))