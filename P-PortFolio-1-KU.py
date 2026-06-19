#Task 1: Store and print the numbers of chromosomes for various organisms
#Your task is to write and submit a python program which does the following:
#Store the information from the following table in lists and dictionaries/
#Ask the user to pick an organism, and print how many autosomes, sex chromosomes and total chromosomes each organism has.
#If the user enters an organism that is not included, Your program should print a message stating that the organism is not in the dataset.




#total number of chromosomes = (autosomes + sex chromosomes)* ploidy level




#---------------------------------------------------------------------------------------------------------------------------


# Introductory message and dictionary options
print("Welcome back User. Please choose a numerical option from the following list for further information:")
print("type esc to exit at any time.")
print("1: Human, 2: Grey Heron, 3: African clawed frog, 4: Strawberry, 5: Platypus.") # 'org list'


# Chromosome (chromo) data for each organism (org)
Human = ["Species: Homo sapiens", "Autosomes = 22", "Sex chromosomes = 1", "Diploid level = 2"]
Grey_heron = ["Species: Ardea cinerea", "Autosomes = 31", "Sex chromosomes = 1", "Diploid level = 2"]
African_clawed_frog = ["Species: Xenopus laevis", "Autosomes = 16", "Sex chromosomes = 2", "Diploid level = 2"]
Strawberry = ["Species: Fragaria x ananassa","Autosomes = 7", "Sex chromosomes = 0", "Diploid level = 8"]
Platypus = ["Species: Ornithorhynchus anatinus","Autosomes = 21", "Sex chromosomes = 5", "Diploid level = 2"]


# Dictionary linking number to org (used to link user input to an org)
organisms = {
    "1" : "Human",
    "2" : "Grey_heron",
    "3" : "African_clawed_frog",
    "4" : "Strawberry",
    "5" : "Platypus",
}


# Dictionary linking org to chromo information (used to link user choice of org, to org information)
org_data = {
    "Human": Human,
    "Grey_heron": Grey_heron,
    "African_clawed_frog": African_clawed_frog,
    "Strawberry": Strawberry,
    "Platypus": Platypus,
}


# Dictionary linking chromo information to numerical value (used to calculate total chromo # when prompted (line 75))
chromo_data = {
"Human" : [22, 1, 2],
"Grey_heron" : [31, 1, 2],
"African_clawed_frog" : [16, 2, 2],
"Strawberry" : [7, 0, 8],
"Platypus" : [21, 5, 2],
}


# Ask user to enter value, main loop used to return back to original 'org list' (line 14)
while True:
    org = input("Please enter number here: ")


# Checking if user wants to exit the dictionary (can be used at any time)
    if org.lower() == "esc":
        print("Thank you for using our service. Have a good day!")
        break


# Determine whether value is in dictionary and print information
# Linking variables to each other (for clarity)(lines 62-64)
    if org in organisms:
        selected = organisms[org]
        display_list = org_data[selected]
        calc_list = chromo_data[selected]


        print(f"\nYou selected: {selected.replace('_', ' ')}")
        print("Organism information: ")
        for item in display_list:
            print(f"{item}")


# chromo_data dictionary used to calculate total chromosome number through prompt (Y/N)(line 42-47)
# 0 = autosome, 1 = sex chromo, 2 = diploid lvl (index positions, act the same way lists for retrieval, whilst in a dictionary)


        chromo = input("See total chromosome count for this organism? Y/N: ")
        if chromo.lower() == "y":
            total = (calc_list[0] + calc_list[1]) * calc_list[2]
            print(f"Total chromosome count: {total}")
            continue
   
# if user input is 'n' automatically return to org list
        elif chromo.lower() == "n":
            print("returning to start. . .")
        else:
            print("Invalid option, please state Y/N: ")


# If value not in dictionary, ask if user wants to return to the start or end service
    else:
        restart = input("Organism not found. Would you like to return to the start? Y/N: ")
        if restart.lower() == "y":
       	    continue
        if restart.lower() != "y":
       	    print("Thank you for using our service. Have a good day!")
            break  



