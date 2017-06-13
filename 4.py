#!/usr/bin/env python
# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt 
import numpy as np
import math

class Pendulo:
	def __init__(self, massa, comprimento, theta, vangular):
		self.m=massa
		self.l=comprimento
		self.x=theta
		self.v=vangular
		self.wo=math.sqrt(g/comprimento)
		self.T=2*math.pi*math.sqrt(comprimento/g)
		self.E= 0.5*self.m*(self.l*self.v)**2 + self.m*g*self.l*(1-math.cos(self.x))
	
	def a(self,x,v,t):
		return(-self.wo**2*math.sin(x)-gama*v+A*math.sin(wf*t))
		
	def movimento(self, t):
		at=self.a(self.x, self.v, t)
		self.x=self.x + self.v*dt+0.5*at*dt**2
		atem=self.a(self.x,self.v,t)
		vtemp=self.v+0.5*(at+atem)*dt
		atemp=self.a(self.x,vtemp, t)
		self.v=self.v+0.5*(at+atemp)*dt
		self.at=self.a(self.x, self.v, t)
		self.E=0.5*self.m*(self.l*self.v)**2 + self.m*g*self.l*(1-math.cos(self.x))

g=9.8
gama=0.5
A=1.25
wf=2.0/3.0
t=0.0
dt=0.0001

p1=Pendulo(1., 10., math.pi/6., 0)

tmax=20*p1.T

t=np.arange(0, tmax, dt)

x=np.zeros(t.size)
v=np.zeros(t.size)
E=np.zeros(t.size)

x[0]=(p1.x+np.pi)%(2*np.pi)-np.pi
v[0]=p1.v
E[0]=p1.E

for i in range(t.size):
	p1.movimento(t[i])
	x[i]=(p1.x+np.pi)%(2*np.pi)-np.pi
	v[i]=p1.v
	E[i]=p1.E

plt.figure(figsize=(6,5), dpi=96)
ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()


plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
#plt.xlabel('Tempo(s)')
#plt.ylabel('Energia(J)')
#plt.ylabel(r'Posi\c{c}\~{a}o (m) e Velocidade (m/s)')


plt.title(r'P\^endulo For\c{c}ado', fontsize=12)
plt.grid()
plt.plot(x,v,'k-', linewidth=2 )
#plt.plot(t,x,'b-', linewidth=2,label="$x_{(t)}$" )
#plt.plot(t,v,'r-', linewidth=2, label="$v_{(t)}$")
#plt.plot(t,E,'g-',linewidth=2, label="$e_{(t)}$")

plt.legend(loc='upper right')
plt.savefig("forcado.pdf", dpi=96)

plt.show()			
				
		
