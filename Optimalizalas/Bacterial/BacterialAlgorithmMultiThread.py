import math
import random
import numpy as num
import heapq
import time
import threading

import BacterialAlgorithm

class MyThread(threading.Thread):
	def __init__(self,countDownLatch,function,MaxStep,MaxChem,startIndex,endIndex,population,Name):
		threading.Thread.__init__(self)
		self.countDownLatch=countDownLatch
		self.startIndex=startIndex
		self.endIndex=endIndex
		self.population=population
		self.MaxStep=MaxStep
		self.MaxChem=MaxChem
		self.Name=Name
		self.function=function
	def run(self):
		#print "Started name:"+self.Name
		for j in range(self.MaxChem):
			for i in range(self.startIndex,self.endIndex):
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
		#print "End name:"+self.Name
		self.countDownLatch.count_down()


class BacterialOptimizatorMultiThread(BacterialAlgorithm.BacterialOptimizatorModified):
	def __init__(self,function,population,MaxStep,MaxChem,MaxRep,MaxED,EDFactor,nrThread):
		self.function=function
		self.population=population
		self.MaxStep=MaxStep
		self.MaxChem=MaxChem
		self.MaxRep=MaxRep
		self.MaxED=MaxED
		self.EDFactor=EDFactor
		self.Evoluation=[]
		self.nrThread=nrThread
		self.Initialize()
	def ChemotaxisPhase(self):
		countDownLatch=CountDownLatch(self.nrThread)
		nrBac=self.population.getNrBac()
		nrBacThread=nrBac/self.nrThread
		for i in range(self.nrThread):
			startIndex=i*nrBacThread
			endIndex=(i+1)*nrBacThread-1
			t1=MyThread(countDownLatch,self.function,self.MaxStep,self.MaxChem,startIndex,endIndex,self.population,str(i))
			t1.start()
		countDownLatch.await()	



class CountDownLatch:
	def __init__(self,count=1):
		self.count=count
		self.lock=threading.Condition()
	def count_down(self):
		self.lock.acquire()
		self.count-=1
		if self.count<=0:
			self.lock.notifyAll()
		self.lock.release()
	def await(self):
		self.lock.acquire()
		while self.count>0:
			self.lock.wait()
		self.lock.release()
			