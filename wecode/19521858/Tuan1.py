#BAI1
# n = int(input())
# S=0
# def TongUocSo(S,n):
#     for i in range(1,n-1):
#         if (n%i==0):
#             S=S+i
#     return S
# print(TongUocSo(S,n))

#BAI2
# n= int(input())
# def fibonacci(n):
#     if n == 1 or n == 2: 
#         return 1
#     return fibonacci(n - 1) + fibonacci(n - 2)
# if n<1 or n>30:
#     print("So " ,n, " khong nam trong khoang [1,30].")
# else:
#     print(fibonacci(n))

#BAI3 
# import math
# a = int(input())
# b = int(input())
# c = int(input())
# if a+b>c and a+c>b and b+c>a:
#     #1/2 Chu vi:
#     p = (a+b+c)/2
#     #Dien tich:
#     s = math.sqrt(p*(p-a)*(p-b)*(p-c))
#     s = round(s,2)
#     if (s==int(s)):
#         s=int(s)
#     if a==b==c:
#         print('Tam giac deu, dien tich = ',s)
#     elif a==b or a==c or c==b:
#         print('Tam giac can, dien tich = ',s)
#     elif a^2 +b^2==c^2 or a^2 +c^2 ==b^2 or b^2 +c^2 == a^2:
#         print('Tam giac vuong, dien tich = ', s)
#     else:
#         print('Tam giac thuong, dien tich = ', s)
# else:
#     print('Khong phai tam giac') 


#Bai 4
# psi = float(input())
# from decimal import*
# getcontext().prec=6
# print(Decimal(psi*0.453592/2.54/2.54).normalize())

#bại5
# import math
# k, t = map(int,input().split())
# if (t//k)%2==0:
#     print(t%k)
# else:
#     print(k-t%k)

# Bai6
# F = float(input())
# from decimal import*
# getcontext().prec=6
# C = (float)((F-32)/1.8)
# K = C + 273.15
# print(Decimal(C).normalize(),Decimal(K).normalize())

# Bai7
# x, y = map(int,input().split())
# b = int((1/2)*y -x)
# a = int(x -b) 
# print(a,b)


#bai 8
n = int(input())
k = int(input())
p = int(input())
q = int(input())

if k > n: 
    print(-1)
if (k%2==0):
    new_q = q
else:
    if(q==1):
        new_q = 2
    else:
        new_q = 1
if (p-1)*2+ q-1 -k >=0:
    new_p = ((p-1)*2+ q-1 -k)//2 +1
    print(new_p,new_q)
elif (p-1)*2 + q-1 + k <= n-1:
    new_p = ((p-1)*2+ q-1 +k)//2 +1
    print(new_p,new_q)
else:
    print(-1)
