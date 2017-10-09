![Coverage image](./img/coverage.svg)
Program

# Classical and Langevine Dynamics package (dynamic)

[![N|Solid](https://cldup.com/dTxpPi9lDf.thumb.png)](https://nodesource.com/products/nsolid)

This package allows to perform either, Classical or Langevine dynamics according to your preference, and also provide a graphical description of the dynamics in the phase space (q,p) as a function of time (z-axis).

### Input data from console

The input that should be put in the console has the following attributes:

  -c , --type 0 (zero) for Classical dynamics otherwise for langevine dynamics
  -q , --q0       Initial position
  -v , --v0       Initial momentum
  -m , --mass     Mass of the particle
  -ti , --ttime   Total time
  -d , --dt       Time step size
  -te , --temp    Temperature of the system
  -l , --lamda    Damping constant
  -i , --input    filename

### Auxiliary data


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
# Input format 
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
Given a file with the same structure than the expected input, the test check the values are correct.

#### Interpolating the force
Due to the fact that the force and potential information is given through a file, with discrete values, it is required to calculate the force of values between the given points.

To test if the interplation is working, a simple scenario is built to compare with a known value.

#### Testing the dynamics 
To test the appropiate behaviour of the numerical integrator, an analytical solvable system is used.
The simple system employed has the following Hamiltonian
            *H(p,q) =  p^2/(2/M) + V(q)*
where *V(q) = Cq* is a linear potential. C and M are fixed to be *1*.

By comparing the analitical solution of this system with the numerical method employed we can check its accuratness.

##### One step
The numerical method to integrate the equation of motion is the *verlet algorithm*, which is weel known due to the simplicity of been implemented and the fact that it is a symplectic integrator.

Given an initial condition, the system is evolved one time step and compared with the analytical result.

##### Complete dynamic

Following the same logic than before, the system is evolved 10 steps and compared with numerical result.



### Development

Want to contribute? Great!







