"""FizzBuzz 문제는 
$i = 1, 2, cdots$ 에 대해 다음 규칙에 따라 문자열을 한 줄에 하나씩 출력하는 문제입니다.

 
$i$가 
$3$의 배수이면서 
$5$의 배수이면 “FizzBuzz”를 출력합니다.
 
$i$가 
$3$의 배수이지만 
$5$의 배수가 아니면 “Fizz”를 출력합니다.
 
$i$가 
$3$의 배수가 아니지만 
$5$의 배수이면 “Buzz”를 출력합니다.
 
$i$가 
$3$의 배수도 아니고 
$5$의 배수도 아닌 경우 
$i$를 그대로 출력합니다.
FizzBuzz 문제에서 연속으로 출력된 세 개의 문자열이 주어집니다. 
이때, 이 세 문자열 다음에 올 문자열은 무엇일까요?"""
# 아 뻘짓했네
# fizzbuzz문제 규칙찾은다음 dictionary에 넣고
# 그거에 맞춰서 출력하면 해결

N = [str(input()) for _ in range(3)]
answer = []
cheek = False
for i in range(3):
    if N[i].isdigit():
        cheek = True
        now = int(N[i]) + (3-i)    
        if now % 3 == 0:
            if now % 5 == 0:
                print("FizzBuzz")
            else:
                print("Fizz")
        elif now % 5 == 0:
            print("Buzz")
        else:
            print(now)
    
"""
cnt = 0
while not cheek:
    if cnt % 3 == 0:
        if cnt % 5 == 0:
                answer.append("FizzBuzz")
        else:
                answer.append("Fizz")
    elif cnt % 5 == 0:
        answer.append("Buzz")
    else:
        answer.append(str(cnt))
    
    cnt += 1






"""

