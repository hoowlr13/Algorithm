"""Day Of Mourning의 기타리스트 강토가 사용하는 기타에서 N개의 줄이 끊어졌다. 
따라서 새로운 줄을 사거나 교체해야 한다. 강토는 되도록이면 돈을 적게 쓰려고 한다. 
6줄 패키지를 살 수도 있고, 1개 또는 그 이상의 줄을 낱개로 살 수도 있다.

끊어진 기타줄의 개수 N과 기타줄 브랜드 M개가 주어지고, 
각각의 브랜드에서 파는 기타줄 6개가 들어있는 패키지의 가격, 낱개로 살 때의 가격이 주어질 때, 
적어도 N개를 사기 위해 필요한 돈의 수를 최소로 하는 프로그램을 작성하시오.

입력
첫째 줄에 N과 M이 주어진다. N은 100보다 작거나 같은 자연수이고, M은 50보다 작거나 같은 자연수이다. 
둘째 줄부터 M개의 줄에는 각 브랜드의 패키지 가격과 낱개의 가격이 공백으로 구분하여 주어진다. 
가격은 0보다 크거나 같고, 1,000보다 작거나 같은 정수이다.

출력
첫째 줄에 기타줄을 적어도 N개 사기 위해 필요한 돈의 최솟값을 출력한다.

예제 입력 1 
4 2
12 3
15 4
예제 출력 1 
12
"""
# 완전히 최소를 만들려면 1. 세트랑 한개랑 전부 비교해서 제일 저렴한거 찾기 2. 만약 6개를 넘는다면? 그때는 세트 & 한개에서 제일 저럼한걸로 구매하기 
# 
import math
Need, M = list(map(int, input().split()))
pack = []
one = []
minString = 2 ** 18
money = 2 ** 18
for m in range(M):
    inp = list(map(int, input().split()))
    pack.append(inp[0])
    one.append(inp[1])

for packs in pack:
    if packs < (min(one) * 6) and packs < minString:
        minString = packs


cnt = (Need // 6)
if Need < 6:
    money = (min(one) * Need)
    for packs in pack:
        if packs < money:
            money = packs

else:
    if minString != 2 ** 18:
        money = (minString * cnt)
        chose = [(min(one) * (Need - (6 * cnt))), minString]
        money += min(chose)
    else:
        money = (min(one) * Need)

print(money)