#!/usr/bin/env python3
# SUTD 50.020 Security Lab 1
# Simple file read in/out
# Quyen, 2014

# Import libraries
import sys
import argparse
import string
import re
import binascii
import struct

def doStuff(filein,fileout,key,mode):
    # open file handles to both files
    len_printable = len(string.printable)
    if key<1 or key>len_printable-1:
        if mode!='d3':
            print("Please input valid key value (-1<k<1)")
            return

    fin  = open(filein, mode='r', encoding='utf-8', newline='\n')       # read mode
    fin_b = open(filein, mode='rb')  # binary read mode
    fout = open(fileout, mode='w', encoding='utf-8', newline='\n')      # write mode
    fout_b = open(fileout, mode='wb')  # binary write mode
    fout_b_png = open(fileout+'.png', mode='wb')
    if mode == 'e':
        all_bytes = fin_b.read()  # read in file into c as a str
        b_length = len(all_bytes)
        out_byte_arr = bytearray()
        for byte in all_bytes:
            byte = (byte+key)%256
            out_byte_arr.append(byte)
        fout_b.write(out_byte_arr)
    if mode == 'd':
        all_bytes = fin_b.read()  # read in file into c as a str
        b_length = len(all_bytes)
        out_byte_arr = bytearray()
        for byte in all_bytes:
            byte = (byte - key) % 256
            out_byte_arr.append(byte)
        fout_b.write(out_byte_arr)

    if mode == 'd3':
        all_bytes = fin_b.read()  # read in file into c as a str
        b_length = len(all_bytes)
        out_byte_arr = bytearray()
        for byte in all_bytes:
            byte = (byte - key) % 256
            out_byte_arr.append(byte)
        fout_b_png.write(out_byte_arr)

    # and write to fileout

    # close all file streams
    fin.close()
    fin_b.close()
    fout.close()
    fout_b.close()

    # PROTIP: pythonic way
    #with open(filein, mode="r", encoding='utf-8', newline='\n') as fin:
       # text = fin.read()
        # do stuff

        # file will be closed automatically when interpreter reaches end of the block


# our main function
if __name__=="__main__":
    # set up the argument parser
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', dest='filein',help='input file')
    parser.add_argument('-o', dest='fileout', help='output file')
    parser.add_argument('-k', dest='key', help='key', type = int, choices=range(0,256))
    parser.add_argument('-m', dest='mode', help='mode', choices=['e','d','d3'])

    # parse our arguments
    args = parser.parse_args()
    filein=args.filein
    fileout=args.fileout
    key=args.key
    mode=args.mode

    doStuff(filein,fileout,key,mode)

    # all done


