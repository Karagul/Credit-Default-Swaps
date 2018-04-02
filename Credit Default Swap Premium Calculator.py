''' This program calculates the premium of a Credit Default Swap given 
the intensity Lambda'''

''' the notional of the contract is not necessary as input'''

import numpy as np

N= 100000000 #notional amount

R= input('Please input the recovery rate as decimal number, for example 0.40 \n') 
R=float(R) #recovery rate

r = input('Please enter the interest rate as decimal, for example 0.05 \n') 
r= float(r) #risk-free interest rate

Lambda= input('Please enter Lambda as decimal number, for example 0.01 \n') 
Lambda=float(Lambda) #hazard rate

T= input('Please enter the duration of the CDS in years \n') #
T= int(T)

dt= input('Please enter the premium times, for example for quarterly premiums enter 0.25 \n')
dt= float(dt)

time= np.arange(0, T+dt, 0.25) #creates an array of times

DF = [] # creates an array of discount factors
P = [1] # creates an array of cumulative survival probabilities
PD = [] # creates an array of period probabilities of default
Premium_leg = [] # creates an array for the premiums at each time t
Default_leg = [] # creates an array for the default leg at each time t

for i in range(1,len(time)):
	DF.append(np.e ** (-r * time[i]) )
	P.append(np.e ** (-Lambda * time [i]) )
	PD.append(P[i-1] - P[i])    
	Premium_leg.append(dt * P[i] * DF[i-1]) 
	Default_leg.append((1 - R) * PD[i-1] * DF[i-1])
		
	Sum_Premium_leg=sum(Premium_leg)
	Sum_Default_leg=sum(Default_leg)
	
premium = Sum_Default_leg / Sum_Premium_leg
	
print('The premium is ', premium)
	

	
	
	
	
	




