#------------------------------------------------------------------------------------------------------------------------#
#  IMPORTING PACKAGES
#------------------------------------------------------------------------------------------------------------------------#

import os
import Bio as Bio
from Bio import SeqIO, AlignIO, Phylo
import matplotlib.pyplot as plt
import subprocess

print("Working directory:", os.getcwd())

#------------------------------------------------------------------------------------------------------------------------#
#  INPUT FILE LIST & LABELS
#------------------------------------------------------------------------------------------------------------------------#
Genomes = [
    "Genome_1_AGENOME_ZPMS_T2b_1.fasta", #tbc
    "Genome_2_AGENOME_ZPMS_T1a_2.fasta", #tbc
    "Genome_3_AGENOME_ZPMS_HV2a_13.fasta", #tbc
    "Genome_4_MW389270_1.fasta", # H HaploG
    "Genome_5_MW389262_1.fasta", # H HaploG
    "Genome_6_PV559576_1.fasta", # L0 HaploG
    "Genome_7_PV560091_1.fasta", # L3 HaploG
    "Genome_8_KY496882_1.fasta", # J HaploG
    "Genome_9_KY496873_1.fasta", # J HaploG
    "Genome_10_MH553725_1.fasta", # M HaploG
    "Genome_11_MN894796_1.fasta", # M HaploG
    "Genome_12_PV559641_1.fasta", # N HaploG
    "Genome_13_PV560139_1.fasta", # N HaploG
    "Genome_14_JN657206_1.fasta", # K HaploG
    "Genome_15_KX467262_1.fasta" # K HaploG 

]

label_map = {
    "Genome_1_AGENOME_ZPMS_T2b_1.fasta": "Unknown_Haplogroup_1", #Unknown haplogroup 1
    "Genome_2_AGENOME_ZPMS_T1a_2.fasta": "Unknown_Haplogroup_2", #Unknown haplogroup 2
    "Genome_3_AGENOME_ZPMS_HV2a_13.fasta": "Unknown_Haplogroup_3", #Unknown haplogroup 3
    "Genome_4_MW389270_1.fasta": "Genome_4_Haplogroup_H", #Genome_4_Haplogroup_H
    "Genome_5_MW389262_1.fasta": "Genome_5_Haplogroup_H", 
    "Genome_6_PV559576_1.fasta": "Genome_6_Haplogroup_L0", 
    "Genome_7_PV560091_1.fasta": "Genome_7_Haplogroup_L3", 
    "Genome_8_KY496882_1.fasta": "Genome_8_Haplogroup_J", 
    "Genome_9_KY496873_1.fasta": "Genome_9_Haplogroup_J", 
    "Genome_10_MH553725_1.fasta": "Genome_10_Haplogroup_M", 
    "Genome_11_MN894796_1.fasta": "Genome_11_Haplogroup_M", 
    "Genome_12_PV559641_1.fasta": "Genome_12_Haplogroup_N", 
    "Genome_13_PV560139_1.fasta": "Genome_13_Haplogroup_N", 
    "Genome_14_JN657206_1.fasta": "Genome_14_Haplogroup_K", 
    "Genome_15_KX467262_1.fasta": "Genome_15_Haplogroup_K"  
}

#------------------------------------------------------------------------------------------------------------------------#
#  SEQUENCE RENAMING AND LOADING
#------------------------------------------------------------------------------------------------------------------------#

mito_data = []

for g in Genomes:
    for record in SeqIO.parse(g, "fasta"):
        record.id = label_map[g]
        record.name = label_map[g]
        record.description = ""
        mito_data.append(record)

print("Number of sequences loaded:", len(mito_data))

#------------------------------------------------------------------------------------------------------------------------#
#  WRITE & COMBINE DATA 
#------------------------------------------------------------------------------------------------------------------------#

SeqIO.write(mito_data, "all_genomes.fasta", "fasta") # place all sequences info a new fasta file

#------------------------------------------------------------------------------------------------------------------------#
#  MAFFT ALIGNMENT 
#------------------------------------------------------------------------------------------------------------------------#

# Run MAFFT
with open ("Genomes.aln", "w") as outfile:
    subprocess.run([
        "mafft",
        "--auto", 
        "all_genomes.fasta"
   
], stdout=outfile)  # this creates 'Genomes.aln' genome alignments
    
print("Alignment complete.")

#------------------------------------------------------------------------------------------------------------------------#
#  IQTREE
#------------------------------------------------------------------------------------------------------------------------#

#run IQtree
result = subprocess.run([
    "iqtree2",
    "-s", "Genomes.aln",
    "-m", "MFP",
    "-nt", "AUTO"
], capture_output=True, text=True) 

print(result.stdout)
print(result.stderr)

# checking where tf this treefile is
if not os.path.exists("Genomes.aln.treefile"):
    raise FileNotFoundError("IQtree is a pos and wont produce what you want. check log above")

# read alignments
alignment = AlignIO.read("Genomes.aln", "fasta")

print(type(alignment))
for record in alignment:
    print(record.id, len(record.seq))

print("IQtree completed")

#------------------------------------------------------------------------------------------------------------------------#
#  LOAD TREE
#------------------------------------------------------------------------------------------------------------------------#

tree = Phylo.read("Genomes.aln.treefile", "newick")

#------------------------------------------------------------------------------------------------------------------------#
#  PRUNING CHIMP BRANCH
#------------------------------------------------------------------------------------------------------------------------#
# due to IQtree file issues, (deletion of .treefile resulting in IQtree refusing to create a new one)
# chimp dataset stored previously on all_genomes.fasta will be pruned from final tree.

for clade in tree.get_terminals():
    if "Chimpanzee" in clade.name or "Chimp" in clade.name:
        tree.prune(clade)
        print("Pruned leftover Chimp branch", clade.name)

#------------------------------------------------------------------------------------------------------------------------#
#  BRANCH COLOURS AND CLADE GROUPS
#------------------------------------------------------------------------------------------------------------------------#

Haplogroup_colours = {
    "L0": "orange", # Deep african
    "L3": "brown", # African Ancestors of M/N
     "M": "olive", # out of Africa founders
    "N": "green", # out of Africa founders
    "H": "magenta", # West Eurasian
    "J": "salmon", # West Eurasian
    "K": "deeppink", # West Eurasian
    "Unknown": "blue",

}

def get_haplogroup(label):
    if label is None:
        return "Unknown"
    
    # Extract last underscore group
    parts = label.split("_")
    last = parts[-1]

    if last in Haplogroup_colours:
        return last
        
    return "Unknown"

label_colours = {
    clade.name: Haplogroup_colours[get_haplogroup(clade.name)]
    for clade in tree.get_terminals()
}

#------------------------------------------------------------------------------------------------------------------------#
#  DRAW TREE
#------------------------------------------------------------------------------------------------------------------------#

Phylo.draw(tree, label_colors=label_colours)
plt.gca().set_aspect('equal')
