import math
a = int(input())
b = int(input())
c = int(input())
if a+b>c and a+c>b and b+c>a:
    #1/2 Chu vi:
    p = (a+b+c)/2
    #Dien tich:
    s = math.sqrt(p*(p-a)*(p-b)*(p-c))
    s = round(s,2)
    if (s==int(s)):
        s=int(s)
    if a==b==c:
        print('Tam giac deu, dien tich = ',s)
    elif a==b or a==c or c==b:
        print('Tam giac can, dien tich = ',s)
    elif a^2 +b^2==c^2 or a^2 +c^2 ==b^2 or b^2 +c^2 == a^2:
        print('Tam giac vuong, dien tich = ', s)
    else:
        print('Tam giac thuong, dien tich = ', s)
else:
    print('Khong phai tam giac') 
