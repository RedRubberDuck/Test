import numpy as num
import math

def SimplexMethod(c,A,b):
    nr_of_eq=len(b)

    #Initailized
    Identity_array=num.identity(nr_of_eq)
    Zeros_array=num.zeros([1,nr_of_eq+1])
    A_array=A.getA()
    M=num.concatenate((A_array,Identity_array,b.getA()),axis=1)
    M_l=num.concatenate((c.getT().getA(),Zeros_array),axis=1)
    M=num.concatenate((M,M_l),axis=0)
    run=True
    while run:
        max_iA=num.argmax(M,axis=1)
        lasteq_i=len(max_iA)-1
        col_index=max_iA[lasteq_i]
        if M[lasteq_i,col_index]<=0:
            run=False
            break
        last_col=len(M[0])-1
        col=M[:,col_index]
        if max(col)<=0:
            run=False
            break
        
        lastcol=M[:,last_col]
    
        div=lastcol/col
        div=div[0:len(div)-1]
        row_index=num.argmin(div)

        pivotVal=M[row_index,col_index]
        M[row_index]=M[row_index,:]/pivotVal
        for i in range(len(M)):
            if i is not int(row_index):
                M[i]=M[i,:]-M[i,col_index]*M[row_index,:]
    
    print M
    
    
    
