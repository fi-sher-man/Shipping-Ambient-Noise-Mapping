import csv
import numpy as np 
import pandas as pd 


def wittekind(f, v, vcis, disp, cb, m, n, mount):
	"""
	f = frequency
	v = speed through water in knots 
	vCIS = cavitation inception speed in knots 
	disp = displacement in t Dref = reference displacement in t = 10,000 
	cB = block coefficient 
	m = engine mass in t 
	n = number of engines operating at the same time  
	mount = 0 engine resiliently mounted, = 15 engine rigidly mounted 
	
	"""
	c = (125, .35, (-8 * (10 ** -3)), (6 * (10 ** -5)), (-2 * (10 ** -7)), (2.2 * (10 ** -10)), (10**-7))
	#c   0	  1     2				   3				  4					5					 6
	SL1 = c[0] + (c[1] * f) + (c[2] * (f ** 2)) + (c[3] * (f ** 3)) + (c[4] * (f ** 4)) + (c[5] * (f ** 5)) + (80 * np.log10(4*cb*(v/vcis))) + ((20/3) * np.log10((m/10000)))
	SL2 = (5*np.log(f)) - (1000/f) + 10 + ((20/3) * np.log10((m/10000))) + (60*np.log10((v/vcis)*1000*cb))
	SL3 = (c[6]* (f**2)) - (0.01*f) + 140 + (15*np.log10(m)) + (10*np.log10(n)) + mount

	SL = 10*np.log10((10**(SL1/10)) + (10**(SL2/10)) + (10**(SL3/10)))

	return SL

print(wittekind(300,2.2,9,39916,0.88,11.3,1,0))
