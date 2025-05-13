N, M = input().split()
answer = 0
for n in N:
    for m in M:
        answer += int(n) * int(m)

print(answer)