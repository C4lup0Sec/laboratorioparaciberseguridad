#!/usr/bin/env python

#https://mirrors.edge.kernel.org/pub/
#ftp.us.debian.org
#http://ftp.ntua.gr/pub/
#http://archie.icm.edu.pl/archie_eng.html
#http://ftp-sites.org/
#http://ftp.freebsd.org/pub/FreeBSD/


RUTA_SERVIDOR_FTP = 'http://ftp.freebsd.org/pub/FreeBSD/'
import ftplib

def cliente_ftp_conexion(servidor, nombre_usuario, correo):
#hacemos la apertura de la conexion
    ftp = ftplib.FTP(servidor, nombre_usuario, correo)
#listamos los archivos del directorio /pub
    ftp.cwd("/pub")
    print("Archivos disponibles en %s:" %servidor)
    archivos = ftp.dir()
    print (archivos)
    ftp.quit()

if __name__ == '__main__':
    cliente_ftp_conexion(servidor=RUTA_SERVIDOR_FTP, nombre_usuario='anonymous', correo='nobody@nourl.com',)