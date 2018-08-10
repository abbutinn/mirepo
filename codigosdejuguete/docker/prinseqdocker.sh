#!/usr/bin/env bash
##llamada al docker de prinseq

sudo docker run -v /home/usuario/Escritorio/reads/:/datos -v /home/usuario/prinseq/:/output/ dceoy/prinseq perl \
prinseq-lite.pl -verbose -fastq /datos/ERR550644_L.fastq -fastq2 /datos/ERR550644_R.fastq \
-ns_max_n 0 -out_good /output/test_no_ns -out_bad /output/.test_with_ns
