# coding=gbk

'''
Created on 2014-10-23

@author: dell
'''
import sys
import os

if len(sys.argv) != 3:
    print "FastaNGlysiteN2J fastafile AA_in_NX(AA)"
    sys.exit(0)
fasta = sys.argv[1]
fasta_N2J = fasta+".N2J"

fasta = open(fasta)
fasta_N2J = open(fasta_N2J,"w")

col = 80
reverse = False
sites = set(list(sys.argv[2]))

def N2J_with_NXST(seq):
    if seq[0] == "N" and len(seq) > 2:
        if seq[1] != "P" and seq[2] in sites:
            seq = "J" + seq[1:]
    for i in range(1,len(seq)-2):
        if seq[i] == "N":
            if seq[i+1] != "P" and seq[i+2] in sites:
                seq = seq[:i] + "J" + seq[i+1:]
    return seq

def Seq2MultiLine(seq):
    seqs = []
    num = (len(seq) / col)+1
    for i in range(num):
        if len(seq[i*col:(i+1)*col]) != 0:
            seqs.append(seq[i*col:(i+1)*col])
    return seqs

def MannReverse(rev_seq):
    for i in range(1,len(rev_seq)):
        if rev_seq[i] == "R" or rev_seq[i] == 'K':
            rev_seq = rev_seq[:i-1] + rev_seq[i] + rev_seq[i-1] + rev_seq[i+1:]
    return rev_seq

pre_seq = ""
pro_ac = ""
while True:
    line = fasta.readline()
    if line == "": break
    if line.startswith(">"):
        if pre_seq != "":
            pre_seq = N2J_with_NXST(pre_seq)
            seqs = Seq2MultiLine(pre_seq)
            rev_seq = pre_seq[::-1]
            fasta_N2J.writelines("\n".join(seqs)+"\n")
            #Reverse
            if reverse:
                fasta_N2J.write(">REVERSE_"+pro_ac[1:])
#                 rev_seq = MannReverse(rev_seq)
                seqs = Seq2MultiLine(rev_seq)
                fasta_N2J.writelines("\n".join(seqs)+"\n")
        pro_ac = line
        fasta_N2J.write(line)
        pre_seq = ""
    else:
        pre_seq += line[:-1]
if pre_seq != "":
    rev_seq = pre_seq[::-1]
    pre_seq = N2J_with_NXST(pre_seq)
    seqs = Seq2MultiLine(pre_seq)
    fasta_N2J.writelines("\n".join(seqs)+"\n")
    #Reverse
    if reverse:
        fasta_N2J.write(">REVERSE_"+pro_ac[1:])
#         rev_seq = MannReverse(rev_seq)
        rev_seq = N2J_with_NXST(rev_seq)
        seqs = Seq2MultiLine(rev_seq)
        fasta_N2J.writelines("\n".join(seqs)+"\n")
fasta.close()
fasta_N2J.close()

