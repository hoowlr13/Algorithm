from functools import reduce
N = reduce(lambda x, y: x * y, [int(input()) for _ in range(3)])
for i in range(10):
    print(str(N).count(str(i))) # 형변환 생각, 문자열도 .count()로 셀수있음 
