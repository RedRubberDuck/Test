import numpy as num
import GeneticAlg2D as gn
import Crossover
import Mutation
import matplotlib.pyplot as plt
import math



def drawCountour(function,intervals):
    x=num.linspace(intervals[0,0],intervals[1,0])
    y=num.linspace(intervals[0,1],intervals[1,1])
    X, Y=num.meshgrid(x,y)
    Z=num.zeros((50,50))
    plt.hold(True)
    for i in range(50):
        for j in range(50):
            Z[i,j]=function([X[i,j],Y[i,j]])
    plt.contour(X,Y,Z)

def drawPoints(all_population):
    nr_population=len(all_population)
    for i in range(nr_population):
        temp=0
        if i<nr_population/2:
            color1=num.matrix([0.0,0.0,1.0])#blue
            color2=num.matrix([0.0,1.0,0.0])#green
        else:
            color1=num.matrix([0.0,1.0,0.0])#green
            color2=num.matrix([1.0,0.0,0.0])#blue
            temp=nr_population/2.0
        pop=all_population[i]
        a=(i-temp+1)/(nr_population/2.0)
        col=(a*color2+(1-a)*color1).getA()[0]
        for j in range(len(pop)):
            chro=pop[j]
            point=plt.plot(chro[0],chro[1],'o')
            plt.setp(point,color=col)
    

def drawEvolution(meanOfFitness):
    nr_generation=len(meanOfFitness)
    indexes_generations= range(nr_generation)
    plt.plot(indexes_generations,meanOfFitness,'go-')

def Sphere(Vec):
    VecM=num.matrix(Vec)
    return (VecM*VecM.getT()).getA()[0,0]

def Rosenbrock(Vec):
    result=0
    for i in range(len(Vec)):
        if i is len(Vec)-1:
            break
        
        nextV=Vec[i+1]
        result+=100*(nextV-Vec[i]*Vec[i])*(nextV-Vec[i]*Vec[i])+(1-Vec[i])*(1-Vec[i])
    return result    

def Rastrigin(Vec):
    result=10*len(Vec)
    for i in Vec:
        result+=i*i-10*math.cos(2*math.pi*i)
    return result
    
def Griewanf(Vec):
    result=0
    for i in Vec:
        result+=1.0/4000.0*i*i
    for i in range(len(Vec)):
        result-=math.cos(Vec[i]/(i+1))
    result+=1
    return result


function=Griewanf
nr_dim=2
interval=num.ones([2,nr_dim])*20
interval[0]=interval[0,:]*-1
(all_pop,meanOfFitness)=gn.BSGenetic2D(function,interval,nr_dim,50)

plt.figure(1)
drawCountour(function,interval)
drawPoints(all_pop)
plt.show()

plt.figure(2)
drawEvolution(meanOfFitness)
plt.show()

#s=Mutation.OpMutation(1000)
#print s
#Crossover.OpCrossover(712,324,1)


