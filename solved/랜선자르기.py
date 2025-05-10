K, N = list(map(int, input().split()))
line = [int(input()) for _ in range(K)]
start = 1
end = max(line)
answer = []

while start <= end:
    mid = (start + end) // 2
    cnt = sum(i // mid for i in line)
    if cnt >= N:
        answer.append(mid)

        start = mid+1
    else:
        end = mid -1
print(max(answer))
    
"""
1. 자를 랜선을 가장긴 랜선길이에 비교
2. 만약 가장짧은 랜선길이에 포함된다면 전부 나눠서 cnt세기  
3. cnt가 맞다면 answer 배열에 추가 아니라면 다시 (더 커도 괜찮음)
4. 그렇게 min <= max 까지 끝내고 가장 큰값 출력
"""
