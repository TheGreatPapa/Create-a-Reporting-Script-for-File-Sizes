#!/usr/bin/python3

import os
import sqlite3 
import sys

from os.path import abspath, join, getsize

metadata = {}

# Get the command-line arguments
arguments = sys.argv

for root, dir, files in os.walk(arguments[1]):
    for _file in files:
        full_path = os.path.join(root, _file)
       
        size = os.path.getsize(full_path)
        metadata[full_path] = size
        #print(f"path: {full_path}\nsize: {size}")

counter = 0
for path, size in sorted(metadata.items(), key=lambda x:x[1], reverse=True):
    if counter>20:
        break
    print(f"path: {path}\nsize: {size}\n")
    counter+=1
