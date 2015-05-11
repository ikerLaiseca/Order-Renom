#!/usr/bin/python
import os
import time
import shutil
import sys
import re
def series(nombreFichero):
  print 'mp4'
  #Hawaii.Five-0.2010.S03E10.HDTV.x264-LOL.[VTV].mp4
  p = re.compile(ur'[S]\d\d[E]\d\d')
  objTempCap = re.search(p, nombreFichero)
  #S03E10
  temporadaCapitulo = objTempCap.group()
  posicionTempCap = nombreFichero.find(temporadaCapitulo)
  nombreSerie = nombreFichero[:posicionTempCap]
  #quitamos el anyo del nombre de la serie para que en el nombre final del capitulo no aprezca
  nombreSerie = nombreSerie[:-6]
  #cambiamos los puntos por espacios 
  nombreSerie = nombreSerie.replace(".", " ");
  print 'nombreSerie: ' + nombreSerie
  print 'posicionTempCap: ' + str(posicionTempCap)
  print 'temporadaCapitulo: ' + temporadaCapitulo
  #S03
  temporada = temporadaCapitulo[:3]
  print 'Temporada: ' + temporada;
  #E10
  capitulo = temporadaCapitulo[3:6]
  print 'Capitulo: ' + capitulo
  #nombre definitivo que se le va a dar al capitulo
  nombreDefinitivo = nombreSerie + " " + temporada +capitulo + '.mp4'
  rename(nombreDefinitivo,nombreFichero)
  print 'nombre del capitulo: ' + nombreDefinitivo
  directorio = os.path.join('series',nombreSerie,temporada)
  directorio = directorio.replace('\n', '')
  moveCap(nombreDefinitivo,directorio)
def moveCap(nombreDefinitivo,directorio):
  print 'directorio: ' + directorio
  if not os.path.isdir(directorio):
    print 'no existe el directorio, creando...'
    os.makedirs(directorio)
    shutil.move(nombreDefinitivo, directorio)
  else:
    print 'el directorio existe, moviendo...'
    shutil.move(nombreDefinitivo, directorio)
def rename(nombreDefinitivo,nombreFichero):
  os.rename(nombreFichero,nombreDefinitivo)
def renombrarYMover(origen,destino):
   fecha = time.strftime("%Y-%m-%d")
   totalesFotos = 0
   totalesCapitulos = 0
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
      if fn[-4:] == ".mp4":
        series(fn)
        totalesCapitulos += 1
   totales = 'Fotos movidas: ' + str(totalesFotos) + ' / Capitulos movidos: ' + str(totalesCapitulos) 
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