import numpy as np
import time


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
    
a = 1
b = 10
tramos = input("Numero de Trapecios: ") 

start_time = time.process_time() 

    
for i in range(1, int(tramos)):
    print("Trapecios: " , i, "Area: " , integral(a, b, i))
    
print("Tiempo de ejecución: " + str(time.process_time() - start_time))