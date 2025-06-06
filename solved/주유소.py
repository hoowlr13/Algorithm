# 기름값의 우선순위
N = int(input())
length = list(map(int, input().split()))
oil = list(map(int, input().split()))
nextOil = oil[0] 
del oil[0]
length_plus = 0
money = 0
for now in range(N-1):
    if nextOil < oil[now]: # 아까 주유소가 더 싸다면? -> 이번 주유소는 패스한다.
        length_plus += length[now]
    else: # 만약 새로운 주유소가 더 싸다면?
        length_plus += length[now]
        money += (length_plus * nextOil)
        length_plus = 0
        nextOil = oil[now] 

money += (length_plus * nextOil)
print(money)

