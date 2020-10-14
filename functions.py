import numpy as np
import sys

def expo(x):  #x is a argument to the function
	return np.exp(x)

#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):
		print(expo(float(i))) 



def main(): 
    n = 10 


if(len(sys.argv)>1):
	n = int(sys.argv[1])


	print("n is equal to,",n)

	show_expo(n)


if __name__=="__main__":
	main()