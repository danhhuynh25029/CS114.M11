import math
a = int(input())
b = int(input())
c = int(input())
if(a + b <= c or c + b <= a or a + c <= b):
    print("Khong phai tam giac")
else:
    result = round(math.sqrt((a+b+c)*(a+b-c)*(b+c-a)*(a+c-b))/4,2)
    if(result*10%10 == 0):
        result = int(result)
    if(a == b and b == c):
        print(f"Tam giac deu, dien tich = {result}")
    elif(a == b or b == c or c == a):
        print(f"Tam giac can, dien tich = {result}")
    elif(c == math.sqrt(a**2+b**2) or b == math.sqrt(a**2+c**2) or a == math.sqrt(b**2+c**2)):
        print(f"Tam giac vuong, dien tich = {result}")
    else:
        print(f"Tam giac thuong, dien tich = {result}")
        
