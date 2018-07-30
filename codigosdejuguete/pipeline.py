from subprocess import call

mode='PE'
SLIDINGWINDOW = argv.fdasfalñs

trimmer = ("java -jar ./trimmomatic-0.38.jar %s -trimlog ./trimm/trimming.log ./reads/ERR550644_1.fastq ./reads/ERR550644_2.fastq ./trimm/ERR550644_1p.fastq ./trimm/ERR550644_1u.fastq ./trimm/ERR550644_2p.fastq ./trimm/ERR550644_2u.fastq ILLUMINACLIP:./adapters/TruSeq3-PE.fa:2:30:10 LEADING:20 TRAILING:20 SLIDINGWINDOW:%s:20"%(mode,SLIDINGWINDOW))


print(trimmer)
call(trimmer, shell = True)
