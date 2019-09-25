import numpy as np
import time
from mpi4py import MPI


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

functionx = lambda x : np.cos(x) + x**3
    
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
    
if comm.rank==0:    
    a = 1
    b = 10
    tramos = input("Numero de Trapecios: ")   
    trabajos = range(int(tramos)+1)
    data = {'a':a,'b':b,'tramos':tramos,'trabajos':trabajos}    
else: 
    data = None    

start_time = time.process_time() 
    
data = comm.bcast(data,root=0)
    
for i,task in enumerate(data['trabajos']):
    if i%size!=rank: continue        
    for j in range(1, int(data['tramos'])):
        if i!= 0:
            print('Hilo: ', str(comm.rank), "Trapecio: " , i, "Area: " , integral(data['a'], data['b'], i))
        break
        
total_time = time.process_time() - start_time
run_time = comm.gather(total_time,0)
if comm.rank == 0:
    print(run_time)
    print(np.sum(run_time))
