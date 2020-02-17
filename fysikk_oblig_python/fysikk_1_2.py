# OPPGAVE 1 OG 2 

import numpy as np
import matplotlib.pyplot as plt 

g = 9.81
y0 = 50
v0 = 0 
N = 2000 # antall elementer i times, må være stor 
tmin = 0
tmax = 6

C = 0.000385 # kg/m
m = 0.00567 # kg


times = np.linspace(tmin, tmax, N) #definerer 1xN-array med N diskrete t-verdier
dt = times[1] - times[0] #intervall mellom t-verdier 

y = np.zeros(N) # alle verdier settes til null
v = np.zeros(N) #Zeros - return a new array of given shape and type, filled with zeros 
a = np.zeros(N)

y[0] = y0 # starthoyden
v[0] = v0 # starthastigheten 

for n in range(0, N - 1, 1): # start, end, step 
    a[n] = -g + ((C/m) * v[n]**2) # setter akselerasjon i tidssteg n    // a = -g + ((C/m) * v**2) 
    
    v[n + 1] = v[n] + a[n]*dt # beregner hastighet et tidssteg fram
    y[n + 1] = y[n] + v[n]*dt # posisjon tidssteg fram 
    
a[N-1] = -g + ((C/m) * v[N-1]**2)   # a = -g + ((C/m) * v**2) 

# Plott av posisjon som funksjon av tid 

fig = plt.figure(1)
plt.ylim(0, 1.1*y0) # laveste verdi 0, hoyeste litt over slipphoyden
K1 = plt.plot(times, y, 'b') # plotter posisjonsgrafen
plt.title('Posisjon som funksjon av tid')
plt.xlabel('t (sekunder)') #symbol og enhet tidsaksen
plt.ylabel('y (meter)') # symbol og enhet på y-aksen
plt.show


# Plott av farten som funksjon av tid

fig = plt.figure(2) 
plt.ylim(0,30) # velger laveste og hoyeste verdi 
L1 = plt.plot(times, np.abs(v), 'b') # Plotter absolutverdi av hastigheten (dvs. farten)
plt.title('Fart som funksjon av tid')
plt.xlabel('t (sekunder)')
plt.ylabel('|V| (meter/sekund)')
plt.show

# Plott av akselerasjon som funksjon av tid 

fig = plt.figure(3)
plt.ylim(0, 11) # laveste og hoyeste verdi 
L1 = plt.plot(times, np.abs(a), 'b')
plt.title('Akselerasjon som funksjon av tid')
plt.xlabel('t (sekunder)')
plt.ylabel('|a| (meter/sekund^2)')
plt.show 












































