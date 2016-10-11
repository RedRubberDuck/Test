import numpy as num
import matplotlib.pyplot as plt

import BacterialAlgorithm
import BacterialAlgorithmMultiThread

def plotEvoluation(evoluation):
	length=len(evoluation)
	indexesOfChemotaxis=range(length)
	plt.plot(indexesOfChemotaxis,evoluation,'g')

def Sphere(Vec):
	vecMat=num.matrix(Vec)
	valMat=vecMat*vecMat.getT()
	return valMat.getA()[0][0]


pop=BacterialAlgorithm.Population(200,[[-10,-10],[10,10]],0.1)
optimizator=BacterialAlgorithmMultiThread.BacterialOptimizatorMultiThread(Sphere,pop,10,200,5,5,0.1,2)
pop.sortPopulation()
print "Init:"
pop.printPopulation()



print "Result:"
optimizator.Optimizate()

print "Result2:"
optimizator1=BacterialAlgorithm.BacterialOptimizatorModified(Sphere,pop,10,200,5,5,0.1)
optimizator1.Optimizate()
evoluation=optimizator1.getEvoluation()
plotEvoluation(evoluation)
plt.show()

