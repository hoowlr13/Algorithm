import sys
print = sys.stdout.writelines
N = int(input())
cnt =0
moved = []
print(f"{2** N -1}\n")

def move(N, start, to):
    print(f"{start} {to}\n")

def hanoi(N, start, to, via):
    if N == 1:
        move(1, start, to)
    else:
        hanoi(N-1, start, via, to)
        move(N, start, to)
        hanoi(N-1, via, to, start)  
if N <= 20: # ㅋㅋ
    hanoi(N, 1, 3, 2)
