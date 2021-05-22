import os
import csv

# Path to collect data from the Resources folder
wrestling_csv = os.path.join("..", "Resources", "WWE-Data-2016.csv")
with open(wrestling_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

# Define the function and have it accept the 'wrestler_data' as its sole parameter
    # Prompt the user for what wrestler they would like to search for
    name_to_check = input("What wrestler do you want to look for? ")

    # Loop through the data
    for row in csvreader:

        # If the wrestler's name in a row is equal to that which the user input, run the 'print_percentages()' function
        if(name_to_check == row[0]):
            wins = int(row[1])
            losses = int(row[2])
            draws = int(row[3])

            # Find the total number of matches wrestled
            total = wins+losses+draws

            print(total)
            # Find the percentage of matches won
            print("wins %" + str(wins/int(total)*100))
            print("losses %" + str(losses/int(total)*100))
            print("draws %" + str(draws/int(total)*100))


# Find the percentage of matches lost

# Find the percentage of matches drawn

# Print out the wrestler's name and their percentage stats

# Read in the CSV file




