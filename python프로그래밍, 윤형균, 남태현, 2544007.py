"""
*****
*****
*****
*****
*****
"""
# 1번 
for i in range(5): 
    for j in range(5): 
        print("*", end="") # for 반복중에 줄바꿈되면 안되니 end=""로 방지하였습니다
    print() # 한줄 출력이 끝나면 줄바꿈합니다

"""
2. 
*
**
***
****
"""
# 2번
for i in range(1, 5):
    for j in range(i): # 인자를 i로 받아 i가 증가한만큼 별도 더 출력됩니다
        print("*", end="")
    print()

"""
3. 
**** 
 ***
  **
   *
"""
# 3번
cnt = 0 # 공백의 숫자를 세는 변수입니다
for i in range(5, 1, -1):
    print(f"{cnt * ' '}",end= "") # 별을 출력하기전 공백을 먼저 출력합니다

    for j in range(1, i): 
        print("*", end= "")

    cnt +=1 # 공백의 갯수를 추가하기위해 +1을 해줍니다
    print()

"""
4. 
*****
 *** 
  * 
"""
# 4번 
cnt = 0
for i in range(6, 1, -1):
    if i % 2: # 별의 길이가 짝수일때는 continue를 해줍니다
        continue
    print(f"{cnt * ' '}",end= "") 
    
    for j in range(1, i):
        print("*", end="")

    cnt +=1
    print()
"""
5. 
  *
 ***
*****
 ***
  * 
"""
# 5번
cnt = 2
starCtnt = 1 # 별의 갯수를 세는 변수입니다
for i in range(1, 11):
    if i % 2:
        continue
    print(f"{cnt * ' '}", end= "")
    
    for j in range(starCtnt): # starCnt를 인자로 받아서 별을 출력합니다
        print("*", end="")
    
    if i < 6: # i가 6 미만이라면 공백 -1, 별의 갯수 +2를 해줍니다
        cnt -= 1
        starCtnt +=2
    else: # i가 6이상일경우 반대로 해줍니다
        cnt +=1
        starCtnt -=2

    print()
