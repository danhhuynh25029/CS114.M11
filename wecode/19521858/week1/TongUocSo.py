n = int(input())
S=0
def TongUocSo(S,n):
    for i in range(1,n-1):
        if (n%i==0):
            S=S+i
    return S
print(TongUocSo(S,n))