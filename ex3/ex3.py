import sys
import argparse
import string
import re
import binascii
import struct
import ex2

for i in range(256):
    ex2.doStuff(filein="flag", fileout="ex3/flag_d" + str(i), key=i, mode="d3")