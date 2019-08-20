# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 18:03:28 2019

@author: Bruko
"""

import random
import numpy as np
import math
import colorsys

from pyvox.models import Vox, Color
from pyvox.writer import VoxWriter

L = 120	# Tamaño / city size 
N = 200 # Número de casas / building size
ven = 2 # Separación entre ventanas / space between windows
altura = 0.6	# 0: sin superposición, 1: gran superposición
probaLuz = 0.2
ciudad = 4 		# 1: Uniformemente distribuidas, 20: todos en un extremo / all buildings on one axis
saturacion = [0,10]	#0: casas grises / grey houses. 100, casas coloridas / colorful houses
valor = [70,100]	#0: casas oscuras / dark colored houses. 100, casas claras / light colored houses




M=np.zeros((L,L,L))
M=M.astype(int)



def cubo(a,b,c,x,y,z,colo):
	for i in range(a,a+x):
		for j in range(b,b+y):
			for k in range(c,c+z):
				if i<L and j<L and k<L:
					M[i,j,k]=colo


def ventanas(a,b,c,x,y,z,colo):
	
	an = random.randint(2,min(4,y-1))
	anc = random.randint(1,ven-1)
	for i in range(a,a+x):
		for k in range(c,c+z):
			for j in range(b+an,b+y-1,3):
				if i<L and j<L and k<L:
					# Es una ventana mirando hacia el sur
					if ( (a-i)%ven == anc and (k == c or k == c+z-1) and i!=a+x-1 ) or ( (c-k)%ven == anc and (i == a or i == a+x-1) and k!=c+z-1 ):
						if random.random()<probaLuz:
							M[i,j,k]=6
						else:
							M[i,j,k]=0



def borde(x0,z,y0,wx,xy,colo):
	for i in range(x0,x0+wx):
		for k in range(y0,y0+wy):
			if i<L and k<L and z<L:
				if (i == x0 or i == x0+wx -1 or k ==  y0 or k == y0 + xy -1 ):
					M[i,z,k]=colo
				elif M[i,z+1,k]==0:
					M[i,z,k]=0

def loMasBajo(posx,posy,wx,wy):
	elMin = L
	for i in range(posx,posx+wx):
		for j in range(posy,posy+wy):
			for k in range(L):
				if i<L and j<L and k<L:
					if M[i,k,j]==0 and elMin>k:
						elMin = k
	return elMin

def loMasAlto(posx,posy,wx,wy):
	elMax = 0
	for i in range(posx,posx+wx):
		for j in range(posy,posy+wy):
			for k in range(L):
				if i<L and j<L and k<L:
					if M[i,k,j]!=0 and elMax<k:
						elMax = k
	return (elMax+1)

def loMasMedio(posx,posy,wx,wy):
	return int((loMasAlto(posx,posy,wx,wy)*altura + loMasBajo(posx,posy,wx,wy)*(1-altura)))

def distribucion(x):
	x = x/L
	x = math.pow(x,ciudad)*L
	
	return int(x)



def invertir():
	b = M.copy()
	for i in range(L):
		for j in range(L):
			for k in range(L):
				if i<L and j<L and k<L:
					M[i,j,k]=b[i,L-j-1,k]




# Hacer el suelo
for i in range(L):
	for j in range(L):
		M[i,0,j]=random.randint(1,2)
		if random.random()<0.002:
			M[i,1,j]=3
			if random.random()<0.5:
				M[i,2,j]=3
				if random.random()<0.3:
					M[i,3,j]=3


# las casas
for i in range(N): # Número de casas
	posx = random.randint(0,L)
	posy = random.randint(0,L)
	
	posy = distribucion(posy)
	h = random.randint(3,6)
	if random.random()<0.5:
		wx = random.randint(10,13)
		wy = random.randint(5,7)
	else:
		wy = random.randint(10,13)
		wx = random.randint(5,7)
	# Pone la casa lo más abajo posible
	elMin = loMasBajo(posx,posy,wx,wy)
	elMax = loMasMedio(posx,posy,wx,wy)
	'''
	cubo(posx,elMin,posy,wx,h,wy,5)
	borde(posx,elMin+h,posy,wx,wy,5)
	ventanas(posx,elMin,posy,wx,h,wy,5)
	'''
	colek = random.randint(11,50)
	cubo(posx,elMin,posy,wx,elMax+h,wy,colek)
	borde(posx,elMax+h,posy,wx,wy,colek)
	ventanas(posx,elMin,posy,wx,elMax+h,wy,colek)


# Colores
pal = []
for i in range(255):
	pal.append(Color(75,75,75,0))


## Colores especiales
pal[0] = Color(210,210,157,0)
pal[1] = Color(200,200,147,0)
pal[2] = Color(137,172,120,0)
pal[3] = Color(155,255,0,0)
pal[4] = Color(195,195,185,0)
pal[5] = Color(245,255,169,0)

# Colores de las casas
for i in range(10,50):
	col = colorsys.hsv_to_rgb(random.random(), random.randint(saturacion[0],saturacion[1])/100, random.randint(valor[0],valor[1])/100)
	col = (int(col[0]*255),int(col[1]*255),int(col[2]*255))
	pal[i]=Color(col[0],col[1],col[2],0)

invertir()
vox = Vox.from_dense(M)
vox.palette = pal


VoxWriter('ejemploc.vox', vox).write()

		