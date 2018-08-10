workflow helloprinseq {

    call prinseq
    call mostrarcabecera {input: outgood=prinseq.test_no_ns, outbad=prinseq.test_with_ns}
    
}

task prinseq {
  
  File entrada1
  File entrada2
  

 command {
    perl prinseq-lite.pl -verbose -fastq ${entrada1} -fastq2 ${entrada2} -ns_max_n 0 -out_good test_no_ns -out_bad test_with_ns
   }

 runtime {
    docker:"dceoy/prinseq"
  }

 output {
    
    File test_no_ns = "test_no_ns"
    File test_with_ns = "test_with_ns"
    
   
  }
 meta {
    author: "UBIT Agosto 2018"
    email: "ubit@ubit.com"
    }
}
  

task mostrarcabecera{
      File outgood
      File outbad
      command{
          head ${outgood} > outgood.txt \
          head ${outbad} > outbad.txt
      }
 output {
     File outgood1 = "outgood.txt"
     File outbad1 = "outbad.txt"
 }


 
}

