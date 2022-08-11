# Add our dependencies
# Import the datetime class from the datetime module with an alias.
import datetime as dt

# Import the csv and os modules

import csv
import os
from tarfile import ReadError

# Use the now() attribute on the datetime classs to retrieve the current time

now = dt.datetime.now()

# Print the current time.

print(f"The current time is {now}!")
print("")


# file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable for the import filehandle
file_to_load = 'C:/Users/azinc/Github/Election_Analysis/Resources/election_results.csv'
# print(file_to_load)

# Assign a variable for the output filehandle
file_to_save = 'C:/Users/azinc/Github/Election_Analysis/Analysis/election_analysis.txt'


# Open a csv file
# election_data = open(file_to_load,'r')
    
print("")

with open(file_to_load) as election_data:
    # to do - perform analysis - print each row in the CSV file
    file_reader = csv.reader(election_data)
    # print the Header row
    headers = next(file_reader)
    print(headers)
    
    # for row in csv.reader(election_data):
    #     print(row[0])
    


with open(file_to_save, "w") as outfile:
    outfile.write("Counties in the Election\n-------------------------------------\nArapahoe\nDenver\nJefferson")









# Close the csv file
# election_data.close()


#The data we need to retrieve.
# 1. The total number of votes cast
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won.
# 5. The winner of the election based on popular vote.

