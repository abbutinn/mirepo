# coding=utf-8
import os
import subprocess
from argparse import ArgumentParser
#from subprocess import call, Popen, PIPE, STDOUT


#----------------------------------------
#trimmomatic acepta: tipo de secuencia (PE o SE),[-threads][-phred33|phred64],[-trimlog], Secuencia1, secuencia2, output_1_pa,out_2_pa,out_1_un,out_2_un, ILLUMINACLIP:<(path en fasta)fastaWithAdaptersEtc>:<seed mismatches>:<palindrome clip threshold>:<simple clip threshold> 
#

#ILLUMINACLIP: Cut adapter and other illumina specific sequences from the read.

#SLIDINGWINDOW: Performs a sliding window trimming approach. It starts scanning at the 5‟ end and clips the read once the average quality within the window falls below a threshold. 

#MAXINFO: An adaptive quality trimmer which balances read length and error rate to maximise the value of each read.
#LEADING: Cut bases off the start of a read, if below a threshold quality.
#TRAILING: Cut bases off the end of a read, if below a threshold quality.
#CROP: Cut the read to a specified length by removing bases from the end.
#HEADCROP: Cut the specified number of bases from the start of the read.
#MINLEN: Drop the read if it is below a specified length.
#AVGQUAL: Drop the read if the average quality is below the specified level.
#TOPHRED33: Convert quality scores to Phred-33.
#TOPHRED64: Convert quality scores to Phred-64.
#



def parse_args():
    
    argp = ArgumentParser(
        prog='trimmer',
        version='1.0',
        description='Alimenta el programa Trimmomatic',
        epilog='julio 2018, UBIT'
        )

    argp.add_argument('-t', '--trimmer', action = 'store', dest='trimmer', required=False, default='./trimmomatic-0.38.jar', help='ruta del trimmer, por defecto el script se ubica en la misma carpeta que el trimmer')
    argp.add_argument('-m', '--modo', action = 'store', required=False, dest='modo',choices=['PE', 'SE'], default= 'PE', help='Modo del programa: Paired End o Single End')
    argp.add_argument('-n', '--nodos', action = 'store', dest='nodos', required=False, help='Cantidad de nodos a utilizar, por defecto utiliza los disponibles')
    argp.add_argument('-b', '--base', action = 'store', required=False, dest='base',choices=['-phred33', '-phred64'], default= '-phred64', help='calidad de la base codificadora -phred33 o -phred64. Por defecto utiliza -phred64')
    argp.add_argument('-l','--log', action = 'store', dest='trimlog', required = False, help='Path donde se quiere guardar el log del trimmer')
    argp.add_argument('-i1', '--input1', action = 'store', dest='input1', required=True, help='primer secuencia')
    argp.add_argument('-i2','--input2', action = 'store', dest='input2', required = False, help='segunda secuencia, esta puede ser opcional')
  
    
    ##ILLUMINACLIP:<fastaWithAdaptersEtc>:<seed mismatches>:<palindrome clip threshold>:<simple clip threshold>
    ##fastaWithAdaptersEtc: specifies the path to a fasta file containing all the adapters, PCR sequences etc. The naming of the various sequences within this file determines how they are used. See below.
    argp.add_argument('-a','--adaptadores',action='store', dest ='adaptadores', required = False, default = './adapters/TruSeq3-PE.fa' , help='ILLUMINACLIP:<fastaWithAdaptersEtc> archivo de adaptadores')
    ##seedMismatches: specifies the maximum mismatch count which will still allow a full match to be performed
    argp.add_argument('-sd','--seed_mismatches',action='store', dest ='seed_mismatches', required = False , default='2', help='seedMismatches: specifies the maximum mismatch count which will still allow a full match to be performed. Default 2')
    ##palindromeClipThreshold: specifies how accurate the match between the two 'adapter ligated' reads must be for PE palindrome read alignment.
    argp.add_argument('-pct','--palindromeClipThreshold', action='store', dest ='palindromeClipThreshold', required = False , default = '30' , help='specifies how accurate the match between the two adapter ligated reads must be for PE palindrome read alignment. Default 30')
    ##simpleClipThreshold: specifies how accurate the match between any adapter etc. sequence must be against a read.
    argp.add_argument('-sct','--simpleClipThreshold',action='store', dest ='simpleClipThreshold', required = False , default = '10', help='specifies how accurate the match between any adapter etc. sequence must be against a read. Default 10')


  

    

    

    

    

    
    
    
    
    
    
        
        #windowSize: specifies the number of bases to average across
        #requiredQuality: specifies the average quality required.
    argp.add_argument('-ws','--windowSize',action='store', dest ='windowSize', required = False , default= '4', help='specifies the number of bases to average across. Default 4')
    argp.add_argument('-rq','--requiredQuality',action='store', dest ='requiredQuality', required = False ,default='20', help='specifies the average quality required. Default 20')
    
    
    #LEADING:<quality>
        #quality: Specifies the minimum quality required to keep a base.
    argp.add_argument('-lq','--leadingQuality',action='store', dest ='leadingQuality', required = False , default='20', help='Specifies the minimum quality required to keep a base. Default 20')
    
    #TRAILING:<quality>
        #quality: Specifies the minimum quality required to keep a base.
    argp.add_argument('-tq','--trailingQuality',action='store', dest ='trailingQuality', required = False , default='20', help='Specifies the minimum quality required to keep a base. Default 20')
    
    #CROP:<length>
        #length: The number of bases to keep, from the start of the read.
    argp.add_argument('-cl','--cropLength', action='store', dest ='cropLength', required = False , help='The number of bases to keep, from the start of the read.')
     
    #HEADCROP:<length>
        #length: The number of bases to remove from the start of the read.
    argp.add_argument('-hc','--headCrop', action='store', dest ='headCrop', required = False , help='The number of bases to remove from the start of the read.')
     
     
    #MINLEN:<length>
        #length: Specifies the minimum length of reads to be kept. 
    argp.add_argument('-ml','--minLen', action='store', dest ='minLen', required = False , default= '50', help='Specifies the minimum length of reads to be kept. Default 50')
     
    parametros = argp.parse_args()
    return parametros

###

def main():

    argumentos = parse_args()
    #print vars(argumentos)
    
    nombrevariable1= os.path.splitext(os.path.basename(argumentos.input1))[0]
    nombrevariable2= os.path.splitext(os.path.basename(argumentos.input2))[0]
    extencion=os.path.splitext(os.path.basename(argumentos.input2))[1]
    
    carpeta=nombrevariable1[:-2]
    
    
    if not os.path.exists(carpeta):
        os.makedirs(carpeta)
    
    
    ubicacion=argumentos.trimmer
    mode=argumentos.modo
    nodo=argumentos.nodos
    calidad=argumentos.base
    archivolog=carpeta+'/'+carpeta+'.log'
    entrada1=argumentos.input1
    entrada2=argumentos.input2
    
   
   #output trimeador
    salida1pareada=carpeta+'/'+nombrevariable1+'p'+extencion
    salida1nopareada=carpeta+'/'+nombrevariable1+'u'+extencion
    salida2pareada=carpeta+'/'+nombrevariable2+'p'+extencion
    salida2nopareada= carpeta+'/'+nombrevariable2+'u'+extencion
    
    
    adapt=argumentos.adaptadores
    seedm=argumentos.seed_mismatches
    pct=argumentos.palindromeClipThreshold
    sct=argumentos.simpleClipThreshold
    ws=argumentos.windowSize
    req=argumentos.requiredQuality
    leading=argumentos.leadingQuality
    trailing=argumentos.trailingQuality
    minlen=argumentos.minLen
    
    
    
    trimmer = ("java -jar %s %s -trimlog %s %s %s %s %s %s %s ILLUMINACLIP:%s:%s:%s:%s LEADING:%s TRAILING:%s SLIDINGWINDOW:%s:%s MINLEN:%s"%(ubicacion,mode,archivolog,entrada1,entrada2, salida1pareada, salida1nopareada, salida2pareada, salida2nopareada, adapt,seedm, pct,sct, leading,trailing,ws,req,minlen))

    print(trimmer)
    subprocess.call(trimmer, shell = True)
   
   #trimmer = subprocess.Popen(("java -jar %s %s -trimlog %s %s %s %s %s %s %s ILLUMINACLIP:%s:%s:%s:%s LEADING:%s TRAILING:%s SLIDINGWINDOW:%s:%s MINLEN:%s"%(ubicacion,mode,archivolog,entrada1,entrada2, salida1pareada, salida1nopareada, salida2pareada, salida2nopareada, adapt,seedm, pct,sct, leading,trailing,ws,req,minlen)), stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell= True)
   
   
   
   
   
    ###captura de salida y posibles errores
    
   # captura= subprocess.Popen(trimmer, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell= True)
    #errorEncontrado= trimmer.stderr
    #datosPantalla= trimmer.stdout    
    #trimmer.stderr.close()
    #trimmer.stdout.close()
    
    #if not errorEncontrado:
        #print(datosPantalla)
    #else:
        #print("se produjo el siguiente error: %s" %(errorEncontrado))
    
    

if __name__ == '__main__':
    
    main()
    
    
    
    

    