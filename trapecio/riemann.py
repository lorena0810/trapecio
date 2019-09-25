import numpy as np
from mpi4py import MPI
import sys

def integral(a, b, tramos):
    h = (b - a) / tramos
    x = a
    suma = functionx(x)
    for i in range(0, tramos - 1, 1):
        x = x + h
        suma = suma + 2 * functionx(x)
    suma = suma + functionx(b)
    area = h * (suma / 2)
    return area

if __name__ == "__main__":
    
    comm = MPI.COMM_WORLD
    rank = comm.Get_rank()
    size = comm.Get_size()
    
    functionx = lambda x : np.cos(x) + x**3
 
    a = int(sys.argv[1])
    b = int(sys.argv[2])
    tramos = int(sys.argv[3])
    area_par = np.array(0 , dtype ='i')
    area_total = np.array(0 , dtype ='i')
    
    tramosproc = int(tramos/size)
    if(rank == 0):
        an = 0
        bn = an + tramosproc


        for j in range(1, size):

            for i in range(an, bn):
                area_par += integral(an, bn, i)
            an = an + tramosproc
            bn = bn + tramosproc

    comm.Reduce(area_par, area_total, op=MPI.SUM , root = 0)
    print("Area bajo la curva: ", area_total)