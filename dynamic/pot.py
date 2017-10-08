


if __name__=='__main__':

    xf = 20
    x0 = -20
    nx = 1000

    dx = (xf-x0)/(nx-1)
    
    func = "x**2 + 2*x"
    
    xfile = open('input2.txt','w')
    for i in range(nx):
        
        x = x0 +(i)*dx
        xt=x
        yt = eval(func)
        ft = -2.0*yt
        xfile.write(str(i)+"\t"+str(xt)+"\t"+str(yt)+"\t"+str(ft)+"\n")


