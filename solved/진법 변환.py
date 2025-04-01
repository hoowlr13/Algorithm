N, M = list(map(str, input().split()))
mBase = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ" 
cnt = len(N)-1
answer = 0
for n in N:

    for m in range(int(M)):
        if n == mBase[m]:
            answer += int(m * (int(M) ** cnt)) # 진법 변환 > 숫자값 * (n진법 ^ 자릿수)
            break
    cnt -=1
print(answer)