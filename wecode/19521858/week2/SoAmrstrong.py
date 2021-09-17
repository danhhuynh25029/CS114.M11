num = int(input())
n = len(str(num))
sum = 0
temp = num
while temp > 0:
   lastNum = temp % 10
   sum += lastNum ** n
   temp //= 10
if num == sum:
   print("True")
else:
   print("False")