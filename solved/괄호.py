def no():
    print('NO')

def yes():
    print("YES")

repeat = int(input())
for r in range(repeat):
    N = list(input())
    if N[0] == ')':
        no()
        continue

    valanceCheker = 0
    isVaild = True

    for n in N:
        
        if n == '(':
            valanceCheker +=1
        else:
            valanceCheker -=1
        
        if valanceCheker < 0:
            isVaild = False
            no()
            break

    else: # break없이 끝났을때
        if valanceCheker == 0:
            yes()
        else:
            no()
