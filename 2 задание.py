import math

x = 3.981 * 10**-2
y = -1.625 * 10**3
z = 0.512

s = 2**(-x)*(x+abs(y)**0.25)**0.5*(math.exp(x-1/math.sin(z)))**(1/3)
print(f"s ≈ {s:.5f}")