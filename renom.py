#!/usr/bin/python
import os
import time
import shutil
def renombrarYMover(origen,destino):
	fecha = time.strftime("%Y-%m-%d")
	print 'fecha ' + fecha
	#coge el directorio actual
	origen = os.getcwd()
	print 'origen ' + origen
	destino = os.getcwd()
	print 'destino ' + destino
	for fn in origen:
  	if fn[-4:] == ".jpg":
   		nombre=fn[0:-4:]
   		nn='' 
   		nn=fecha + '_' + nombre + '.jpg'
   		os.rename(fn,nn)
   		shutil.move(fn,destino)
   	if fn[-4:] == ".avi":
   		nombre=fn[0:-4:]
   		#eliminamos espacio
   		nombre.strip()
   		nombre.lstrip('[]')
   		os.rename(fn,nombre)
  #Comienzo del programa
try:
	origen = sys.argv[1]
	destino = sys.argv[2]
except IndexError:
	raise SystemExit("Número de parámetros incorrectos, introduce ruta de origen y de destino")

renombrarYMover(origen,destino)