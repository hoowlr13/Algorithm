import math
N = int(input())
shirts = list(map(int, input().split()))
maxshirts = max(shirts)
T, P = map(int, input().split())
shirtsCnt = 0
for s in shirts:
    shirtsCnt += math.ceil(s / T)

print(shirtsCnt)
print(f"{N // P} {N % P}")