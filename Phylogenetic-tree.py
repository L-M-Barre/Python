import os
print("Working directory:", os.getcwd())


import Bio as Bio
from Bio import SeqIO
from Bio import AlignIO
from Bio import Phylo
import matplotlib.pyplot as plt
import subprocess

Genomes = [
    "Root_genome_NC_001643_1.fasta", #chimpanzee root genome
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
    "Root_genome_NC_001643_1.fasta": "Chimpanzee_Haplogroup", 
    "Genome_1_AGENOME_ZPMS_T2b_1.fasta": "Unknown_Haplotype_1", #tbc
    "Genome_2_AGENOME_ZPMS_T1a_2.fasta": "Unknown_Haplotype_2", #tbc
    "Genome_3_AGENOME_ZPMS_HV2a_13.fasta": "Unknown_Haplotype_3", #tbc
    "Genome_4_MW389270_1.fasta": "Genome_4_Haplogroup_H", 
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

mito_data = []

for g in Genomes:
    for record in SeqIO.parse(g, "fasta"):
        record.id = label_map[g]
        record.name = label_map[g]
        record.description = ""
        mito_data.append(record)

#---PHYLOGENETIC TREE----------------------------------------------------------------------------------------------------------------#

tree = Phylo.read("Genomes.aln.treefile", "newick")

#Removing root sequence due to uneven branch lengths
tree.prune("Chimpanzee")

Phylo.draw(tree, do_show=False, branch_labels=label_map)
Phylo.draw(tree) # this draw works, removing = no graph
plt.gca().set_aspect('equal')
plt.show