from Bio import SeqIO

for rec in SeqIO.parse("AL123456.3.fasta", "fasta"):
    if rec.features:
        for feature in rec.features:
            if feature.type == "CDS":
                print (feature.location)
                print (feature.qualifiers["protein_id"])
                print (feature.location.extract(rec).seq)
