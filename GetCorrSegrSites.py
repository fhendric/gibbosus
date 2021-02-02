#!/usr/bin/python
#Script to extract SNPs and indels with expected genotypes for gibbosus locus
#Input file is FORMAT.GT file from VCFtools
import sys
import os
import re

##***********************************************************************************
##////////////////// Command line use ///////////////////////////////////////////////
##***********************************************************************************

def scancommandline():
        """ command line consists of flags, each with a dash, '-', followed immediately by a letter
                some flags should be followed by a value, depending on the flag.  The value can be placed
                immediately after the flag or spaces can be inserted """

        def pflag (tempname):   # Name of FORMAT.GT file
                global genfilename
                genfilename = tempname
        def mflag (tempname):   # Not used
                global scaffilename
                scaffilename = tempname

        cldic = {'p':pflag,'m':mflag}
        for i in range(1,len(sys.argv)):
                if sys.argv[i][0] == '-' :
                        flaglet = sys.argv[i][1].lower()
                        if len(sys.argv[i]) == 2:
                                if i == (len(sys.argv)-1):
                                        cldic[flaglet]()
                                else :
                                        if  sys.argv[i+1][0] == '-' :
                                                cldic[flaglet]()
                                        else :
                                                cldic[flaglet](sys.argv[i+1])
                                                i += 1
                        else :
                                print(sys.argv[i])
                                if (len(sys.argv[i]) < 2):
                                        print "problem on command line "
                                        exit()
                                cldic[flaglet](sys.argv[i][2:len(sys.argv[i])])


def printcommandset():
        print " Script to extract SNPs and indels with genotypes expected for gib locus"
        print " Expected genotype vector should be given manually in same order as FORMAT.GT file"
        print " Input file is FORMAT.GT file from vcftools"
        print " -p: original FORMAT.GT file"

##************************************************************##
##//////////////////////Program///////////////////////////////##
##************************************************************##

#setdefaults()
cmdstr=""
if len(sys.argv)<=1 : ## true if not run from command line with commands given on that line, use this so can run in IDLE and in cmd window
        sys.argv =cmdstr.split()  ## use the line defined in the program
if len(sys.argv)<=1 :
        printcommandset()
        sys.exit()
scancommandline()
sys.argv = []

#Core program

# Define vector of expected genotypes

geno_exp1=["1/1","1/1","0/0","0/0","0/0","0/1","0/1","0/0","0/0","0/1","0/1","0/0","0/1","0/0","0/1","0/0"]
geno_exp2=["0/0","0/0","1/1","1/1","1/1","0/1","0/1","1/1","1/1","0/1","0/1","1/1","0/1","1/1","0/1","1/1"]

geno_exp3=["./.","./.","0/0","0/0","0/0","0/0","0/0","0/0","0/0","0/0","0/0","0/0","0/0","0/0","0/0","0/0"]
geno_exp4=["./.","./.","1/1","1/1","1/1","1/1","1/1","1/1","1/1","1/1","1/1","1/1","1/1","1/1","1/1","1/1"]

geno_exp5=["0/0","0/0","./.","./.","./.","0/0","0/0","./.","./.","0/0","0/0","./.","0/0","./.","0/0","./."]
geno_exp6=["1/1","1/1","./.","./.","./.","1/1","1/1","./.","./.","1/1","1/1","./.","1/1","./.","1/1","./."]


Genome=open(genfilename)
for line in Genome:
    line=line.rsplit()
    if line[2:18]==geno_exp1 or line[2:18]==geno_exp2 or line[2:18]==geno_exp3 or line[2:18]==geno_exp4 or line[2:18]==geno_exp5 or line[2:18]==geno_exp6:
        if line[2:18]==geno_exp1:
                print "%s\t%s\tCT1\t1\t0" %(line[0],line[1])
        if line[2:18]==geno_exp2:
                print "%s\t%s\tCT2\t0\t1" %(line[0],line[1])
        if line[2:18]==geno_exp3:
                print "%s\t%s\tCT3\t.\t0" %(line[0],line[1])
        if line[2:18]==geno_exp4:
                print "%s\t%s\tCT4\t.\t1" %(line[0],line[1])
        if line[2:18]==geno_exp5:
                print "%s\t%s\tCT5\t0\t." %(line[0],line[1])
        if line[2:18]==geno_exp6:
                print "%s\t%s\tCT6\t1\t." %(line[0],line[1])

Genome.close()
