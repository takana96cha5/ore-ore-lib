def fibonacci(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    return fibonacci(n-1) + fibonacci(n-2)

# 末尾再帰
def fibonacciTail(n:int) -> int:
    return fibonacciTailHelper(0,1,n)

def fibonacciTailHelper(f1,f2,n) :
    if n == 0: return f1
    return fibonacciTailHelper(f2,f1+f2,n-1)

print(fibonacci(5)) # 5
print(fibonacci(9)) # 34
print(fibonacci(10)) # 55
print(fibonacci(19)) # 4181

print(fibonacciTail(5)) # 5
print(fibonacciTail(9)) # 34
print(fibonacciTail(10)) # 55
print(fibonacciTail(19)) # 4181
