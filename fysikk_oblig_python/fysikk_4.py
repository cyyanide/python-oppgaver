# OPPGAVE 4 

import math 

y = 50
y0 = 0
g = 9.81 
C = 0.000385 # kg/m
m = 0.00567 # kg 
v0 = 0
v = math.sqrt(v0**2 + 2*g*(y-y0)) # bevegelsesligning 
a = -g + ((C/m) * v**2) 


# kinetisk energi uten luftmotstand 
ek_utenlm = m/2 * v**2


# kinetisk energi med luftmotstand

v2 = math.sqrt(m*g/C) 
ek_medlm = m/2 * v2**2 

print("Kinetisk energi uten luftmotstand er lik ", ek_utenlm, "J")
print("Kinetisk energi med luftmotstand er lik ", ek_medlm, "J")










