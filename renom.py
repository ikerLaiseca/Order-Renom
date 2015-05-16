#!/usr/bin/python
# -*- coding: utf-8 -*-
import os
import time
import shutil
import sys
import re
def subtitulos(nombreFichero):
  #Hawaii Five 0 (2010) 3x01 - La O Na Makuahine (Mother's Day) (Español (España)).srt
  posicionIdioma = nombreFichero.find('(Espa')
  nombreSubtitulo = nombreFichero[:posicionIdioma]
  print 'nombreSubtitulo: ' + nombreSubtitulo
  p = re.compile(ur'\d?\d[x]\d\d')
  objTempCap = re.search(p, nombreFichero)
  #3x01
  temporadaCapitulo = objTempCap.group()
  posicionTempCap = nombreFichero.find(temporadaCapitulo)
  nombreSerie = nombreFichero[:posicionTempCap]
  #quitamos el anyo del nombre de la serie si lo tiene para que en el nombre final del capitulo no aprezca
  p = re.compile(ur'[(]?\d\d\d\d[)]?')
  objTempCap = re.search(p, nombreFichero)
  #(2010)
  nombreSerie = re.sub(p,'', nombreSerie)
  print 'nombreSerie ' + nombreSerie
  posicionX = temporadaCapitulo.find('x')
  print 'posicionX: ' + str(posicionX)
  temporada = temporadaCapitulo[:posicionX]
  print 'temporada: ' + temporada
  capitulo = temporadaCapitulo[posicionX+1:]
  print 'capitulo: ' + capitulo
  if len(temporada) < 2:
    temporadaCap = 'S0'+temporada + 'E' +capitulo
  else:
    temporadaCap = 'S'+temporada + 'E' +capitulo
  print 'temporadaFinal: ' + temporada
  posicionGuion = nombreFichero.find('-')
  nombreSegundaParte =nombreFichero[posicionGuion+1:posicionIdioma-1]
  nombreSubtitulo = nombreSerie + temporadaCap + nombreSegundaParte + '.srt'
  nombreSubtitulo = nombreSubtitulo.strip()
  print 'nombreSubtituloFinal: ' + nombreSubtitulo
  rename(nombreSubtitulo,nombreFichero)
  directorio = os.path.join('series',nombreSerie.strip(),temporadaCap[:3].strip(),'subtitulos')
  directorio = directorio.replace('\n', '')
  moveCap(nombreSubtitulo,directorio)

def series(nombreFichero):
  print 'mp4'
  #Hawaii.Five-0.2010.S03E10.HDTV.x264-LOL.[VTV].mp4
  p = re.compile(ur'[S]\d\d[E]\d\d')
  objTempCap = re.search(p, nombreFichero)
  #S03E10
  temporadaCapitulo = objTempCap.group()
  posicionTempCap = nombreFichero.find(temporadaCapitulo)
  nombreSerie = nombreFichero[:posicionTempCap]
  #quitamos el anyo del nombre de la serie si lo tiene para que en el nombre final del capitulo no aprezca
  p = re.compile(ur'[(]?\d\d\d\d[)]?')
  objTempCap = re.search(p, nombreFichero)
  #(2010)
  nombreSerie = re.sub(p,'', nombreSerie)
  #cambiamos los puntos por espacios 
  nombreSerie = nombreSerie.replace(".", " ")
  nombreSerie = nombreSerie.replace("-" ," ")
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
  rename(nombreDefinitivo.strip(),nombreFichero)
  print 'nombre del capitulo: ' + nombreDefinitivo
  directorio = os.path.join('series',nombreSerie.strip(),temporada.strip(),'capitulos')
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
   totalesSubtitulos = 0
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
      if fn[-4:] == ".srt":
        subtitulos(fn)
        totalesSubtitulos +=1
   totales = 'Fotos movidas: ' + str(totalesFotos) + ' / Capitulos movidos: ' + str(totalesCapitulos) + ' / Subtitulos movidos: ' + str(totalesSubtitulos)
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