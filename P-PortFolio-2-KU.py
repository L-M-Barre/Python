# Introductory message and dictionary options
print("Welcome back User. Please choose a numerical option from the three sequences below for further information:")
print("type esc to exit at any time.")
print("below are the three sequences available:")
print(" ") # Space for presentation


# Reading sequence file, removing the > before the sequence starts and printing information within
sequences = {}
with open("Python_task_2_sequences.fa", "r") as f:
    lines = f.readlines()
    label = ""
    for line in lines:
        line = line.strip()
        if line.startswith(">"):
            label = line[1:]
            sequences[label] = ""
        else:
            sequences[label] += line.upper()


# Formatting how the sequences are printed for better clarity
    print(lines[0:1])
    print(lines[1:2])
    print(" ")
    print(lines[2:3])
    print(lines[3:4])
    print(" ")
    print(lines[4:5])
    print(lines[5:6])
    print(" ")
    
#---START------------------------------------------------------------------------#
# Sequence list for user to choose from
print("Please choose from the following")
print("Sequence 1: 1, Sequence 2: 2, Sequence 3: 3")


# dictionary linking users number input to correct sequence
sequence = {
    "1" : "Sequence 1",
    "2" : "Sequence 2",
    "3" : "Sequence 3",
}


# Codon table provided in assignment (copy pasted)
# Full standard codon table (DNA codons → amino acids, 1-letter code)
standard_codon_table = {
    # Phenylalanine and Leucine
    "TTT": "F", "TTC": "F", "TTA": "L", "TTG": "L",
    # Leucine
    "CTT": "L", "CTC": "L", "CTA": "L", "CTG": "L",
    # Isoleucine and Methionine (start)
    "ATT": "I", "ATC": "I", "ATA": "I", "ATG": "M",
    # Valine
    "GTT": "V", "GTC": "V", "GTA": "V", "GTG": "V",
    # Serine
    "TCT": "S", "TCC": "S", "TCA": "S", "TCG": "S",
    # Proline
    "CCT": "P", "CCC": "P", "CCA": "P", "CCG": "P",
    # Threonine
    "ACT": "T", "ACC": "T", "ACA": "T", "ACG": "T",
    # Alanine
    "GCT": "A", "GCC": "A", "GCA": "A", "GCG": "A",
    # Tyrosine and Stop
    "TAT": "Y", "TAC": "Y", "TAA": "*", "TAG": "*",
    # Histidine and Glutamine
    "CAT": "H", "CAC": "H", "CAA": "Q", "CAG": "Q",
    # Asparagine and Lysine
    "AAT": "N", "AAC": "N", "AAA": "K", "AAG": "K",
    # Aspartic acid and Glutamic acid
    "GAT": "D", "GAC": "D", "GAA": "E", "GAG": "E",
    # Cysteine, Stop, Tryptophan
    "TGT": "C", "TGC": "C", "TGA": "*", "TGG": "W",
    # Arginine (TCN was Ser already)
    "CGT": "R", "CGC": "R", "CGA": "R", "CGG": "R",
    # Serine and Arginine
    "AGT": "S", "AGC": "S", "AGA": "R", "AGG": "R",
    # Glycine
    "GGT": "G", "GGC": "G", "GGA": "G", "GGG": "G"
}


# Asking user to enter value linked to sequence number, while loop used to continue asking for vable number
while True:
    seq = input("Please enter number here: ") # appears after line 57


# If user types esc, ends code. works at any time
    if seq.lower() == "esc":
        print("Thank you for using this service! Have a good day!")
        break


# Print the sequence chosen by user
# getting labels from FASTA file
    label = list(sequences.keys())


    if seq in sequence:
        print("Labels found:", label)
        print("User input:", seq)
        print("Trying to access index:", int(seq) - 1)


        #convert 1 to 0 index VV
        selected_label = label [int(seq) - 1]
        selected_seq = sequences[selected_label]
        print(f"\nYou selected: {selected_label}")
        print(f"\n{selected_seq}")
   
    elif seq not in sequence:
        wrong_seq = input("Sequence not found. Return to the start? Y/N: ")
        if wrong_seq.lower() == "y":
            continue
        else:
            print("Thank you for using our service. Have a good day!")
            break


# Identifying start and stop codons in each of the sequences
    Start_codon = ("ATG")
    stop_codon = {"TAA", "TGA", "TAG"}


# Asking user if they want codon information listed
    print(" ")# space for formatting
    print("Would you like to see codon locations and amino acid information for this sequence?")
    info = input("Y/N: ")
    if info.lower() == "y":
        print("Stop and start codon's will be highlighted by ***")


# Converts all DNA sequences in FASTA file used into upper case
        selected_sequence = selected_seq.upper()
        codon_positions = []


#---START/STOP CODON SECTION------------------------------------------------------------------------#
# Finding start codons
        start_index = selected_sequence.find(Start_codon)
        if start_index == -1:
            print("No start codon (ATG) found in this sequence. ")
        else:
            codon_positions.append((start_index, start_index + 3, "Start"))
            # scan in steps of 3
            stop_index = -1
            for i in range(start_index + 3, len(selected_sequence), 3):
                codon = selected_sequence[i:i+3]
                if codon in stop_codon:
                    stop_index = i
                    codon_positions.append((stop_index, stop_index + 3, "Stop"))
                    break


# Sorts the positions of start/stop codons, found using quickref.me/python cheat sheet in #Python Lists section
        codon_positions.sort(key=lambda x: x[0])


# highlighting the sections (with ***__***)
        highlighted_seq = selected_sequence
        for start, end, codon_type in reversed(codon_positions): #reversed goes through the codon_position list backwards
            highlighted_seq = (
                highlighted_seq[:start]
                +"***"
                + highlighted_seq[start:end]
                +"***"
                + highlighted_seq[end:]
            )
        print(f"\nHighlighted sequence: \n{highlighted_seq}\n")


# Print codon positions
        print("Codon positions: ")
        for start, end, codon_type in codon_positions:
            print(f"{codon_type.capitalize()} codon at position {start}: {selected_sequence[start:end]}")


#---AMINO ACID SECTION------------------------------------------------------------------------#
# List of all the hydrophobic/phillic/charged amino acids in standard_codon_table
        Hydrophobic = ("G", "A", "V", "L", "I", "M", "P", "F", "W")
        Hydrophillic = ("S", "T", "Y", "N", "Q", "C", "D", "E", "K", "H", "R")
        Charged_neg = ("D", "E")
        Charged_pos = ("K", "R", "H")


# Translating amino acid codons between start and stop codons
        if start_index != -1 and stop_index != -1:
            amino_acids = []
            AA_count = {}
            Hydrophobic_count = 0
            Hydrophillic_count = 0
            Charged_pos_count = 0
            Charged_neg_count = 0


            for i in range(start_index, stop_index, 3): # Counting the AA in sets of 3s
                codon = selected_sequence[i:i+3]
                AA = standard_codon_table.get(codon, "X") # X = unknown amino acids
                amino_acids.append(AA)


                AA_count[AA] = AA_count.get(AA, 0) + 1


        # Linking amino acids to their 'states'
                if AA in Hydrophillic:
                    Hydrophillic_count += 1
                elif AA in Hydrophobic:
                    Hydrophobic_count += 1
                if AA in Charged_pos:
                    Charged_pos_count += 1
                if AA in Charged_neg:
                    Charged_neg_count += 1
       
        # Printing AA chain
            print("\n Amino acid sequence: ")
            print(" ".join(amino_acids))


        # Printing AA counts (any repeat AA's)
            print("\n Amino acid counts:")
            for AA, count in sorted(AA_count.items()):
                print(f"{AA}: {count}")


        # Summary of AA section
            print("Amino acid list: ")
            print("Hydrophobic AAs:")
            print(Hydrophobic)
            print("Hydrophillic AAs:")
            print(Hydrophillic)
            print(" + Charged AAs:")
            print(Charged_pos)
            print(" - Charged AAs:")
            print(Charged_neg)
            print("\n Amino acid (AA's) characteristics: ")
            print(f" Hydrophobic AA's: {Hydrophobic_count}")
            print(f" Hydrophillic AA's: {Hydrophillic_count}")
            print(f" Positively charged AA's: {Charged_pos_count}")
            print(f" Negatively charged AA's: {Charged_neg_count}")


# End program if user does not want further information
    if info.lower() != "y":
        print("Thank you for using our service. Have a good day!")
        break


# if information for sequence not found, continue to start
    else:
        ("Start codon not found")
        continue    


