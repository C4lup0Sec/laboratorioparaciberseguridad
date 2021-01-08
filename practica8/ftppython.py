# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 13:31:07 2020

@author: wolf9
"""

from ftplib import FTP, FTP_PORT
from typing import List

 

def save_file(con: FTP, remote_file_path:str, local_file_path:str):
    with open(local_file_path,'wb') as local_file:
        con.retrbinary(f'RETR {remote_file_path}', local_file.write)

 

def get_txt_file(con: FTP, file_path:str):
    listado = []
    con.retrlines(f'RETR {file_path}', listado.append)
    return listado

 

def list_folder(con: FTP, directory:str):
    print(directory)
    listado = []
    con.retrlines(f'LIST {directory}', listado.append)
    return listado

 


def get_file_dir(con: FTP, directory:str):
    listado = list_folder(con,directory)
    return [file_info for file_info in listado if file_info.startswith('-')],  \
        [file_info for file_info in listado if not file_info.startswith('-')]

 

def get_file_name(file_info:str) -> str:
    return ''.join(file_info.split()[8:])

 

def connect_ftp(host:str, port:int = FTP_PORT, usr:str = '', pwd:str = '', save_path:str = ''):
    connection = FTP()
    connection.connect(host=host, port=port, timeout=3)
    connection.login(usr,pwd)
    actual_path = ''
    l_file, l_dir = get_file_dir(connection, actual_path)
    #print(f'files:\n{l_file}\ndirs:\n{l_dir}')
    #print(get_txt_file(connection, 'welcome.msg'))
    # save_file(connection, 'welcome.msg', f'{save_path}/welcome.msg')
    for file_info in l_file:
        file_name = get_file_name(file_info)
        print(file_name)
        save_file(connection, f'{actual_path}/{file_name}', f'{save_path}/{file_name}')
    #print(list_folder(connection, 'debian'))

 

    connection.close()

 

if __name__ == '__main__':
    # connect_ftp('192.168.11.3', 8022)
    connect_ftp('ftp.freebsd.org/pub/FreeBSD/', save_path='C:/Users/wolf9/Documents/Python Scripts/Laboratorio para ciberseguridad/laboratorioparaciberseguridad/practica8')
#https://mirrors.edge.kernel.org/pub/
#ftp.us.debian.org
#http://ftp.ntua.gr/pub/
#http://archie.icm.edu.pl/archie_eng.html
#http://ftp-sites.org/
#http://ftp.freebsd.org/pub/FreeBSD/
