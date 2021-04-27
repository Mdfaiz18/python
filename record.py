from Bio.Seq import Seq
from Bio import SeqIO
#record = SeqIO.read("AL123456.3.fasta","fasta")
#print(str(record.seq))
my_list = []
with open("AL123456.3.fasta",mode="rt") as bla:
    reader = bla.read()
    my_list = reader.split("//\n")
    dna= str(my_list)
    mrna = dna.transcribe()
    print (mrna)
