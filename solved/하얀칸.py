cnt = 0
for i in range(8):
    N = list(map(str, input()))
    for j in range(8):
        if not j % 2 and not i % 2:
            if N[j] == "F":
                cnt +=1         
        if j % 2 and i % 2:
            if N[j] == "F":
                cnt +=1      
print(cnt)