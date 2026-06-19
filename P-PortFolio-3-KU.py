# StuID: K2370658
# Dataset: Fertility rates over time: children-born-per-woman.csv
# Description: select a country and graph type to plot a line plot, scatter plot, histogram or box plot using matplotlib


#--IMPORTING PACKAGES----------------------------------------------------------------------------------------------------#


# Importing the CSV file and matplotlib so that they can be used within the code
import csv
import matplotlib.pyplot as plt


#---START----------------------------------------------------------------------------------------------------------------#
# Introductory message and dictionary options
print("Welcome back User. The current information available on this program consists of the fertility rates of children born per woman between 1950 and 2023")
print("Please choose a number linked to the six countries below for further information:")
print("type esc to exit at any time.")
print("1: China, 2: Ecuador, 3: India, 4: Japan, 5: United Kingdom, 6: Zimbabwe")
print("") # Space for presentation


# Fertility rates over time of Number of children born per woman between 1950 and 2023


# Dictionary linking number to countries (used to link user input to a country)
countries = {
    "1" : "China",
    "2" : "Ecuador",
    "3" : "India",
    "4" : "Japan",
    "5" : "United Kingdom",
    "6" : "Zimbabwe",
}


# Reading CSV file so that user can choose data related to chosen country and storing information
Fertility_rates = {}
years = []


#---READING CSV FILE-----------------------------------------------------------------------------------------------------#
# Link user input to country chosen via storing csv info, organised by country in 'data' and then find all keys/values asssociated with that country
# (this is used so that the correct information is used for the graphs later on)
data = []
with open("children-born-per-woman.csv") as f:
    reader = csv.DictReader(f)
    for row in reader:
        # Creates a new dictionary (clean_rows) to store csv info, k is for keys ('Year, Entity' in csv file) and v is for values (eg 5.04)
        clean_rows = {k.strip(): v for k, v in row.items()}
        data.append(clean_rows) # Creates one dictionary per row and stores in the data list (line 37)


# Asking user to enter value linked to country number, while loop used to continue asking for viable number
program_running = True # prevents continuity issues after line 158, where program wouldnt end
while program_running:
    chosen_country = input("Please enter number here: ")


# If user types esc, ends code. works at any time
    if chosen_country.lower() == "esc":
        print("Thank you for using this service! Have a good day!")
        break


#---CONVERTING CSV DATA INTO FLOAT/INTEGERS------------------------------------------------------------------------------#
# Plotting info associated with chosen country
    if chosen_country in countries:
        plot_country = countries[chosen_country]


        # Filtering rows for chosen country
        years = []
        F_rates = []
        for row in data:
            if row["Entity"] == plot_country: # if chosen country matches names in column 'entity' plot those rows
                years.append(int(row["Year"]))
                F_rates.append(float(row["FertilityRate"]))


#---CREATING THE GRAPHS--------------------------------------------------------------------------------------------------#
# Creating a scatter chart for the chosen country
# Bar charts are not viable, since there is 70+ years of data, the bars are too small
        print(f"Here is a scatter plot for {plot_country}")
        plt.scatter(years, F_rates, label=plot_country, color="pink", s=20) # s = 20 is the size of the markers


# Labeling each axis, graph title, and legend
        plt.xlabel("Year")
        plt.ylabel("Births per woman")
        plt.title(f"Fertility rates over time for {plot_country}")
        plt.legend()
        plt.grid(True, alpha=0.3) # Sets the opacity of the gridlines in the background of the graph
        plt.tight_layout()
        plt.show() # 'prints' the graph
       
        while True: # While loop used to ask user choice after each action once first graph is created
            other_country = input(f"You are currently viewing {plot_country}. Would you like to choose another country (1)? change plot type/combine all countries (2)? or end program (esc)?")
            if other_country == "1": # Loop back to line 49
                break
       
            elif other_country =="2": # Giving user options to create which plot best suits their need
                print("Other plot types for this graph are available. Please choose from the following:")
                print("1: Line plot, 2: Histogram, 3: Box plot 4: Combine country data into one plot")
                graph_type = input("please type one of the following numbers here: ")
                plt.clf() # This function clears the previous plot


                if graph_type == "1": # Line plot (same logic for scatter plot applies to all of these, axis names, graph titles, legend etc)
                    plt.plot(years, F_rates, label=plot_country, linewidth=2)
                    plt.xlabel("Year")
                    plt.ylabel("Births per woman")
                    plt.title(f"Fertility rates over time for {plot_country}")
                    plt.legend()
                    plt.grid(True, alpha=0.3)
                    plt.tight_layout()
                    plt.show()


                elif graph_type == "2": # Histogram
                    plt.hist(F_rates, bins=10, color="purple", edgecolor="black")
                    plt.xlabel("Births per woman")
                    plt.ylabel("Frequency (Years)")
                    plt.title(f"Fertility rates over time for {plot_country}")
                    plt.grid(True, alpha=0.3)
                    plt.tight_layout()
                    plt.show()


                elif graph_type == "3": # Box plot
                    plt.boxplot(F_rates)
                    plt.ylabel("Births per woman")
                    plt.title(f"Fertility rates over time for {plot_country}")
                    plt.grid(True, alpha=0.3)
                    plt.tight_layout()
                    plt.show()
               
                elif graph_type == "4": # Comibining all country data into one line plot
                    plt.clf() # Clear previous plot (prevents all the plots being made on top of each other)


                    colors = ["pink", "purple", "orange", "blue", "green", "brown"] # Identifying a colour for each country


                    for (cid, cname), color in zip(countries.items(), colors): # Loop through all the countries in the dictionary and plot each
                        years_all, rates_all = [], []
                        for row in data:
                            if row["Entity"] == cname: # 'c' means country name, country id etc...
                                years_all.append(int(row["Year"]))
                                rates_all.append(float(row["FertilityRate"]))
                        # Plotting a line for each country
                        plt.plot(years_all, rates_all, label=cname, color=color, linewidth=2)
                       
                    # Labels, title and legend
                    plt.xlabel("Year")
                    plt.ylabel("Births per woman")
                    plt.title("Fertility rates over time for six countries")
                    plt.legend()
                    plt.grid(True, alpha=0.3)
                    plt.tight_layout()
                    plt.show()


                else: # Default back to scatter plot
                    print("plotting original graph")
                    plt.scatter(years, F_rates, label=plot_country, color="pink", s=20)
                    plt.xlabel("Year")
                    plt.ylabel("Births per woman")
                    plt.title(f"Fertility rates over time for {plot_country}")
                    plt.legend()
                    plt.grid(True, alpha=0.3)
                    plt.tight_layout()
                    plt.show()


            elif other_country.lower() == "esc":
                print("Thank you for using this service! Have a good day!")
                program_running = False
                break
           
            else: # Links back to line 49
                print("invalid choice, returning to the start.")
                break
       
    else: # Links back to line 49 with invalid input
        print("Invalid number, Please try again.")
        continue


#---END------------------------------------------------------------------------------------------------------------------#

