import random
import numpy as num

def CrossOver(conv_pop,nr_chromosome,nr_bits):
    new_pop=[]
    for i in range(len(conv_pop)):
        for j in range(i+1,len(conv_pop)):
            chro_i=conv_pop[i];chro_j=conv_pop[j]
            new_chro1=[];new_chro2=[]
            for k in range(len(chro_i)):
                chro1=chro_i[k];chro2=chro_j[k];
                (n_chro1,n_chro2)=OpCrossover2(chro1,chro2,10,nr_bits)
                new_chro1.append(n_chro1);new_chro2.append(n_chro2);
            new_pop.append(new_chro1)
            if len(new_pop) is nr_chromosome:
                return new_pop
            new_pop.append(new_chro2)
            if len(new_pop) is nr_chromosome:
                return new_pop
    return new_pop

def OpCrossover2(chro1,chro2,nr_rand,nr_bits):
    randNum=random.random()
    new_chro1=(chro1*randNum)+(chro2*(1-randNum))
    new_chro2=(chro2*randNum)+(chro1*(1-randNum))
    return (new_chro1,new_chro2)
def OpCrossover(chro1,chro2,nr_rand,nr_bits):
    val=GetRandNum(nr_rand,nr_bits)
    negVal=~val
    new_chro1=(val&chro1)|(negVal&chro2)
    new_chro2=(val&chro2)|(negVal&chro1)
    return (new_chro1,new_chro2)
    
    
def GetRandNum(nr_rand,nr_bits):
    randNum=[]
    while len(randNum) is not nr_rand:
        temp=random.randint(0,nr_bits-1)
        if not (temp in randNum):
            randNum.append(temp)
    randNum.sort()
    ss_op=''
    j=0
    val='1'
    for i in range(10):
        if i is not randNum[j]:
           ss_op+=val
        else :
            if val is '1':
                val='0'
            else:
                val='1'
            ss_op+=val
            if j < nr_rand-1:
                j+=1
    val=int(ss_op,2)
    return val
    
            
