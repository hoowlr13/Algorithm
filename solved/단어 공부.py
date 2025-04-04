N = input()
nUpper =  N.upper()
answer = {}
for n in nUpper:
    if not n in answer:
        answer[n] = 1
    else:
        answer[n] +=1

maxValue = max(answer.values())

maxChar = [key for key, Value in answer.items() if Value == maxValue] 
# [반환값, for _ in 반복 뒤에 if선언가능]
if len(maxChar) > 1:
    print("?")
else:
    print(*maxChar)
