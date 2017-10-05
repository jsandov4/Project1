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
	return  index, xs, pot, force
		
	

