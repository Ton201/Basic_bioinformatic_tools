#! /usr/bin/env python

from pathlib import Path
import subprocess

# Creates subdirectory for results
Path('data_analysed').mkdir(exist_ok=True)

# Declaires input and output paths variables
p_in = Path() / 'fastq' # function Path() returns current directory (".")
p_out = Path() / 'data_analysed'


# Runs fastqc for each file in input directory
for file in p_in.iterdir():
	command = ['fastqc','-o',p_out, file]
	subprocess.run(command, check=True)
