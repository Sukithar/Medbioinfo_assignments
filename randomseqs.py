#!/Users/srrn/miniconda3/bin/python

# generating random DNA
# ask user to give the length of dna; generate a random
# dna seq in fasta format

# created: June 07, 2017
# Sukithar Rajan
##########################################

import sys
import random

nucleotide = list ('ATCG') # initialize the nucleotides

#ask user to give a target below 500 nucleotide
tar_length = int(input('Please enter the desired sequence length: '))

#function for fasta formatting
def format_fasta(name, sequence):
    fasta_string = '>' + name + '\n' + sequence + '\n'
    return fasta_string

dna = [random.choice(nucleotide) for i in range (tar_length)]
dna = ''.join(dna)
print('Length:',tar_length,'\n')
print(format_fasta('Your_sequence', dna))
