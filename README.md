![Coverage image](./img/coverage.svg)
Program

# Classical and Langevine Dynamics package (dynamic)

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

This package allows to perform either, Classical *(CD)* or Langevine *(LD)* dynamics according to your preference, and also provide a graphical description of the dynamics in the phase space *(q,p)* as a function of time *(z-axis)*. Also an output file is generated.




## Getting started


### Prerequisites
 For using this package you would need to install python 3. You can download it from https://www.python.org/downloads/

### Installing

For installing the dynamic package you have to do the following
  - Go to the folder *Project1*
  - Once inside, type the following command through the terminal
```sh
$ pip3.6 install --user .
```

### Input data from console

The input that should be put in the console has the following parameters:

###### (-ty) : Type of dynamics 
You can chose between doing Classical (CD) or Langevine dynamics (LD). Type on the terminal 0 (zero) for CD otherwise you will performe LD.
###### (-q) : Initial position
###### (-v) : Initial velocity
###### (-m) : Mass of the particle
###### (-ti) : Total time of the simulation 
###### (-d) : Time step or dt
###### (-tem) : Temperature
###### (-l) : Lamda  [Damping parameter]
###### (-i) : Reltive path of the Input file 
  .
##### Example of a console input
Once installed, you can use following command to perform a LD simulation 
```sh
dynamic -ty 1 -q 9 -v 1 -m 1 -ti 10 -d 0.01 -te 10 -l 1 -i input.txt 
```
In this particular case the initial position and velocity are 9 and 1, respectively. The mass is 1, the simulation time is fixed to 10, the time step is 0.01, temperature 10, and the damping parameter is set to 1.
To perform CD simulation  with the same parameters just change *"-ty 1"* for *"-ty 0".* In this case the damping parameter and temperature will not play a role on the dynamics.


### Auxiliary data
If you want to test the accurateness of the method, an input file is provided 
 - *"input2.txt"*.
 
This file contains the data to perform a simulation using a quadratic potential described by

 - V(q) = q^2 + 2q
 
 where the force is given by
 - f(q) = -d/dq[V(q)] = - 2q - 2


# Input file format 
The input file with the information of the potential and the force must be a text-file where each line contains an index, position (q), potential energy V(q) , and force (f), separated by spaces.
```sh
 index _ q _ V(q) _ f(q)
```
# Output file format 
The outpu file with the information of the dynamics, position (q) and velocity (v), will have the following structure 
```sh
 index _ time _ q _ v
```

# Running the tests
In order to perform the test cases done for building this package you have to:
 - Go to the *Project1* folder
 - Install *pytest* using the following command
  ```sh
$ pip3.6 install pytest
```
- Then to check the test, please type
 ```sh
$ python3 -m pytest Test/test.py
```

## Test cases
#### Reading the file
The aim of this test is to verify if the input file is read it in the appropriate way. 
Given a file with the same structure than the expected input, the test check ifthe values are correct.

#### Interpolating the force
Due to the fact that the force and potential information is given through a file, with discrete values, it is required to calculate the force of values between the given points.

To test if the interpolation is working, a simple scenario is built to compare with a known value.

#### Testing the dynamics 
To test the appropiate behaviour of the numerical integrator, an analytic solvable system is used.
The simple system employed has the following Hamiltonian

            H(p,q) =  p^2/(2/M) + V(q)
            
where *V(q) = Cq* is a linear potential. C and M are fixed to be *1*.

By comparing the analytic solution (Solving Hamilton's equation of motion) of this system with the numerical method employed, we can check its accurateness.

##### One step
The numerical method used to integrate the equation of motion is the *verlet algorithm*, which is well known due to the simplicity of its implementation and the fact that it is a Symplectic integrator.

Given an initial condition, the system is evolved one time step and compared with the analytic result.

##### Complete dynamic

Following the same logic than before, the system is evolved 10 steps and compared with numerical result.



### Development

Want to contribute? Great!



**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>


