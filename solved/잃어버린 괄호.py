# 아이디어 -> 굳이 괄호를 구현할 필요가 없음 -가 나오면 어떻게 묶던 다 빼는것이기에 똑같음
q = input()
string = ""
zeroCheck = False
for char in q:
    if zeroCheck and char == "0":
        continue
    elif char is ("+" or "-") and not zeroCheck:
        string += char
        zeroCheck = True

    else:
        string += char
        zeroCheck = False


nums = ""
minusCheck = False
answer = 0
for s in string:
    if s.isdigit() and 0 <= int(s) <= 9:
        nums += s
    else: # 기호 만났을때
        if not nums:
            nums = "0"
        if minusCheck:
            answer -= int(nums)    
            nums = ""

        elif s == "+" or not minusCheck:
            answer += int(nums)
            nums = ""
            
        if s == "-":
            minusCheck = True
            
if nums:
    if minusCheck:
        print(answer - int(nums))
    else:
        print(answer + int(nums))    
else:
    print(answer)    
        
"""
폐기
40 - 50 + 30
이면 마이너스가 나오기전까지 모든 수를 더한다 
마이너스가 나왔다면 그뒤는 모
내가 해야될 작업
-연산자가 1개가 될때까지 이 작업을 반복한다.
먼저 저장할 문자열을 이전문자열과 이후 문자열로 나눈다 코드의 구조는
while
    부호 갯수체크
    if 마이너스가 1개이하라면
        break
    else:
        for 이전문자열 돌리기
            if 저장된 연산자가 있는가?
                if 이전숫자가 차있는가?
                    if 이후숫자가 차있는가?
                        이전숫자 = int(이전숫자) + int(이후숫자)
                    else:
                        이전숫자 = true
                이후 문자열 += s
                저장된 연산자 = true
            elif 저장된 연산자가 있다면 
                if 연산자가 +라면
                    이후 문자열 += s
                if 연산자가 -라면
                    if 이전숫자 == false
                        이전숫자 += s
                    else:
                        이후숫자 += s
                    
    이전문자열 = 이후문자열
    이후문자열 = ""
    의 구조로 진행
1. 저장된 연산자가 없으면 연산자를 
2. 연산자가 있다면 연산자
3-1. 다음 연산자가 +라면 다음 숫자를 새로운 변수에 저장한다
    3-1-1. 다음 연산자도 + 라면 새로운 숫자를 이전 숫자에 int로 더한다
    3-1-2. 다음 연산자가 - 라면 여태까지 이전숫자를 모두 정답란에 더한다 정답란에 더하는건 - 로 더한다
3-2. 다음 연산자가 + 라면 그대로 놔둔다  
"""

# 마지막엔 기호가없으니 생각해야됨