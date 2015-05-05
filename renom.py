#!/usr/bin/python
import os
import time
import shutil
def renombrarYMover(origen,destino):
	fecha = time.strftime("%Y-%m-%d")
	print 'fecha ' + fecha
	print 'origen ' + origen
	print 'destino ' + destino
	for fn in origen:
  	if fn[-4:] == ".jpg":
   		nombre=fn[0:-4:]
   		#eliminamos espacios en blanco a izq y dcha
   		nombre.strip()
   		nn='' 
   		nn=fecha + '_' + nombre + '.jpg'
   		os.rename(fn,nn)
   		shutil.move(fn,destino)
   	if fn[-4:] == ".avi":
   		nombre=fn[0:-4:]
   		#eliminamos espacios en blanco a izq y dcha
   		nombre.strip()
   		nombre.lstrip('[]')
   		os.rename(fn,nombre)
 #Comienzo del programa
 #si el argumento correspondiente a origen es null se coge el directorio en actual
if sys.argv[1] != null:
	origen = sys.argv[1]
else:
	origen = os.getcwd()
#si el argumento correspondiente a destino es null se coge el directorio en actual
if sys.argv[2] != null:
	destino = sys.argv[2]
else:
	destino = os.getcwd()
	
renombrarYMover(origen,destino)