#!/usr/bin/python
import os
import time
import shutil
import sys
def renombrarYMover(origen,destino):
   fecha = time.strftime("%Y-%m-%d")
   totalesFotos = 0
   totalesPeliculas = 0
   print 'fecha ' + fecha
   for fn in os.listdir(origen):
      if fn[-4:] == ".jpg":
         nombre=fn[0:-4:]
        #eliminamos espacios en blanco a izq y dcha
        nombre.strip()
        nn='' 
        nn=fecha + '_' + nombre + '.jpg'
        print 'nombre de la foto ' + nn
        os.rename(fn,nn)
        shutil.move(fn,destino)
        totalesFotos += 1
      if fn[-4:] == ".avi":
        nombre=fn[0:-4:]
        #eliminamos espacios en blanco a izq y dcha
        nombre.strip()
        nombre.lstrip('[]')
        print 'nombre de la pelicula ' + nombre
        os.rename(fn,nombre)
        totalesPeliculas += 1
   totales = 'Fotos movidas: ' + str(totalesFotos) + ' / Peliculas movidas: ' + str(totalesPeliculas) 
   return totales
 #Comienzo del programa
 #si el argumento correspondiente a origen es null se coge el directorio en actual
if len(sys.argv) > 2:
   origen = sys.argv[1]
else:
   origen = os.getcwd()
print 'origen ' + origen
#si el argumento correspondiente a destino es null se coge el directorio en actual
if len(sys.argv) > 3:
   destino = sys.argv[2]
else:
   destino = os.getcwd()
print 'destino ' + destino
totales = renombrarYMover(origen,destino)
print totales