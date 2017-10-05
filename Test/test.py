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
	
	assert (index[5] == 5.0) and (force[0] == 3), "stupid life"

	

	 


