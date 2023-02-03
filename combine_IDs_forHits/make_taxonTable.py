"""
Let's make a taxon table for the dsrAB reference sequences/OTUs to be input for a phyloseq object
for the reference tree!
"""
import csv

from Bio import SeqIO
import re
import pandas as pd

# read in reference sequence fasta file
ref_seq_file = "dsrAB_referenceSequences_fromSupp.fasta"
f = open(ref_seq_file, 'r')

# make taxa table
taxa_table = pd.DataFrame(columns=["OTU",
                                   "environmental_category",
                                   "dsrab_type",
                                   "supercluster",
                                   "level1_taxon",
                                   "level2_taxon",
                                   "level3_taxon"])

# parse out info!
for record in SeqIO.parse(f, "fasta"):
    description = record.description.split("\t")

    OTU = re.sub(" ", "_", description[1]) + "__" + description[0]

    taxonomy = description[4].split(";")

    # add row to taxa table
    otu_dict = {"OTU": OTU,
                "environmental_category": description[3],
                "dsrab_type": taxonomy[0],
                "supercluster": taxonomy[1],
                "level1_taxon": taxonomy[2],
                "level2_taxon": taxonomy[3],
                "level3_taxon": taxonomy[4]}

    taxa_table = taxa_table.append(otu_dict, ignore_index=True)

# write output taxa table file to csv
pd.DataFrame(taxa_table).to_csv("taxa_table.csv")

# make taxa table for only OTUs in the reference tree?
