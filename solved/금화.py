t, x, m = list(map(int, input().split())) # 진행시간, 주울수있는 동전갯수, 몬스터 갯수
monster_min = 10000000

for _ in range(m):
    d, s = list(map(int, input().split())) 
    monster_min = min(monster_min, (d-1) // s) # 닿기전까지 몇번 주울 수 있나?
if monster_min == 0: # 0번 주울 수 있다면 거리가 제로(시작거리보다 뒤로 못감)
    print(0)
elif monster_min < t: # 주울 수 있는 
    print((monster_min + ((t - monster_min)//2)) * x)
else:
    print(t * x)

"""t, x, m = list(map(int, input().split())) # 진행시간, 주울 수 있는 동전 개수, 몬스터 개수
monsters = []

if m == 0:
    print(t * x)
else:

    for _ in range(m):
        d, s = list(map(int, input().split()))
        monsters.append([d, s, d]) # 위치 속도 첫위치치
        
    coin = 0 # 금화를 주운 횟수
    
    # 총 t번의 행동을 반복
    for time_unit in range(t): 
        can_pick_this_turn = True # 금화?
        
        for monster in monsters:
            if (monster[0] - monster[1]) <= 0: 
                can_pick_this_turn = False 
                break 
                
        if can_pick_this_turn: # 이번 턴에 금화를 주울 수 있다면
            for monster_info in monsters:
                monster_info[0] -= monster_info[1] 
            coin += 1 
        else: 
            for monster_info in monsters:
                
                monster_info[0] = min(monster_info[2], monster_info[0] + monster_info[1])
    
    print(coin * x) """