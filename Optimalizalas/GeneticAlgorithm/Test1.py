import numpy as num
import GeneticAlg1 as gn
import Crossover
import Mutation
def func1(Vec):
    VecM=num.matrix(Vec)
    return (VecM*VecM.getT()).getA()[0,0]

nr_dim=2
interval=num.ones([2,nr_dim])*10
interval[0]=interval[0,:]*-1
Pop=gn.BSGenetic(func1,interval,nr_dim)

print Pop

#s=Mutation.OpMutation(1000)
#print s
#Crossover.OpCrossover(712,324,1)


