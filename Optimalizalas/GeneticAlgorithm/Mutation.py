import numpy as num
import random
import math
def Mutation(population,search_intervals):
    nr_bits=32
    minAx=num.min(population,axis=0)
    maxAx=num.max(population,axis=0)
    intervals=[minAx]
    intervals=num.concatenate((intervals,[maxAx]),axis=0)
    intervals=UniteIntervals(search_intervals,intervals)
    for i in range(len(population)):
        rand=random.random()
        chro=population[i,:]
        if rand<0.5:
            conv_chro=Convert2BinaryString(intervals,chro,nr_bits)
            conv_mutchro=[]
            for i in range(len(conv_chro)):
                conv_mutchro.append(OpMutation(conv_chro[i],nr_bits))
            mutChro=Convert2RealValues(intervals,conv_mutchro,nr_bits)
            population[i]=mutChro
    return population
            


def OpMutation(chro,nr_bits):
    temp2=temp1=random.randint(0,nr_bits-1)
    while temp2 is temp1:
        temp2=random.randint(0,nr_bits-1)
    interval=[temp1,temp2];interval.sort()
    strNumber='{0:010b}'.format(chro)
    for i in range(0,10):
        if i>= interval[0] and i <=interval[1]:
            if strNumber[i] is '1':
                strNumber=strNumber[:i]+'0'+strNumber[i+1:]
            else:
                strNumber=strNumber[:i]+'1'+strNumber[i+1:]
    mut_chro=long(strNumber,2)
    return mut_chro 
    
    

def Convert2BinaryString(intervals,chro,nr_bits):
    ss_chro=[]
    conv_chro=[]
    maxVal=long(math.pow(2,nr_bits)-1)
    for j in range(len(chro)): 
        temp=long((chro[j]-intervals[0][j])/(intervals[1][j]-intervals[0][j]+10e-10)*maxVal)
            #ss_chro.append('{0:010b}'.format(temp))
        conv_chro.append(temp)
    return conv_chro

def Convert2RealValues(intervals,chro,nr_bits):
    maxVal=float(math.pow(2,nr_bits)-1)
    conv_chro=[]
    for j in range(len(chro)):
        temp=chro[j]/maxVal*(intervals[1][j]-intervals[0][j])+intervals[0][j]
        conv_chro.append(temp)
    return conv_chro


def UniteIntervals(search_intervals,intervals):
    newIntervals=[]
    row1m=intervals[0]
    row2m=search_intervals[0]
    new_rowm=[]
    for i in range(len(row1m)):
        if row1m[i]<row2m[i]:
            new_rowm.append(row1m[i])
        else:
            new_rowm.append(row2m[i])
    
    newIntervals.append(new_rowm)

    row1M=intervals[1]
    row2M=search_intervals[1]
    new_rowM=[]
    for i in range(len(row1M)):
        if row1M[i]>row2M[i]:
            new_rowM.append(row1M[i])
        else:
            new_rowM.append(row2M[i])
    
    newIntervals.append(new_rowM)
    return newIntervals
        
