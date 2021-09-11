k,t = map(int,input().split())
# 0 1 2 3 4 5 4 3 2 1 0 1  2  3 4 5
#  1 2 3 4 5 6 7 8 9 10  11 12
# 0 1 2 3 4 5 6 5 4 3  2
#  1 2 3 4 5 6 7 8 9 10
if( t <= k):
    print(t)
else:
    if((t//k)%2 ==0):
        print(t%k)
    else:
        print(k - (t%k))

