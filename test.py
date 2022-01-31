import numpy as np
#from tdd import Ini_TDD,Index,Tensor
import tdd
from tdd.CUDAcpl import np2CUDAcpl
import torch
'''
u1 = np.zeros((2,2,2))
u2 = np.zeros((2,2,2))
u1[0,0,0]=2
u2[0,1,0]=3

U_c = np.array([u1,u2])
'''

U=np2CUDAcpl(1/np.sqrt(2)*np.array([2,2]))
#B = tdd.CUDAcpl.einsum3('...ab,...cd,...ef->...acebdf',U,U,U)
#B = tdd.CUDAcpl.einsum('...ab,...cd->...acbd',U,U)

#print(B)
print('============')
tdd1=tdd.as_tensor((U,[],[]))
tdd1.show(path='output_test',full_output=True)

print(tdd1.numpy())
print('yes')

exit()
