#!/usr/bin/python3
"""reads text file and prints output to stdout"""

def read_file(filename = ""):
    """prints utf-8 files to stdout"""
    with open(filename, encoding = 'utf-8') as f:
        print(f.read(), end = "")
