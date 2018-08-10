workflow hellotrimmer {

    call trimmomatic
    call mostrarcabecera {input: cabecera=trimmomatic.salida2pareada}
    
}

task trimmomatic {
  File Trimmer
  String nombrevariable
  File entrada1
  File entrada2
  String modo
  File adaptador
  String parametrosadaptador
  String leading
  String slidingWindow
  String minlen


 command {
    java -jar ${Trimmer} ${modo} -trimlog ${nombrevariable}.log ${entrada1} ${entrada2} ${nombrevariable}_1p.fastq ${nombrevariable}_1u.fastq ${nombrevariable}_2p.fastq ${nombrevariable}_2u.fastq ILLUMINACLIP:${adaptador}${parametrosadaptador} LEADING:${leading} SLIDINGWINDOW:${slidingWindow} MINLEN:${minlen} 
   }
 
 output {
    
    File salida1pareada = "${nombrevariable}_1p.fastq"
    File salida1nopareada = "${nombrevariable}_1u.fastq"
    File salida2pareada = "${nombrevariable}_2p.fastq"
    File salida2nopareada = "${nombrevariable}_2u.fastq"
    File archivolog = "${nombrevariable}.log"
   
  }
 meta {
    author: "UBIT Agosto 2018"
    email: "ubit@ubit.com"
    }
}
  

task mostrarcabecera{
      File cabecera
      command{
          head ${cabecera} > cabeza.txt
      }
 output {
     File cabeza = "cabeza.txt"
 }


 
}






