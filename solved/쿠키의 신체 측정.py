# 최적화 실패
N= int(input())
cookie = []
for n in range(N):
    check = list(input())
    cookie.append([])
    for append in check:
        cookie[n].append(append)      


heart =[0,0]
heart_check = False
right = 0
left = 0
waist = 0
waist_last = 0
left_foot = -1
right_foot = -1
for i in range(N):
    for j in range(N):
        if cookie[i][j] == "*" and heart_check is False:
            heart = [i,j]
            heart_check = True
            continue
        
        if i == heart[0]+1:
            if j< heart[1] and cookie[i][j] == "*":
                left +=1
            if j> heart[1] and cookie[i][j] == "*":
                right +=1

        if i >= heart[0]+2:
            if cookie[i][heart[1]] == "*" and j == heart[1]:
                waist +=1
                waist_last = i-1
        if waist_last < i and cookie[i][heart[1]-1] == "*" and j == heart[1]-1:
            left_foot +=1
        if waist_last < i and cookie[i][heart[1]+1] == "*" and j == heart[1]+1:
            right_foot +=1

print(heart[0]+2,heart[1]+1)

print(left,right,waist,left_foot,right_foot)