import math
def heron(a,b,c):
    s = 0.5*(a+b+c)
    print('The value of s is', s)
    return math.sqrt(s * (s-a) * (s-b) * (s-c))
print(heron(1,1,1))
