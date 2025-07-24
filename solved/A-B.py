# 짝수일때 나누고 홀수일때 더하기 + 검산
# dfs로도 풀이가능? 
A, B = list(map(int, input().split()))
B_reclac = B
recalc =  []
cnt = 1
while B > A:
    if B % 2 == 0:
        recalc.append('mult') # 2곱하기
        B = B // 2
        cnt +=1
    else:
        recalc.append('one') # 1추가
        B = int(B // 10)
        cnt +=1 

ok = False
recalc.reverse()

for r in recalc:
    if r == 'mult':
        A = A*2
    else:
        A = (A * 10 + 1)
    if A == B_reclac:
        ok = True
if ok:
    print(cnt)
else:
    print(-1)
