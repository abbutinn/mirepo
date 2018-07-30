# -*- coding: utf-8 -*-

from optparse import OptionParser
import glob
import os
import gzip
import sys


#clase ReadRecord que le cambie de nombre a LeoRegistro (thread)
class LeoRegistro:
    def __init__(self,thread):
        self.pareado = False
        self.thread = thread
        self.muestra  = ()
        self.sample2len = dict()
        self.sample2phred = dict()

##design_f a archivodisenio-----read_design a leo_disenio
    def leo_disenio(self, archivodisenio):
        with open(archivodisenio, 'r') as design_f:
            lines = [line.rstrip().split("\t") for line in design_f]
            if len(lines[0]) == 3:
                self.pareado = True
            elif len(lines[0]) == 2:
                self.pareado = False
            else:
                print("Formato incorrecto, por favor chequee el archivo")
            if self.paired :
                if lines[0][2] != 'right':
                    sys.exit("Por favor chequee el encabezado del arvhico")
            self.muestra = lines[1:]

### chequeo fastq

def check_fastq(self):
        for sample_record in self.samples:
            first_fqgz = sample_record[1]
            sample_name = sample_record[0]
            sample_name.replace(' ', '_')
            # get the phred format
            len_max = 0
            qual_min = 1000
            qual_max = 0
            with gzip.open(first_fqgz, "rt") as fqgzIN:
                count = 0
                limit = 200
                qual_str_all = ''
                for line in fqgzIN:
                    count += 1
                    if count > limit:
                        break
                    if count % 4 == 0:
                        qual_str = line.rstrip()
                        qual_str_all += qual_str
                        if len_max < len(qual_str):
                            len_max = len(qual_str)
                for qual_char in qual_str_all:
                    qual = ord(qual_char)
                    if qual_min > qual:
                        qual_min = qual
                    if qual_max < qual:
                        qual_max = qual
            if qual_min < 33 or qual_max > 105:
                sys.exit("Quality values corrupt. found [$min; $max] where [33; 104] was expected \n")
            if qual_min >= 59 and qual_max <= 110:
                qual_out = '64'
            elif qual_min >= 33 and qual_max <= 74:
                qual_out = '33'
            else:
                sys.exit("May be new fastq format \n")
            # output to class
            self.sample2len[sample_name] = len_max
self.sample2phred[sample_name] = qual_out