from . import main 
from . import quantum_basic
import torch
from .config import device

print()
print('# DEVICE : ' + device)
print()

torch.set_printoptions(precision=15)


#the data type provided
CUDAcpl_Tensor = main.CUDAcpl_Tensor

_U_ = main ._U_
np2CUDAcpl = main .np2CUDAcpl
CUDAcpl2np = main .CUDAcpl2np
norm = main .norm
einsum1 = main .einsum1
einsum = main .einsum
einsum3 = main .einsum3
tensordot = main .tensordot
scale = main .scale
e_i_theta = main .e_i_theta

eye = main.eye
ones = main.ones
zeros = main.zeros

conj = main .conj