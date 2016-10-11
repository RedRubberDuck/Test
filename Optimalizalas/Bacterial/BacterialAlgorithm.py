import math
import random
import numpy as num
import heapq
import time

class Bacterial:
 	def __init__(self,x,step):
 		self.x=x
 		self.step=step
 		self.val=None
 	def getVal(self):
 		return self.val
 	def setVal(self,value):
 		self.val=value
 	def getX(self):
 		return self.x
 	def getStep(self):
 		return self.step
 	def setX(self,x):
 		self.x=x
 	def setStep(self,step):
 		self.step=step
 	def Chemotaxis(self,nrStep,direction):
 		xMat=num.matrix(self.x)
 		dirMat=num.matrix(direction)
 		new_xMat=xMat+nrStep*self.step*dirMat
 		new_x=new_xMat.getA()[0]
 		return new_x
 	#Tumble
 	def Rotation(self):
 		dimension=len(self.x)
 		direction=[]
 		summ=0
 		for i in range(dimension):
 			temp=random.random()
 			direction.append(temp)
 			summ+=temp*temp
 		summ=math.sqrt(summ)
 		for i in range(dimension):
 			direction[i]/=summ
 		return direction
class Population:
	def __init__(self,nrBac,intervals,initstep):
		self.nrBac=nrBac
		self.intervals=intervals
		self.initstep=initstep
		self.population=self.randomInitialize()


	def randomInitialize(self):
		nrDimension=len(self.intervals[0])
		population=[]
		for i in range(self.nrBac):
			bac=[]
			for j in range(nrDimension):
				temp=random.random()*(self.intervals[1][j]-self.intervals[0][j])+self.intervals[0][j]
				bac.append(temp)
			Bac=Bacterial(bac,self.initstep)
			population.append(Bac)
		return population
	def getIntervals(self):
		return self.intervals
	def getBacteria(self,index):
		return self.population[index]
	def setBacteria(self,index,bac):
		self.population[index]=bac
	def getNrBac(self):
		return self.nrBac
	def printPopulation(self):
		for bac in self.population:
			print bac.getVal(),bac.getX()
	def getPopulationPos(self):
		pos=[]
		for bac in self.population:
			if len(pos) is 0:
				pos=[bac.getX()]
			else:
				pos=num.concatenate((pos,[bac.getX()]),axis=0)
		return pos
	def sortPopulation(self):
		heap=[]
		for i in range(self.nrBac):
			bac=self.population[i]
			heapq.heappush(heap,(bac.getVal(),bac))
		lenHeap=len(heap)
		sortedPopulation=[]
		for i in range(lenHeap):
			(tempV,tempBac)=heapq.heappop(heap)
			sortedPopulation.append(tempBac)
		self.population=sortedPopulation
	def getMeanOfPopulation(self):
		summ=0
		for i in range(self.nrBac):
			summ+=self.population[i].getVal()
		mean=summ/float(self.nrBac)
		return mean









class BacterialOptimizator:
	def __init__(self,function,population,MaxStep,MaxChem,MaxRep,MaxED,EDFactor):
		self.function=function
		self.population=population
		self.MaxStep=MaxStep
		self.MaxChem=MaxChem
		self.MaxRep=MaxRep
		self.MaxED=MaxED
		self.EDFactor=EDFactor
		self.Initialize()
	def Initialize(self):
		for i in range(self.population.getNrBac()):
			bac=self.population.getBacteria(i)
			bacV=self.function(bac.getX())
			bac.setVal(bacV)
	def ChemotaxisPhase(self):
		for j in range(self.MaxChem):
			for i in range(self.population.getNrBac()):
				bac=self.population.getBacteria(i)
				bacV=bac.getVal()
				direction=bac.Rotation()
				newBacPos=bac.Chemotaxis(1,direction)#It's a vector
				newBacV=self.function(newBacPos)
				stepIndex=1
				while stepIndex<self.MaxStep:
					if bacV>newBacV:
						bacV=newBacV
						bac.setX(newBacPos)
						bac.setVal(newBacV)
						newBacPos=bac.Chemotaxis(1,direction)
						newBacV=self.function(newBacPos)
						stepIndex+=1
					else:
						break
	def ReproductionPhase(self):
		for j in range(self.MaxRep):
			self.ChemotaxisPhase()
			self.population.sortPopulation();
			startIndex=self.population.getNrBac()/2
			if self.population.getNrBac()%2 is 1:
				startIndex+=1
			for i in range(self.population.getNrBac()/2):
				bac=self.population.getBacteria(i)
				self.population.setBacteria(i+startIndex,bac)
	def EliminateAndDispersalPhase(self):
		for k  in range(self.MaxED):
			self.ReproductionPhase()
			for i in range(self.population.getNrBac()):
				if random.random()<self.EDFactor:
					dimension=len(self.population.getBacteria(i).getX())
					new_x=[]
					for j in range(dimension):
						temp=random.random()*(self.population.getIntervals()[1][j]-self.population.getIntervals()[0][j])+self.population.getIntervals()[0][j]
						new_x.append(temp)
					new_val=self.function(new_x)
					oldBac=self.population.getBacteria(i)
					newBac=Bacterial(new_x,oldBac.getStep())
					newBac.setVal(new_val)
					self.population.setBacteria(i,newBac)
	def Optimizate(self):
		self.EliminateAndDispersalPhase()





class BacterialOptimizatorModified(BacterialOptimizator):
	def __init__(self,function,population,MaxStep,MaxChem,MaxRep,MaxED,EDFactor):
		self.function=function
		self.population=population
		self.MaxStep=MaxStep
		self.MaxChem=MaxChem
		self.MaxRep=MaxRep
		self.MaxED=MaxED
		self.EDFactor=EDFactor
		self.Evoluation=[]
		self.Initialize()
	def ChemotaxisPhase(self):
		for j in range(self.MaxChem):
			for i in range(self.population.getNrBac()):
				bac=self.population.getBacteria(i)
				bacV=bac.getVal()
				direction=bac.Rotation()
				newBacPos=bac.Chemotaxis(1,direction)#It's a vector
				newBacV=self.function(newBacPos)
				stepIndex=1
				while stepIndex<self.MaxStep:
					if bacV>newBacV:
						bacV=newBacV
						bac.setX(newBacPos)
						bac.setVal(newBacV)
						newBacPos=bac.Chemotaxis(1,direction)
						newBacV=self.function(newBacPos)
						stepIndex+=1
					else:
						break
			mean=self.population.getMeanOfPopulation()
			self.Evoluation.append(math.log10(mean))
	def Optimizate(self):
		startTime=time.clock()
		self.EliminateAndDispersalPhase()
		endTime=time.clock()
		print "Run Time:",endTime-startTime
		print "Number of chemotaxis:",len(self.Evoluation)
	def getEvoluation(self):
		return self.Evoluation











