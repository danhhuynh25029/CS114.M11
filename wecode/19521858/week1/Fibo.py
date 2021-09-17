n= int(input())
def fibonacci(n):
    if n == 1 or n == 2: 
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)
if n<1 or n>30:
    print("So " ,n, " khong nam trong khoang [1,30].")
else:
    print(fibonacci(n))
