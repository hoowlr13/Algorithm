repeat = int(input())
for i in range(repeat):
    N = list(map(str, input().split()))
    print(f"Case #{i+1}:", end=" ")
    answer = []
    for j in range(len(N), 0, -1):
        answer.append(N[j-1])
    
    
    print(*answer)