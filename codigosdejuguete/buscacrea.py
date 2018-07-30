# coding=utf-8
import os
from argparse import ArgumentParser




#----------------------------------------






def parse_args():
    
    argp = ArgumentParser(
        prog='nuevopaciente',
        version='1.0',
        description='Busca y crea carpetas con el dni del paciente',
        epilog='julio 2018, UBIT'
        )

    argp.add_argument('-d', '--dni', action = 'store', dest='dni', required=True, help='DNI del paciente que generará la carpeta raiz')
    argp.add_argument('-r', '--ruta', action = 'store', required=False, dest='ruta', default= './', help='ruta donde se desea crear la raiz de carpetas, por defecto se ubica donde se ejecuta el script. Sino, debe ingresar un path.')
    
    results = argp.parse_args()
    return results


#----------------------------- mkdir -p (-p crea cualquier directorio sup q no exista
#mkdir -p DNI/{fichapersonal,estudios/{ngs,bioq,etc}}


if __name__ == '__main__':
    argumentos = parse_args()
    print vars(argumentos)
    
    folder = argumentos.ruta+argumentos.dni
    if not os.path.exists(folder):
        os.makedirs(folder)

    