# 최솟값으로 정렬, 현재cnt계속갱신
human = int(input())
cnt = sorted(map(int, input().split()))

total = [sum(cnt[:i+1]) for i in range(len(cnt))]

print(sum(total))