from Bio.Seq import Seq
from Bio import SeqIO
from Bio.Seq import transcribe
from Bio.Seq import translate
from Bio import SeqFeature
import re
#my_list = []
#with open("sequence.gb", mode="rt") as r:
 #   reader = r.read()
for rec in SeqIO.parse("sequence.gb", "genbank"):
    if rec.features:
        for feature in rec.features:
            if (feature.type != "CDS"):
                mrna = Seq.transcribe(rec)
                my_list = [mrna]
                if (len(my_list) < 200):
                    print (str(my_list))
                    print (feature.location)
                    print (feature.location.extract(rec).seq)
                    #print (feature)
                    
                    #print (Seq(my_list))
                 #   print (my_list)
