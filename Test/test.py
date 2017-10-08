import io
def test_import():
	import dynamic
def test_read_file():
	import dynamic
	text  = u"""0 1 2 3 
	1 2 3 4 
	2 3 4 5 
	3 4 5 6 
	4 5 6 7  
	5 6 7 8"""

	test = io.StringIO(text)
	index, x, energy, force = dynamic.read_file(test)
	
	assert (index[5] == 5.0) and (force[0] == 3), "Bad reading"

	
def test_interpol():
	import dynamic
	import numpy
	xvals = [0,0,0]
	forcev = [0,0,0]

	xvals[0] = 0
	xvals[1] = 20
	xvals[2] = 40
	forcev[0] = 0
	forcev[1] = 200
	forcev[2] = 400

	xtest = 30
	xinter = dynamic.interpol(xvals,forcev,xtest)
	
	assert numpy.isclose(xinter,300.0), "very bad interpol"
	
	 
def test_normalverlet():
	import dynamic
	import numpy

	# H = p^2/2m + (-c*q) 
	# test for a linear potential
	# with analitical solution

	# Force and position arrays
	
	xpos = range(-5,6) 
	fforce  = [1]*11	

	# Initial conditions (q0,p0)
	q0 = 0.0
	p0 = 0.0
	
	# Parameters
	deltat = 1.0
	mass = 1.0
	
	# Next position
	q1 = 0.5
	p1 = 1.0
                 #               (xarray,farray,mass,deltat,q0,p0,lamda,temp,types):
	qf,pf = dynamic.normalverlet(xpos,fforce,mass,deltat,q0,p0,0,0,0)
	#print(qf,pf)
	assert numpy.isclose(q1,qf) and numpy.isclose(p1,pf) , "Bad verlet"

def test_fullDynamic():

	import dynamic
	import numpy


	ttime = 10
	tstep = 0.1
	mass = 1.0
	q0 = 0.0
	p0 = -10.0
        # H = p^2/2m + (-c*q)
        # test for a linear potential
        # with analitical solution
	xpos = range(-60,10)
	fforce =[1]*70

	# Final values (analitical)
	q1 = -50.0
	p1 = 0.0

	qf,pf,vt,xt,inde = dynamic.fullDynamics(xpos,fforce,mass,tstep,q0,p0,ttime,0,0,0)

	print(qf,pf)
	assert numpy.isclose(q1,qf) and numpy.isclose(p1,pf) , "Bad FullDynamics"



        #def test_inputconsole
        #    import os
        #    os.system("")







