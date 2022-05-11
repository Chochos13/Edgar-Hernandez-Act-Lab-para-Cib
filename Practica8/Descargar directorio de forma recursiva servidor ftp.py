#! /usr/bin/python # -*- coding: utf-8 -*
 # import unittest # Unit test case
import os
import re
import sys
import datetime,time
 desde ftplib import FTP # Define la clase FTP para implementar la carga y descarga ftp
import traceback
import logging
 
 LOG_FORMAT = "% (message) s" # "% (asctime) s% (name) s% (levelname) s% (pathname) s% (message) s" #Configure el formato de registro de salida
 DATE_FORMAT = '% Y-% m-% d% H:% M:% S% a' # Configure el formato del tiempo de salida, preste atención al mes y al número de días que no se confunden
LOG_PATH = None#os.path.join(os.getcwd(),'./logs/ftpget.log')
logging.basicConfig(level=logging.DEBUG,
                    format=LOG_FORMAT,
                    datefmt = DATE_FORMAT ,
                                         filemode = 'a', # Sobrescribe el registro anterior 'a' se agrega
                                         filename = LOG_PATH # Con el parámetro de nombre de archivo, no se enviará directamente a la consola, sino que se escribirá directamente en el archivo
                    )
 
'''
 @Compruebe si la descarga está completa
'''
def IsDownloadCompletely(RemoteFile, LocalFile, remote_size):
    p = re.compile(r'\\',re.S)
    LocalFile = p.sub('/', LocalFile)
    localsize = os.path.getsize(LocalFile)
    if localsize == remote_size:
        print('downloading  %s ...Successs! remote_size:%d , local_size:%d.' %(RemoteFile, remote_size, localsize))
        logging.debug('downloading  %s ... Successs! remote_size:%d , local_size:%d.' %(RemoteFile, remote_size, localsize))
        return True
    else:
        print('downloading  %s ...Successs! remote_size:%d , local_size:%d.' %(RemoteFile, remote_size, localsize))
        logging.debug('downloading  %s ... Successs! remote_size:%d , local_size:%d.' %(RemoteFile, remote_size, localsize))
        return False
 
'''
 @ La función real responsable de la función de descarga
'''
def ftp_download(LocalFile, RemoteFile, bufsize, ftp):
         # ¿Este archivo está disponible localmente?
    if not os.path.exists(LocalFile):
        with open(LocalFile, 'wb') as f:
            ftp.retrbinary('RETR %s' % RemoteFile, f.write, bufsize)
                         # ftp.set_debuglevel (0) # Desactivar el modo de depuración
        
                 # Aquí el archivo se cancelará y se colocará fuera de la declaración with
        return IsDownloadCompletely(RemoteFile, LocalFile, bufsize)
    else:
        if not IsDownloadCompletely(RemoteFile, LocalFile, bufsize):
                         # Si ya existe, pero está incompleto, reescribir sobrescribir 
            with open(LocalFile, 'wb+') as f:
                ftp.retrbinary('RETR %s' % RemoteFile, f.write, bufsize)
            
                         # Aquí el archivo se cancelará y se colocará fuera de la declaración with    
            return IsDownloadCompletely(RemoteFile, LocalFile, bufsize)
"""
 # Descargar archivo basado en el prefijo del nombre del archivo
"""
def DownLoadRUledFile(LocalDir, RemoteDir, filename, ftp):
    print("RemoteDir:", RemoteDir)
 
    if not os.path.exists(LocalDir):
        os.makedirs(LocalDir)
         Local = os.path.join (LocalDir, nombre de archivo) # Descargar a la ruta local completa
    
    try:
                 # Abra el directorio remoto
        ftp.cwd(RemoteDir)
                 #Descargar
                 ftp.voidcmd ('TYPE I') # Cambie el modo de transmisión a modo binario para evitar el mensaje ftplib.error_perm: 550 SIZE no permitido en ASCII
                 bufsize = ftp.size (nombre de archivo) # Tamaño total del archivo en el servidor
        #print(bufsize)
        ftp_download(Local, filename, bufsize, ftp)
    except:
        print('some error happend in get file:%s. Err:%s' %(filename, traceback.format_exc()))
        logging.debug('some error happend in get file:%s. Err:%s' %(filename, traceback.format_exc()))
    
    return
 
"""
 Descargar archivos en todo el directorio
"""
def DownLoadFileTree(LocalDir, RemoteDir, ftp, IsRecursively=False):
    print("RemoteDir:", RemoteDir)
 
    if not os.path.exists(LocalDir):
        print('local directory %s not exists , make it ...')
        os.makedirs(LocalDir)
    
         # Abra el directorio remoto
    ftp.cwd(RemoteDir)
    dir_list = []
         '' 'Dirige el directorio actual y coloca el resultado en la lista' ''
    ftp.dir('.', dir_list.append)
    for dif in dir_list:
        if dif.startswith("d"):
            if IsRecursively:
                                 '' 'El objeto es un directorio Descarga recursiva' ''
                print('%s is a directory, download it Recursively...' %(dif))
                p_subdir = dif.split(" ")[-1]
                p_local_subdir = os.path.join(LocalDir, p_subdir)
                                 '' 'El principio de crear subdirectorios locales es el mismo, pero no se crea aquí.
                p_remote_subdir = os.path.join(ftp.pwd(), p_subdir)
                DownLoadFileTree(p_local_subdir, p_remote_subdir, ftp)
                                 ftp.cwd ("..") # Regresar al lado más externo de la ruta
            else:
                print('%s is a directory, download mode is UnRecursive, continue...' %(dif))
                continue
        else:
                         '' 'Es un archivo para descargar directamente' ''
            print('%s is a file, download it directly...' %(dif))
            p_filename = dif.split(" ")[-1]
                         bufsize = ftp.size (p_filename) # Tamaño total del archivo en el servidor
                         Localfile = os.path.join (LocalDir, p_filename) # Descargar a la ruta local completa
            ftp_download(Localfile, p_filename, bufsize, ftp)
    return
if __name__ == '__main__':  
    host = 'Direccion IP del servidor FTP'
    port = 21 #Casi es default este puerto
    username = 'Usuario del servidor'
    password = 'Contraseña del servidor'
    ftp = FTP()
    ftp.connect(host,port)
    ftp.login(username, password)
         '' 'Descargar por nombre de archivo' ''
    LocalDir = os.getcwd()
    RemoteDir = '/home/li'
    filename = 'readme.txt'
    #DownLoadRUledFile(LocalDir, RemoteDir, filename, ftp)
         '' 'Descargar todo el directorio de forma recursiva' ''
         IsRecursively = True # Ya sea para cambiar subdirectorios bajo el directorio recursivo Sí Verdadero No Falso
    DownLoadFileTree(LocalDir, RemoteDir, ftp, IsRecursively)