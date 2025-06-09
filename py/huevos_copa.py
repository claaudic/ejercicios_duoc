import math
temperatura = float (input("Ingrese la temperatura del huevo "))
m = 47 
p = 1.038 
c = 3.7
k = 5.4*10**-3
pi= math.pi
t = (m**(2/3)* c*p**(1/3))/ ((k *pi**2)*(4*pi/3)**(2/3))*math.log (0.76*((temperatura - 100) /(70-100)))
print(t)