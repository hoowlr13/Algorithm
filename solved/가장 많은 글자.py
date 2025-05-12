from collections import defaultdict

many = defaultdict(int)
answer = []
while True:
    try:
        N = input()
        Strip = N.replace(' ','') # replace => 값을 받을변수가 있어야한다
        for i in Strip:
            many[i] +=1

    except EOFError:
        break

answer = [k for k, v in many.items() if v == max(many.values())]

print(''.join(sorted(answer)))