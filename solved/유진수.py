N = input()

check = False
for i in range(1, len(N)):
    first= 1
    last = 1    
    for x in N[0:i]:
        first *= int(x)
    
    for y in N[i:len(N)]:
        last *= int(y)
        if last > first:
            break
    
    if first == last:
        print("YES")
        check = True
        break
if not check:
    print("NO")