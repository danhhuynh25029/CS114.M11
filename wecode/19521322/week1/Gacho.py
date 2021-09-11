x,y = map(int,input().split())
# y = 4*c + 2*g
# x = c + g
# y = 4*(x-g) + 2*g
# y = 4x - 4g + 2g
# y = 4x - 2g
# g = (4x-y)/2
g = (4*x - y)//2
c = x - g
print(f"{g} {c}")
