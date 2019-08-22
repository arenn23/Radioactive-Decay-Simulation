# -*- coding: utf-8 -*-
"""
Alan Renner
CBE 5790
Homework 1: Radioactive Decay
"""

import numpy as np
import matplotlib.pyplot as plt


#Setting initial values. Set Rn variables
RnHalfLife = 3.8235 * 24   #Halflife of radon isotope (hr)
RnMeanLifeTime = RnHalfLife / np.log(2)
MaxTime = 5 * RnMeanLifeTime   #Simulation time limit (hr)
TimeStep = 0.005   #Time step size (hr)
Time = np.arange(0., MaxTime, TimeStep)
ProbNotDecayRn = np.exp(-TimeStep / RnMeanLifeTime)   #Probability of not Rn decaying
#End Rn section values

#Setting the number of atoms besides Rn present at time zero
NumPoAtomsZero = 0   #No Po 218 atoms are present at time zero
NumPb214AtomsZero = 0   #No Pb 214 atoms are present at time zero
NumBiAtomsZero = 0   #No Bi atoms are present at time zero
NumPo214AtomsZero = 0   #No Po 214 atoms are present at time zero
NumPb210AtomsZero = 0   #No Pb 210 atoms present at time zero

#Defining halflifes for each isotope (except Rn). All units are hours
PoHalfLife = 3.10 / 60   #Halflife of Po 218 in hours
Pb214HalfLife = 26.8 / 60   #Halflife of Pb 214 in hours
BiHalfLife = 19.9 / 60   #Halflife of Bi in hours
Po214HalfLife = 0.0000027383   #Halflife of Po 214 in hours
Pb210HalfLife = 22.2 * 365 * 24  #Halflife of Pb 210 in hours
HalfLifes = [RnHalfLife, PoHalfLife, Pb214HalfLife, BiHalfLife, Po214HalfLife, Pb210HalfLife]   #Half lifes for all elements

#Defining mean life time for all elements besides Rn
PoMeanLifeTime = PoHalfLife / np.log(2)   #Mean life time for Po 218
Pb214MeanLife = Pb214HalfLife / np.log(2)   #Mean life time for Pb 214
BiMeanLife = BiHalfLife / np.log(2)  #Mean life time for Bi
Po214MeanLife = Po214HalfLife / np.log(2)   #Mean life time for Po 214
Pb210MeanLife = Pb210HalfLife / np.log(2)   #Mean life time for Pb 210
MeanLifeTimes = [RnMeanLifeTime, PoMeanLifeTime, Pb214MeanLife, BiMeanLife, Po214MeanLife, Pb210MeanLife]   #Mean life times for all elements

#Probability of not decaying for all atoms besides Rn
ProbNotDecayPo = np.exp(-TimeStep / PoMeanLifeTime)   #Probability of Po 218 not decaying
ProbNotDecayPb214 = np.exp(-TimeStep / Pb214MeanLife)   #Probability of Pb 214 not decaying
ProbNotDecayBi = np.exp(-TimeStep / BiMeanLife)   #Probability of Bi not decaying
ProbNotDecayPo214 = np.exp(-TimeStep / Po214MeanLife)   #Probability of Po 214 not decaying
ProbNotDecayPb210 = np.exp(-TimeStep / Pb210MeanLife)   #Probability of Pb 210 not decaying
ProbNotDecay = [ProbNotDecayRn, ProbNotDecayPo, ProbNotDecayPb214, ProbNotDecayBi, ProbNotDecayPo214, ProbNotDecayPb210]   #Probability of not decay for all elements


NumOfAtoms = np.zeros((Time.size, 6), dtype=np.int)  #Creates a array to track all elements at once. 
NumOfAtoms[0,0] = 20   #Sets the original value of Rn as 20

for i in range(1, Time.size):   #A for loop to run sufficiently long to ensure all atoms decay to Pb 210
    NumOfAtomsNotDecay = np.random.binomial(NumOfAtoms[i-1], ProbNotDecay)   #Gives how many atoms will not decay based on previous number of atoms of the element and decay probability
    NumOfAtomsDecay = NumOfAtoms[i-1] - NumOfAtomsNotDecay  #Number of atoms that actually decayed. 
    NumOfAtoms[i,0] = NumOfAtomsNotDecay[0]   #Gives the number of Rn atoms. It is just equal to the number of not decayed Rn atoms.
    NumOfAtoms[i, 1:] = NumOfAtomsNotDecay[1:] + NumOfAtomsDecay[0:-1]   #Computes the number of all other atoms besides Rn. It sums the number of not decayed atoms of the elment (next line)
    #with the number of decayed atoms prior in the chain. 
    
#Plotting atoms of elements
plt.plot(Time,NumOfAtoms[:,0], 'b-', label = 'Rn 222')
plt.plot(Time,NumOfAtoms[:,1], 'g-', label = 'Po 218')
plt.plot(Time,NumOfAtoms[:,2], 'r-', label = 'Pb 214')  
plt.plot(Time,NumOfAtoms[:,3], 'y-', label = 'Bi 214')
plt.plot(Time,NumOfAtoms[:,4], 'g:', label = 'Po 214')
plt.plot(Time,NumOfAtoms[:,5], 'b:', label = 'Pb 210')
#Title, axis labels and legend
plt.title('Radioactive Decay')
plt.xlabel('Time (hr)')
plt.ylabel('Number of atoms')
plt.legend(loc = 'best')