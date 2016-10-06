#Definition of the problem
# min f(x)=c.T*x
# A*x<=b
# x>=0
#,where A are  matrixes
# and b is a row vector
# c is a column
# x equal to [x1;x2;x3...] 

import numpy as num
import SimplexMethod

c=num.matrix('[3.0;3.0]')
A=num.matrix('[9.0 2.0;8.0 10.0]')
b=num.matrix('[196.0;105.0]')

def function1(X):
    #X has to be a column vector(matrix)
    return c.getT()*X


SimplexMethod.SimplexMethod(c,A,b)



