#!/usr/bin/env python3
# SUTD 50.020 Security Lab 1
# Simple file read in/out
# Quyen, 2014

# Import libraries
import sys
import argparse
import string

def doStuff(filein,fileout,key,mode):
    # open file handles to both files
    len_printable = len(string.printable)
    if key<1 or key>len_printable-1:
        print("Please input valid key value (-1<k<1)")
        return

    fin  = open(filein, mode='r', encoding='utf-8', newline='\n')       # read mode
    fin_b = open(filein, mode='rb')  # binary read mode
    fout = open(fileout, mode='w', encoding='utf-8', newline='\n')      # write mode
    fout_b = open(fileout, mode='wb')  # binary write mode
    c = fin.read()         # read in file into c as a str
    length_c = len(c)

    if mode == 'e':
        out_str=''
        for i in range(0, length_c):
            current_cha = c[i]
            current_cha_ord = ord(current_cha)
            encrypted_ord = current_cha_ord + key
            encrypted_char = chr(encrypted_ord)
            out_str = out_str+encrypted_char
        fout.write(out_str)

    if mode == 'd':
        out_str=''
        for i in range(0, length_c):
            current_cha = c[i]
            current_cha_ord = ord(current_cha)
            encrypted_ord = current_cha_ord - key
            encrypted_char = chr(encrypted_ord)
            out_str = out_str+encrypted_char
        fout.write(out_str)

    # and write to fileout

    # close all file streams
    fin.close()
    fin_b.close()
    fout.close()
    fout_b.close()

    # PROTIP: pythonic way
    with open(filein, mode="r", encoding='utf-8', newline='\n') as fin:
        text = fin.read()
        # do stuff

        # file will be closed automatically when interpreter reaches end of the block


# our main function
if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein',help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k', dest='key', help='key', type = int)
    parser.add_argument('-m', dest='mode', help='mode', choices=['e','d'])

    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout
    key=args.key
    mode=args.mode

    doStuff(filein,fileout,key,mode)

    # all done


