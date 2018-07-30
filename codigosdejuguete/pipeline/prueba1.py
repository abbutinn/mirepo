from subprocess import call
impor shutil

#funciones

def checkTools():
    '''chequeo de requerimientos del sistema'''

    print("\n\n Chequeando las librerias y componentes requeridos\n\n")

    if param.strip() == '@Trimmomatic_PATH':
                    global Trimmomatic_PATH
                    Trimmomatic_PATH = str(value.strip())
                    print('User Input Trimmomatic_PATH  :',Trimmomatic_PATH)
    sys.exit()

trimmer = ("java -jar ~/usuario/herramientas/Trimmomatic-0.38/trimmomatic-0.38.jar SE -phred33 archivoentrada")