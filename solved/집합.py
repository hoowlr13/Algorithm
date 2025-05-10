# pypy3 -> 메모리많이먹음, 속도빠름 python3 -> 메모리 적게먹는대신 속도느림
import sys
input = sys.stdin.readline
print = sys.stdout.write
S = set()
repeat = int(input().rstrip())

for i in range(repeat):
    
    N = list(map(str, input().rstrip().split()))
    if N[0] == "add":
        S.add(N[1])
    elif N[0] == "remove":
        if N[1] in S:
            S.remove(N[1])
    elif N[0] == "check":
        if N[1] in S:
            print("1\n")
        else:
            print("0\n")
    elif N[0] == "toggle":
        if N[1] in S:
            S.remove(N[1])
        else:
            S.add(N[1])
    elif N[0] == "all":
        S = set(str(i) for i in range(1, 21)) 
    elif N[0] == "empty":
        S = set()