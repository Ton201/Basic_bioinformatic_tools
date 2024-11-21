#! usr/bin/env python

import sys
import subprocess

ids =[]

id_file = sys.argv[1]
with open(id_file,'r') as f:
    for line in f:
       ids.append(line.strip('\n'))

for id in ids:
    print(f'Downoading seq: {id}')
    command = ['fastq-dump','--split-files', id]   
    try:
        subprocess.run(command, check=True)
        print(f"Successfully downloaded {id}")
    except subprocess.CalledProcessError as e:
        print(f"Failed to download {id}: {e}")
