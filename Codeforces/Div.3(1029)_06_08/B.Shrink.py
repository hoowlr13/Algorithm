repeat = int(input())
for _ in range(repeat):
    N = int(input())
    lists = [1]
    for _ in range(N, 1, -1):
        lists.append(_)
    cnt = 0
    """for l in range(1, len(lists)-1):
        if lists[l-1] < lists[l] and lists[l+1] < lists[l]:
            del lists[l]
            cnt +=1
        """
    print(*lists)
