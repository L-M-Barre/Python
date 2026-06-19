# StuID: K2370658
# Dataset: eels_chromosomes_1-6.vcf.gz
# Description: calculating and plotting the heterozygosity of american, european and hybrid eels
# using (% heterozygous = # hetero sites / total # sites x 100) and bar charts on Matplotlib


#---IMPORTING PACKAGES --- ----------------------------------------------#


# Importing matplotlib and scikit.allel packages so that they can be used within the code


import matplotlib.pyplot as plt
import allel as al


# --- START--- ----------------------------------------------#
# Introductory message and dictionary options
print("Welcome back User. This program creates a bar chart on the heterozygosity of eels in three different countries ")
print("Please choose one of the countries below for further information:")
print("type esc to exit at any time.")
print("a: Iceland, b: France, c: Cuba")
print("d: Compile all three countries onto one graph")
print("") # Space for presentation


# --- DICTIONARIES --- ----------------------------------------------#


# Linking user input to country info
countries = {
    "a" : "Iceland",
    "b" : "France",
    "c" : "Cuba",
    "d" : "Compiled",
}


# Linking sample names to countries
sample_countries = {
    "Gir_01" : "France", # Gir = euro eels (France)
    "Gir_02" : "France",
    "Gir_03" : "France",
    "Gir_04" : "France",
    "Aro_01" : "Cuba", # Aro = american eels (Cuba)
    "Aro_02" : "Cuba",
    "Aro_03" : "Cuba",
    "Aro_04" : "Cuba",
    "Vog_01" : "Iceland", # Vog = Hybrid euro/americ eels (Iceland)
    "Vog_02" : "Iceland",
    "Vog_03" : "Iceland",
    "Vog_04" : "Iceland",
}


# --- LOADING SAMPLE NAMES --- ----------------------------------------------#
import time
print("Retriving VCF data. . .") # Added due to slight slowness when accessing data
time.sleep(0.5)
callset = al.read_vcf("eels_chromosomes_1-6.vcf.gz", fields=['samples']) # Reads file to determine which samples are there
samples = callset['samples']


# --- HELPER FUNCTIONS --- -----------------------------------------------#
def country_indices(samples, sample_countries, country):
    # Enumerate pairs up values and indices by country by looping through lists in the vcf file.
    return [i for i, name in enumerate(samples) if sample_countries[name] == country]


def percent_hetero(het_array, sample_indi): # A dictionary of sample_index
    results = {}
    for i in sample_indi:
            sample_het = het_array[:, i]
            percent = (sample_het.sum() / sample_het.size)*100 # % heterozygous = # hetero sites / total # sites x 100
            results[i] = percent


    return results # sends result of function back to callset
   


# --- PLOTTING HETEROZYGOSITY --- ----------------------------------------------#
def plot_hetero(results, country_name):
    sample_indi = list(results.keys())
    hetero_val = list(results.values())


    # plt stands for plot. plots bar chart based off what country was selected.
    plt.bar(sample_indi, hetero_val, color='pink')
    plt.xlabel("Sample")
    plt.ylabel("Percent heterozygous alleles")
    plt.title(f"Heterozygosity for {country_name}")
    plt.ylim(0, max(hetero_val)*1.2) # headroom for Cuba plot
    plt.grid(axis='y', alpha=0.3)
    plt.tight_layout()
    plt.show()


#--- USER INPUT --- ----------------------------------------------#
program_running = True # Prevents continuity issues, where program wouldnt end
while program_running:
    chosen_country = input("Please enter a, b, c, or d here: ")


# If user types esc, ends code. works at any time
    if chosen_country.lower() == "esc":
        print("Thank you for using this service! Have a good day!")
        break


#--- SINGLE BAR CHARTS (a, b, c) --- ----------------------------------------------#
    if chosen_country in ["a", "b","c"]:
        country_name = countries[chosen_country]
        print("You selected:", country_name)


# Locating genotype data
        import time
        print("Loading genotype data, please wait. . .") # in case of slowness whilst graph is being made
        time.sleep(0.5)


        # Extracts raw genotype calls within vcf file, scikit-allele then converts it into Genotype array for analysis
        # gt: genotype field
        callset = al.read_vcf("eels_chromosomes_1-6.vcf.gz", fields=['calldata/GT'])
        gt = al.GenotypeArray(callset['calldata/GT'])
        print("Genotype data loaded.")


# Calculating heterozygosity
        het = gt.is_het()
# Retriving sample indices
        indi = country_indices(samples, sample_countries, country_name)
# Calc % hetero
        het_val = percent_hetero(het, indi)


        # Print's the percentage hetero's for all 12 samples
        print("Heterozygosity percentages for:", country_name)
        for idx, pct in het_val.items():
            print(f"Sample {idx}: {pct:.2f}%") # idx: sample idex (0, 1, 2..), pct: heterozygosity %, :.2f formats as float with 2 decimal places


# Plot results
        plot_hetero(het_val, country_name)


#--- COMBINED BAR CHART (d) --- ----------------------------------------------#
    elif chosen_country == "d":
        print("Compiling all countries. . .")


        import time
        print("Loading genotype data, please wait. . .") # In case of slowness whilst graph is being made
        time.sleep(0.5)


        # Retrieving data from vcf file
        callset = al.read_vcf("eels_chromosomes_1-6.vcf.gz", fields=['calldata/GT'])
        gt = al.GenotypeArray(callset['calldata/GT'])
        print("Genotype data loaded.")
        het = gt.is_het() # determines whether the sample its looking at is heterozygous (true)(0/1 1/0) or homozygous (false)


        # Retrieving hetero for each country and storing them in a dictionary
        groups = {
            "Iceland" : country_indices(samples, sample_countries, "Iceland"),
            "Cuba" : country_indices(samples, sample_countries, "Cuba"),
            "France" : country_indices(samples, sample_countries, "France")
        }


        # Calculating hetero values
        het_values = {country: percent_hetero(het, indi) for country, indi in groups.items()}


        # Grouping bar charts
        fig, ax = plt.subplots(figsize=(10,6))


        countries_list = list(het_values.keys())
        x_positions = range(len(groups["Iceland"])) # Iceland used as an example for how many samples there should be (4 samples)


        bar_width = 0.25


        # Enumerate function
        for i, country in enumerate(countries_list):
            vals = list(het_values[country].values())
            ax.bar(
                [x + i * bar_width for x in x_positions],
                vals,
                width=bar_width,
                label=country
            )


        # Creating the chart, adding labels and title
        ax.set_xlabel("Sample Index")
        ax.set_ylabel("Percent Heterozygous Alleles")
        ax.set_title("Heterozygosity in Eels Across France, Cuba and Iceland")
        ax.set_xticks([]) # Leaves x axis labels blank due to three different samples being present (Aro, Gir and Vog)
        ax.legend()
        ax.grid(axis='y', alpha=0.3)


        plt.tight_layout()
        plt.show()
        continue


    else: # 1st user input, if input is wrong (part of main while loop)
        print("Invalid input, please enter a, b, c or d here: ")
