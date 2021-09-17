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