import sys
input = sys.stdin.readline
N, K = list(map(int, input().rstrip().split()))
N_lists = list(map(int, input().rstrip().split()))
window = sum(N_lists[0: K])
maxWindow = window
for n in range(K, N): # 범위 1 ~ n말고 K로 잡으면 간편함
    window = window - N_lists[n-K] + N_lists[n]
    if window > maxWindow:
        maxWindow = window

print(maxWindow)