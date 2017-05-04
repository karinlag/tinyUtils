import sys
import os
from Bio import SeqIO

name = sys.argv[1]
seqfile = sys.argv[2]

dirname = os.path.dirname(seqfile)


for record in SeqIO.parse(seqfile, "fasta"):
    if name in record.description:
        record.id = dirname + "_" + record.id
        SeqIO.write(record, sys.stdout, 'fasta')


        

