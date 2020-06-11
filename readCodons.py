#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Given a string representing a strand of mRNA returns the polypeptide 
chain of amino acids it codes for.
Created on Wed Jun 10 11:46:53 2020

@author: bram
"""

# Import modules needed
import sys

# Dict of all possible codons 
codonDict = {
    'AUA':'I', 'AUC':'I', 'AUU':'I', 'AUG':'M',
    'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACU':'T',
    'AAC':'N', 'AAU':'N', 'AAA':'K', 'AAG':'K',
    'AGC':'S', 'AGU':'S', 'AGA':'R', 'AGG':'R',
    'CUA':'L', 'CUC':'L', 'CUG':'L', 'CUU':'L',
    'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCU':'P',
    'CAC':'H', 'CAU':'H', 'CAA':'Q', 'CAG':'Q',
    'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGU':'R',
    'GUA':'V', 'GUC':'V', 'GUG':'V', 'GUU':'V',
    'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCU':'A',
    'GAC':'D', 'GAU':'D', 'GAA':'E', 'GAG':'E',
    'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGU':'G',
    'UCA':'S', 'UCC':'S', 'UCG':'S', 'UCU':'S',
    'UUC':'F', 'UUU':'F', 'UUA':'L', 'UUG':'L',
    'UAC':'Y', 'UAU':'Y', #'UAA':'_', 'UAG':'_', 'UGA':'_',
    'UGC':'C', 'UGU':'C', 'UGG':'W'}

codon = '' # string to hold each codon
translation = '' # String to hold each 

with open(sys.argv[1]) as f:
    for string in f.readlines(): # Read each character in file one at a time
        for char in string:
            if char == "\n":
                continue # Don't include newline characters in the codon
            else:
                codon += str(char)
            # Once codon has three letters, convert to amino acid
            if len(codon) == 3:
                if not codonDict.get(codon): # Don't include if not in dictionary
                    codon = '' # reset codon 
                else:
                    translation += str(codonDict.get(codon)) # Add amino acid to translation string 
                    codon = '' # reset codon string 

print(f"Amino acid string is: {translation}")
