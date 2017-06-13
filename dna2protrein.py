#!/Users/srrn/miniconda3/bin/python

# Find longest ORF in each DNA seq
# translate the ORF to proteins

# created: June 07, 2017
# Sukithar Rajan
##########################################

import sys
import os.path

#initialize variables
start_codon = 'ATG'
stop_codon = ('TAA', 'TAG', 'TGA')
dna_seq = 'AAATGACCGTAAATCCAGTATACGGACATTAATGAATGACAAATGACCGTAAATC'
amino_seq = 'MPRGQIMTGQ DWEPQVFNFQ NRNTGNKKPG RVNE*AEANRL'

# define functions
def rev_comp(dna_seq): # function for reverse complement
    complement = {'A':'T', 'T':'A', 'G':'C', 'C':'G'} # dictionary of nucleotides
    return ''.join([complement[base]for base in dna_seq[::-1]]) #go through a string backwards

"""
print(rev_comp('AGAGTCCCGACAT')) # test
for i in start_codon: # test
    print(rev_comp(i)) # test
"""
"""
start = dna_seq.find(start_codon)
if start != -1:
    print (len(dna_seq))

"""

def translate_to_protein(seq): # takes a DNA, finds the star codon, and returns amino acid
    start = seq.find('ATG')
    new_seq = seq[start:] # trim sequence from start codon

    gencode = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M', 'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K', 'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L', 'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q', 'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V', 'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E', 'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S', 'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_', 'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W'}

    peptide = ''
    for i in range(0, len(new_seq), 3):
        codon = new_seq[i: i+3]
        amino_acid = gencode.get(codon, '_')
        if amino_acid != '_':
            peptide += amino_acid
        else:
            break

    return peptide

#print('Protein:',translate_to_protein(dna_seq))

def distance_to_stop(seq_aa): # input amino acid and start codon, returns dist to first stop codon
    for j in (seq_aa):
        if '*' in j:
            stop_point = seq_aa.find('*')
            new_aa = seq_aa[:stop_point]
    return(len(new_aa))

#print(distance_to_stop(amino_seq))

"""
end_point = amino_seq.find('*')
new_aa = amino_seq[:end_point]
print(len(new_aa))

"""
