N = int(input())
cnt = N-1
for i in range(N):
    print(f"{" " * cnt}{"*" * (i*2+1)}")
    cnt -=1
for j in range(N-1, 0, -1):
    cnt +=1
    print(f"{" " * (cnt+1)}{"*" * (j*2-1)}")
    