
import numpy as np #import numpy module

np.random.seed(101) #fixing the seed to get ensure reproducability 

inputs= np.random.rand(3) #input array of 1x3 with values b/w 0-1

weights=np.random.rand(3) #weights array of 1x3 with values b/w 0-1

weighted_input= np.dot(inputs,weights) #dot product of inputs and weights i.e. x1w1+x2w2+x3w3

def activation_func(weighted_input):  #activation function defenition

	if(weighted_input <= 0):   #step function condition
		return 0
	else:
		return 1

output=activation_func(weighted_input)  #final output

print("Inputs->",inputs)
print("weights->",weights)
print("weighted_input dot product->",weighted_input) 
print("output->",output)

#electroica_blog