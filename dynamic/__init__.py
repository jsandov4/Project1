""" Project Langevine Dynamics """

def read_file(xfile):

	index = []
	xs = []
	pot = []
	force = []

	data = xfile.readlines()
	size = len(data)
	lista = []
	for i in range(size):
                lista = data[i].split()
                index.append(float(lista[0]))
                xs.append(float(lista[1]))
                pot.append(float(lista[2]))
                force.append(float(lista[3]))
                #print(lista[0],lista[3])

	return  index, xs, pot, force
		
	
def interpol(xarray, farray, xpos):
	
	size = len(xarray)
	xmin = xarray[0]
	xmax = xarray[size-1]

	imin = 0
	imax = 0

	for i in range(1,size):
		val = xarray[i]		
		if xpos < val:
			imin = i-1
			imax = i

	slope = (farray[imax]-farray[imin])/(xarray[imax]-xarray[imin])
	b = farray[imin] - slope*xarray[imin]
	force = slope*xpos + b
	
	return force
			
def normalverlet(xarray,farray,mass,deltat,q0,p0,lamda,temp,types):
        import random
        force0 = interpol(xarray,farray,q0)
        qt = q0 + (p0/mass)*deltat + (force0/mass)*(deltat**2)/2
        force1 = interpol(xarray,farray,qt)
        sigma = (2.0*lamda*temp)**(0.5)
        # Introducting noise
        # generate random number from normal distribution
        # using lamda obtain v*lamda

        if types == 0:
                ran = 0
                damp = 0
        else:
                ran  = random.gauss(0,sigma)
                damp =-lamda*(p0/mass)

        pt = p0 + (force0+force1)*deltat/2 + damp + ran
        return qt,pt

	
def fullDynamics(xarray,farray,mass,deltat,q00,p00,ttime,lamda,temp,types):
        q0 = q00
        p0 = p00
        steps = int(ttime/deltat)
        vt = []
        xt = []
        ind = []
        tt = []
        
        
        for i in range(steps):
                q1,p1 = normalverlet(xarray,farray,mass,deltat,q0,p0,lamda,temp,types)
                
                vt.append(p1/mass)
                xt.append(q1)
                ind.append(i)

                q0 = q1
                p0 = p1
        return q1,p1,vt,xt,ind


def inputconsole():
        import argparse
        parse = argparse.ArgumentParser(description='Calculate dynamics')
        parse.add_argument('-c','--types',type=float,metavar ='',required=True,help='(0) for Classical dynamics'+\
                           'otherwise for langevine dynamics')
        parse.add_argument('-q','--q0',type=float,metavar ='',required=True,help='Initial position')
        parse.add_argument('-v','--v0',type=float,metavar ='',required=True,help='Initial momentum')
        parse.add_argument('-m','--mass',type=float,metavar ='',required=True,help='Mass of the particle')
        parse.add_argument('-ti','--ttime',type=float,metavar ='',required=True,help='Total time')
        parse.add_argument('-d','--dt',type=float,metavar ='',required=True,help='Time step size')
        parse.add_argument('-te','--temp',type=float,metavar ='',required=True,help='Temperature of the system')
        parse.add_argument('-l','--lamda',type=float,metavar ='',required=True,help='Damping constant')
        parse.add_argument('-i','--input',type=str,metavar ='',required=True,help='filename')
        
        return parse

if __name__=='__main__':

        import os
        import matplotlib as mpl
        from mpl_toolkits.mplot3d import Axes3D
        import numpy as np
        import matplotlib.pyplot as plt

        
        args = inputconsole().parse_args()
        p0 = args.v0*args.mass
        typess = args.types

        xfile = open(args.input,"r")
        index, xpos, pot, fforce = read_file(xfile)

        
        qf,pf,vt,xt,ind = fullDynamics(xpos,fforce,args.mass,args.dt,args.q0,p0,args.ttime,args.lamda,args.temp,typess)
        steps = int(args.ttime/args.dt)
        xwrite = open("output.txt","w")
        for i in range(steps):
                xwrite.write(str(ind[i])+"\t"+str(args.dt*ind[i])+"\t"+str(xt[i])+"\t"+str(vt[i])+"\n")

        mpl.rcParams['legend.fontsize'] = 10
        fig = plt.figure()
        ax = fig.gca(projection='3d')

 #       tt = ind*dt


 #       theta = np.linspace(-4 * np.pi, 4 * np.pi, 100)
#        z = np.linspace(-2, 2, 100)
#        r = z**2 + 1
#        x = r * np.sin(theta)
#        y = r * np.cos(theta)

#        plt.plot(ind, xt, 'r--', ind, vt,'g--')
#        plt.show()
        
 #       plt.plot(ind,xt)
        ax.set_xlabel('Position')
        ax.set_ylabel('Velocity')
        ax.set_zlabel('Time')
        
        ax.plot( xt, vt, ind,'r--', label='Phase space trajectory')
        ax.legend()
        plt.show()
        
#        print(qf,pf,steps)





