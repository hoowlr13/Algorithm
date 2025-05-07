import sys
input = sys.stdin.readline
print = sys.stdout.write

a, b = list(map(int, input().strip().split()))
N = [input().strip() for _ in range(a)]

poketName = {}
poketCount = {}

for i in range(len(N)):
    poketName[N[i]] = i + 1 
    poketCount[i + 1] = N[i]

M = [input().strip() for _ in range(b)]
for m in M:
    if m.isdigit():
        number = int(m)
        for key, value in poketCount.items():
            if number == key:
                print(f"{value}\n")
                break
                
    else:
        print(f"{poketName[m]}\n")