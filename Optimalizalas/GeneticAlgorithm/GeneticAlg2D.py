#Basic genetic algorithm
#It's problem to representate the real number, as bit strings
import numpy as num
import numpy.random as random
import heapq
import math
import Crossover
import Mutation

def BSGenetic2D(function,search_interval,dimension,nr_chromosome):
    
    nr_bits=32
    
    nr_sel=int(math.ceil(math.sqrt(nr_chromosome))+1)
    print nr_sel
    population=RandomPopulation(search_interval,nr_chromosome,dimension)
    all_population=[]
    meanOfFitness=[]
    
    run=True
    k=1
    while run:
        all_population.append(population)
        val_population=CalculateValues(function,population)
        
        #print val_population
        populationArray=OrdonatePopulation(population,val_population)
        
        #print populationArray
        selectedpopulationArray=Selection(populationArray,nr_sel)
        meanOfFitness.append( CalcMean(selectedpopulationArray[0]))
        #print selectedpopulationArray[0]
        run=StopCriterion(selectedpopulationArray)
        if run is False:
            break
        sel_population=selectedpopulationArray[1]
        (intervals,conv_pop)=Convert2BinaryString(sel_population,nr_bits)
        new_convPop=Crossover.CrossOver(conv_pop,nr_chromosome,nr_bits)
        newPopulation=Convert2RealValues(new_convPop,intervals,nr_bits)
        population=newPopulation
       
        population=Mutation.Mutation(newPopulation,search_interval)
        k+=1
        #print sel_population
        if k>1000:
            run=False
            print 'End of search'
            
    return (all_population,meanOfFitness)

def CalcMean(val_population):
    return sum(val_population)/float(len(val_population))

def StopCriterion(populationArray):
    val_population=populationArray[0]
    if math.fabs(val_population[1])<10e-3:
        return False
    return True
    
    
def CrossOver(ss_pop,nr_chromosome):
    new_pop=[]
    for i in range(len(ss_pop)):
        for j in range(i+1,len(ss_pop)):
            chro1=ss_pop[i];chro2=ss_pop[j]
    

def Selection(populationArray,nr_selChrom):
    populationValues=populationArray[0]
    population=populationArray[1]
    nr_population=len(populationValues)
    selectedVal=populationValues[0:nr_selChrom]
    selectedChro=population[0:nr_selChrom]
    return (selectedVal,selectedChro)

def CalculateValues(function,population):
    nr_chromosome=len(population)
    val_population=[]
    for i in range(0,nr_chromosome):
        chromosome=population[i,:]
        val=function(chromosome)
        val_population.append(val)
    return val_population
    
def RandomPopulation(interval,nr_Chromosome,dimension):
    mat=random.random((dimension,nr_Chromosome))
    length=interval[1,:]-interval[0,:]
    for i in range(dimension):
        mat[i]=mat[i,:]*length[i]+interval[0][i]
    mat=num.matrix(mat).getT().getA()
    return mat


def OrdonatePopulation(population,val_population):
    heap=[]
    nr_Chromosome=len(population)
    for i in range(nr_Chromosome):
        heapq.heappush(heap,(val_population[i],i))
    lengthHeap=len(heap)
    temp=heapq.heappop(heap)
    sorted_chromosomes=[population[temp[1],:]]
    sorted_values=[temp[0]]
    for i in range(1,lengthHeap):
        temp=heapq.heappop(heap)
        sorted_chromosomes=num.concatenate((sorted_chromosomes,[population[temp[1],:]]),axis=0)
        sorted_values.append(temp[0])
    return (sorted_values,sorted_chromosomes)
        
def Convert2BinaryString(population,nr_bits):
    nr_chromosome=len(population)
    maxVal=long(math.pow(2,nr_bits)-1)
    minAx=num.min(population,axis=0)
    maxAx=num.max(population,axis=0)
    intervals=[minAx]
    intervals=num.concatenate((intervals,[maxAx]),axis=0)
    ss_pop=[]
    conv_pop=[]
    for i in range(len(population)):
        chro=population[i,:]
        ss_chro=[]
        conv_chro=[]
        for j in range(len(chro)):
            temp=long((chro[j]-intervals[0,j])/(intervals[1,j]-intervals[0,j]+10e-10)*maxVal)
            #ss_chro.append('{0:010b}'.format(temp))
            conv_chro.append(temp)
        #ss_pop.append(ss_chro)    
        conv_pop.append(conv_chro)
    return (intervals,conv_pop)

def Convert2RealValues(population,intervals,nr_bits):
    nr_chromosome=len(population)
    maxVal=float(math.pow(2,nr_bits)-1)
    conv_pop=[]
    for i in range(nr_chromosome):
        chro=population[i]
        conv_chro=[]
        for j in range(len(chro)):
            temp=chro[j]/maxVal*(intervals[1,j]-intervals[0,j])+intervals[0,j]
            conv_chro.append(temp)
        if len(conv_pop) is 0:
            conv_pop=[conv_chro]
        else:
            conv_pop=num.concatenate((conv_pop,[conv_chro]),axis=0)
    return conv_pop
            
            
    
    
    
    
