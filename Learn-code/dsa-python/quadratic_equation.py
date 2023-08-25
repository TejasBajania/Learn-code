import cmath 

# D = b^2 - 4ac
# x1, x2 = (-b+root(D))/2a,(-b-root(D))/2a

a = 1
b=5
c =6
D = b**2 - 4*a*c
x1, x2 = (-b+cmath.sqrt(D))/2*a,(-b-cmath.sqrt(D))/2*a

print(x1,x2)