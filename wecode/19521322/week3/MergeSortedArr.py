a,b = list(map(int,input().split()))
arr = list(map(int,input().split()))
arr1 = list(map(int,input().split()))
result = arr + arr1
result.sort()
print(*result,sep=" ")

