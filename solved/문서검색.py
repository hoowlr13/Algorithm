docs = input()
find = input()
length = len(find)
cnt = 0
findCnt = 0

for i in range(len(docs)):
    first = i + findCnt
    last = i + length + findCnt
    if (i + length) > len(docs):
        break
    elif find == docs[first: last]:
       cnt +=1 
       findCnt += (length - 1) # for i 에서 1씩 증가하는거 고려
    
print(cnt)