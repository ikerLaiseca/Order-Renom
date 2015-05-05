#!/usr/bin/python
import os
import time
import shutil
fecha = time.strftime("%Y-%m-%d")
print 'fecha ' + fecha
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