N = int(input())
answer = 1
def factorial(n):
    global answer
    if n == 0:
        return 1
    answer = answer * n
    factorial(n-1)
    return answer
print(factorial(N))