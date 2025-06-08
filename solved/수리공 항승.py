N, L = list(map(int, input().split())) # 갯수, 길이
hole = list(map(int, input().split()))
hole.sort()
last_tape = -1
tape = 0
for h in hole:
    if h <= last_tape: # 마지막으로 붙인 테이프 길이가 포함되어있다면?
        pass
    else: # 테이프 길이가 부족하다면?
        tape += 1
        last_tape = (h-0.5 + L)
print(tape)