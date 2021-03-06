__author__ = 'iker'

#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import shutil
import sys
import re
import pyexiv2
def moverFotos(nombreFichero,origen):
  srcOrigen = os.path.join(origen,nombreFichero)
  print "srcOrigen" +srcOrigen
  nombreFecha = meta(srcOrigen)
  nombreFecha = nombreFecha.replace(":", "-")
  nombreFecha = nombreFecha[:10]
  nombreDefinitivo = nombreFecha + "_" + nombreFichero
  srcDestino = os.path.join(origen,nombreDefinitivo)
  rename(srcDestino,srcOrigen)
  directorio = os.path.join(nombreFecha)
  directorio = directorio.replace('\n', '')
  moveCap(srcDestino,directorio)


def meta(archivo):
    #Se crea la instancia metadata al pasarle el archivo que se quiere analizar
    metadata = pyexiv2.ImageMetadata(archivo)
    #Se lee el metadato
    metadata.read()
     #Se muestra en pantalla un mensaje

    print "Se muestra la informacion exif del archivo %s" %archivo

    print  "---------------------------------------------"

    #Se despliega la informacion de metadatos exif que contiene la imagen

    for metadato in metadata.exif_keys:

        texto = metadato + ": " + metadata[metadato].raw_value

        print texto
    fechaCaptura = metadata["Exif.Photo.DateTimeOriginal"].raw_value
    print "fechaCaptura" +fechaCaptura
    return fechaCaptura

def ordenarManualmente(nombreFichero,origen):
  directorio = os.path.join('Ordenar Manualmente')
  directorio = directorio.replace('\n', '')
  moveCap(os.path.join(origen,nombreFichero),directorio)

def peliculas(nombreFichero,origen):
  srcOrigen = os.path.join(origen,nombreFichero)
  print "srcOrigen" +srcOrigen
  nombrePelicula = srcOrigen
  pos = srcOrigen.find('[')
  if(pos != -1):
    nombrePelicula = srcOrigen[:pos]
  pos1 = srcOrigen.find('(')
  if(pos1 != -1):
    nombrePelicula = srcOrigen[:pos1]
  nombrePelicula = nombrePelicula.replace(".", "")
  nombrePelicula = nombrePelicula.replace("-" ,"")
  nombrePelicula = nombrePelicula.replace("\\" ,"")
  print 'nombrePelicula: ' + nombrePelicula
  extension = nombreFichero[-4:]
  nombreDefinitivo = nombrePelicula + extension
  srcDestino = os.path.join(origen,nombreDefinitivo)
  rename(srcDestino,srcOrigen)
  directorio = os.path.join('peliculas')
  directorio = directorio.replace('\n', '')
  moveCap(os.path.join(origen,nombreDefinitivo),directorio)

def subtitulos(nombreFichero,origen):
  posicionIdioma = nombreFichero.find('(Espa')
  if(posicionIdioma != -1):
    nombreSubtitulo = nombreFichero[:posicionIdioma]
    print 'nombreSubtitulo: ' + nombreSubtitulo
    p = re.compile(ur"\d?\d[x]\d\d")
    objTempCap = re.search(p, nombreFichero)
    #3x01
    if objTempCap is None:
      p = re.compile(ur'[Ss]\d\d[Ee]\d\d')
      objTempCap = re.search(p, nombreFichero)
    if objTempCap is not None:
      temporadaCapitulo = objTempCap.group()
      posicionTempCap = nombreFichero.find(temporadaCapitulo)
      temporadaCapitulo = temporadaCapitulo.upper()
      nombreSerie = nombreFichero[:posicionTempCap]
      nombreSerie = nombreSerie.replace(".", "")
      nombreSerie = nombreSerie.strip()
      #quitamos el anyo del nombre de la serie si lo tiene para que en el nombre final del capitulo no aprezca
      p = re.compile(ur'[(]?\d\d\d\d[)]?')
      objTempCap = re.search(p, nombreFichero)
      #(2010)
      nombreSerie = re.sub(p,'', nombreSerie)
      print 'nombreSerie ' + nombreSerie
      posicionX = temporadaCapitulo.find('X')
      print 'posicionX: ' + str(posicionX)
      if posicionX == -1:
        #S03
        temporada = temporadaCapitulo[:3]
        print 'Temporada: ' + temporada
        #E10
        capitulo = temporadaCapitulo[3:6]
        print 'Capitulo: ' + capitulo
      else:
        temporada = temporadaCapitulo[:posicionX]
        print 'temporada: ' + temporada
        capitulo = temporadaCapitulo[posicionX+1:]
        print 'capitulo: ' + capitulo
        if len(temporada) < 2:
          temporadaCapitulo = 'S0'+temporada + 'E' +capitulo
        else:
          temporadaCapitulo = 'S'+temporada + 'E' +capitulo
      print 'temporadaFinal: ' + temporada
      nombreSubtitulo = nombreSerie + " "+ temporadaCapitulo+'.srt'
      nombreSubtitulo = nombreSubtitulo.strip()
      print 'nombreSubtituloFinal: ' + nombreSubtitulo
      rename(os.path.join(origen,nombreSubtitulo),os.path.join(origen,nombreFichero))
      directorio = os.path.join('series',nombreSerie.strip(),temporadaCapitulo[:3].strip(),'subtitulos')
      directorio = directorio.replace('\n', '')
      moveCap(os.path.join(origen,nombreSubtitulo),directorio)

def series(nombreFichero,origen):
  srcOrigen = os.path.join(origen,nombreFichero)
  print "srcOrigen" +srcOrigen
  #Hawaii.Five-0.2010.S03E10.HDTV.x264-LOL.[VTV].mp4
  p = re.compile(ur'[Ss]\d\d[Ee]\d\d')
  objTempCap = re.search(p, srcOrigen)
  if objTempCap is not None:
    #S03E10
    temporadaCapitulo = objTempCap.group()
    posicionTempCap = srcOrigen.find(temporadaCapitulo)
    temporadaCapitulo = temporadaCapitulo.upper()
    nombreSerie = srcOrigen[:posicionTempCap]
    #quitamos el anyo del nombre de la serie si lo tiene para que en el nombre final del capitulo no aprezca
    p = re.compile(ur'[(]?\d\d\d\d[)]?')
    objTempCap = re.search(p, srcOrigen)
    if objTempCap is not None:
      #(2010)
      nombreSerie = re.sub(p,'', nombreSerie)
    #cambiamos los puntos por espacios
    nombreSerie = nombreSerie.replace(".", " ")
    nombreSerie = nombreSerie.replace("-" ,"")
    nombreSerie = nombreSerie.replace("\\" ,"")
    print 'nombreSerie: ' + nombreSerie
    print 'posicionTempCap: ' + str(posicionTempCap)
    print 'temporadaCapitulo: ' + temporadaCapitulo
    #S03
    temporada = temporadaCapitulo[:3]
    print 'Temporada: ' + temporada
    #E10
    capitulo = temporadaCapitulo[3:6]
    print 'Capitulo: ' + capitulo
    #nombre definitivo que se le va a dar al capitulo
    extension = nombreFichero[-4:]
    nombreDefinitivo = nombreSerie.strip() + " " + temporada.strip() +capitulo.strip() + extension
    srcDestino = os.path.join(origen,nombreDefinitivo)
    rename(srcDestino,srcOrigen)
    print 'nombre del capitulo: ' + nombreDefinitivo
    directorio = os.path.join('series',nombreSerie.strip(),temporada.strip(),'capitulos')
    directorio = directorio.replace('\n', '')
    moveCap(os.path.join(origen,nombreDefinitivo),directorio)

def moveCap(nombreDefinitivo,directorio):
  if not os.path.isdir(directorio):
    print 'no existe el directorio, creando...'
    os.makedirs(directorio)
    try:
      shutil.move(nombreDefinitivo, directorio)
    except Exception, e:
      print e.message
  else:
    print 'el directorio existe, moviendo...'
    try:
      shutil.move(nombreDefinitivo, directorio)
    except Exception, e:
      #episodio duplicado
      print e.message
def rename(nombreDefinitivo,nombreFichero):
  os.rename(nombreFichero,nombreDefinitivo)
def renombrarYMover(origen,destino):
   global archivos, ficheros
   totalesFotos = 0
   totalesCapitulos = 0
   totalesSubtitulos = 0
   totalesPeliculas = 0
   totalesManual = 0
   for (path, ficheros, archivos) in os.walk("."):
     pathEnCurso = path
     for fn in archivos:
       if (fn != "Order&Renom.py"):
         if (fn[-4:] == ".mp4") | (fn[-4:] == ".mkv") | (fn[-4:] == ".avi") | (fn[-5:] == ".mpeg"):
           p = re.compile(ur'[Ss]\d\d[Ee]\d\d')
           objTempCap = re.search(p, fn)
           if objTempCap is None:
             objTempCap = re.search(p, path)
           if objTempCap is not None:
             series(fn,path)
             totalesCapitulos += 1
           else:
             peliculas(fn,path)
             totalesPeliculas += 1
         else:
            if (fn[-4:] == ".JPG") | (fn[-5:] == ".jpeg"):
              moverFotos(fn,path)
              totalesFotos +=1
            else:
              if fn[-4:] == ".srt":
                subtitulos(fn,path)
                totalesSubtitulos +=1
              else:
                ordenarManualmente(fn,path)
                totalesManual += 1
   totales = 'Fotos movidas: ' + str(totalesFotos) + ' / Capitulos movidos: ' + str(totalesCapitulos) + ' / Subtitulos movidos: ' + str(totalesSubtitulos) + ' / Peliculas movidos: ' + str(totalesPeliculas) + ' / Orden manual: ' + str(totalesManual)
   return totales
 #Comienzo del programa
 #si el argumento correspondiente a origen es null se coge el directorio en actual
origen = os.getcwd()
print 'origen ' + origen
os.chdir(origen)
#si el argumento correspondiente a destino es null se coge el directorio en actual
destino = os.getcwd()
print 'destino ' + destino
totales = renombrarYMover(origen,destino)
print totales
raw_input("press enter to exit ;)")