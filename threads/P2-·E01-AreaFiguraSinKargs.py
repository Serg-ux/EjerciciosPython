import threading
import time


def Area(base, altura, figura):
  #time.sleep(1) descomentar para ver que no acaban los cálculos
  global areaTotal
  if figura=="triangulo":
    area = (base*altura)/2
  elif figura=="cuadrilatero":
    area = base*altura
  #print (area)
  #with lock:
  areaTotal += area

figuras = [["triangulo",10,12],["cuadrilatero",12,8],["cuadrilatero",6,5],["triangulo",2,5]]
lock = threading.Lock()
areaTotal=0
hilos = list()
for f in figuras: 
  t = threading.Thread(target=Area, args=(f[1], f[2],f[0]))
  hilos.append(t)
  t.start()

print (areaTotal)