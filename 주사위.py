from collections import defaultdict
one, two, three = list(map(int, input().split()))
answer = defaultdict(int)
for i in range(1, one+1):
    for j in range(1, two+1):
        for k in range(1, three+1):
            answer[(i+j+k)] += 1
sortanswer = sorted(answer.items(), key=lambda x: x[1]) # 반환은 튜플   

anx = [k for k, v in sortanswer if v == sortanswer[-1][1]] 
print(min(anx))