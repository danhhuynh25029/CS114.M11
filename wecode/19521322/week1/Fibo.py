x = int(input())
def fibo(x:int)->int:
    if(x == 1 or x == 2):
        return 1
    else:
        return fibo(x-1) + fibo(x-2)

if(x < 1 or x > 30):
    print(f"So {x} khong nam trong khoang [1,30].")
else:
    print(fibo(x))
    
