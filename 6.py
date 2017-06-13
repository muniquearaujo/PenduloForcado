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
A=2.5
wf=2.0/3.0
t=0.0
dt=0.0001

p1=Pendulo(1., 10., math.pi/6., 0)
p2=Pendulo(1.,10.,math.pi/6-1e4,0)

tmax=20*p1.T


t=np.arange(0, tmax, dt)


x1=np.zeros(t.size)
v1=np.zeros(t.size)
E1=np.zeros(t.size)

x2=np.zeros(t.size)
v2=np.zeros(t.size)
E2=np.zeros(t.size)

difx=np.zeros(t.size)
difv=np.zeros(t.size)
dife=np.zeros(t.size)


x1[0]=(p1.x+np.pi)%(2*np.pi)-np.pi
v1[0]=p1.v
E1[0]=p1.E

x2[0]=(p2.x+np.pi)%(2*np.pi)-np.pi
v2[0]=p2.v
E2[0]=p2.E



for i in range(t.size):
	p1.movimento(t[i])
	p2.movimento(t[i])
	x1[i]=(p1.x+np.pi)%(2*np.pi)-np.pi
	v1[i]=p1.v
	E1[i]=p1.E
	
	
	x2[i]=(p2.x+np.pi)%(2*np.pi)-np.pi
	v2[i]=p2.v
	E2[i]=p2.E

	difx[i]=math.fabs(x1[i]-x2[i])
	difv[i]=math.fabs(v1[i]-v2[i])
	dife[i]=math.fabs(E1[i]-E2[i])
plt.figure(figsize=(6,5), dpi=96)
ax=plt.gca()
ax.xaxis.set_ticks_position('bottom')
ax.yaxis.set_ticks_position('left')
ax.autoscale()


plt.rc('text', usetex=True)
plt.rc('font', **{'sans-serif' : 'Arial', 'family' : 'sans-serif'})
plt.xlabel('Tempo(s)')
#plt.ylabel('Energia(J)')
plt.ylabel(r'Diferen\c{c}a da Posi\c{c}\~{a}o (m) ')
#relax=4000
#xr,vr,t1r = x1[relax:],v1[relax:],t[relax:]
#difvr,difxr = difv[relax:],difx[relax:]


plt.title(r'P\^endulo Fo\c{c}ados', fontsize=12)
plt.grid()
plt.plot(t,difx,'c-', linewidth=2 )
#plt.plot(t,x,'b-', linewidth=2,label="$x_{(t)}$" )
#plt.plot(t,v,'r-', linewidth=2, label="$v_{(t)}$")
#plt.plot(t,E,'g-',linewidth=2, label="$e_{(t)}$")

plt.legend(loc='upper right')
plt.savefig("forcado2.pdf", dpi=96)

plt.show()			
				
		
