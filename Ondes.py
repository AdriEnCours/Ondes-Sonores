
import numpy as np 
import matplotlib.pyplot as plt
import mpmath as mp

#Préparation

#On laisse définir les parametres l, m et n par l'utilisateur
l = 2
m = 3
n = 8

#Taille de la salle
Lx = 6
Ly = 8
Lz = 3


#Dimmension du cylindre
a = 5
L = 50


#Définition des parametres des équations
A = 1
c = 340 #vitesse du son dans l'air a 15°C (m/s)
t = 0

#calculs

w1 = c*np.sqrt(((l*np.pi/Lx)**2)+((m*np.pi/Ly)**2)+((n*np.pi/Lz)**2))

#On défini la fonction de P
def f(x, y):
    return  A*np.cos(x*l*np.pi/Lx)*(y*m*np.pi/Ly)*(z*n*np.pi/Lz)*np.exp(l*w1*t)

nb = 150 #nombre de points sur la figure
x = np.linspace(-Lx/2, Lx/2, nb)
y = np.linspace(-Ly/2, Ly/2, nb)
z = np.linspace(-Lz/2, Lz/2, nb)
X, Y = np.meshgrid(x, y)  #Maillage sur le plan x, y, z0
TXY = f(X, Y)

plt.figure(figsize=(12, 10))

plt.subplot(2,2,1)
plt.pcolor(X, Y, TXY, cmap='hsv', shading='auto')
plt.colorbar(shrink=0.9)
plt.title('Cartogaphie du champ de pression sur le plan X,Y,Z0')
plt.xlabel("X", size = 15,)
plt.ylabel("Y", size = 15)



Y2, Z = np.meshgrid(y, z) #Maillage sur le plan x0, y, z
TYZ = f(Y2, Z)

plt.subplot(2,2,2)
plt.pcolor(Y2, Z, TYZ, cmap='hsv', shading='auto')
plt.colorbar(shrink=0.9)
plt.title('Cartogaphie du champ de pression sur le plan X0,Y,Z')
plt.xlabel("Y", size = 15)
plt.ylabel("Z", size = 15)



plt.subplot(2,2,4)
fig1 = plt.contour(Y2,Z,TYZ, cmap='jet')
plt.clabel(fig1)
plt.plot([0],[0], "o")
plt.title('lignes isobares sur le plan X0,Y,Z')
plt.xlabel("Y", size = 15)
plt.ylabel("Z", size = 15)


plt.subplot(2,2,3)
fig2 = plt.contour(X,Y,TXY, cmap='jet')
plt.plot([0],[0], "o")
plt.clabel(fig2)
plt.title('lignes isobares sur le plan X,Y,Z0')
plt.xlabel("X", size = 15,)
plt.ylabel("Y", size = 15)


#On passe a la partie cylindrique 

#Calcul de Xi
def BesselSpe(a, b):
    return mp.besseljzero(a, b, 1)



#Calcule de w
w2 = c*np.sqrt((l*np.pi/L)**2+(BesselSpe(m,l)/a)**2)


#Mise en place des fonctions nécessaires au calcul de P2
def Bessel(m,x):
    return  mp.besselj(m,x)

#On défini la fonction de P2
def f2(r, th):
    return A*Bessel(m, x2)*np.cos(m*th)*np.cos((l*np.pi*z2)/L)

x2 = (BesselSpe(m, l)/a) 
z2 = np.linspace(0, L, 360)


th =  np.linspace(0, 2*np.pi, 20)
r = np.linspace(0, a, 360)



R, TH = np.meshgrid(r, th)  #Maillage sur le plan r, theta, z0
Tcyl = f2(R, TH) 



fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
fig3 = ax.contourf(TH, R, Tcyl)
plt.colorbar(fig3)
plt.title('Champ de pression en coordonées polaire')


fig, ax = plt.subplots(subplot_kw=dict(projection='polar'))
fig4 = ax.contour(TH, R, Tcyl)
plt.colorbar(fig4)
plt.title('Lignes isobares')

plt.show()