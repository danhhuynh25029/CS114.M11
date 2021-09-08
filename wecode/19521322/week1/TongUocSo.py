n = int(input())
result = 1
for i in range(2,n):
    if n % i == 0:
        result += i
print(result)
