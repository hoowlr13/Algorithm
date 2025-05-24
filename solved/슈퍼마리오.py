N = [int(input()) for _ in range(10)]
ranks = []
ranks.append(0)

answer = {}
for n in N:
    ranks.append((n+ranks[-1]))

for r in range(len(ranks)):
    answer[r+1] = ranks[r]-100

sort_answer = sorted(answer.items(), key= lambda x: (abs(x[1]), x[0])) 
minKey = sort_answer[0]
for k, v in sort_answer:
    if abs(v) == abs(minKey[1]) and k > minKey[0]:
        minKey = (k, v)
        
    
print(minKey[1]+100)
    

