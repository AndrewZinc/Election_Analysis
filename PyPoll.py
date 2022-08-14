# Add our dependencies - Import the csv and os modules

import csv
import os

file_to_load = os.path.join('Resources', 'election_results.csv')
# Assign a variable for the import filehandle
#file_to_load = 'C:/Users/azinc/Github/Election_Analysis/Resources/election_results.csv'
print(file_to_load)

# Assign a variable for the output filehandle
file_to_save = 'C:/Users/azinc/Github/Election_Analysis/Analysis/election_analysis.txt'

# Open a csv file
election_data = open(file_to_load,'r')

# Declare and initialize the vote accumulator
total_votes = 0
# Declare a list of candidates
candidate_options = []
# Declare a dictionary for the candidate-votes
candidate_votes = {}

# Winning candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

# Open the election results and read the file

with open(file_to_load) as election_data:
    # Begin analysis of the CSV file
    
    file_reader = csv.reader(election_data)
    
    # Read and skip the Header row
    headers = next(file_reader)

    # Read each row of the CSV file
    for row in file_reader:
        # Count the vote for the row
        total_votes += 1
        
        # extract the candidate name from each row
        candidate_name = row[2]
        
        if candidate_name not in candidate_options:
            # Add the candidate name to the candidate list
             candidate_options.append(candidate_name)
             
             # Begin tracking the candidate's votes
             candidate_votes[candidate_name] =0
             
        # Add to the candidate's votes
        candidate_votes[candidate_name] +=1
        
# Prepare to write the election results to the output file
       
with open(file_to_save, "w") as outfile:

    election_results = (
        f"Election Results \n"
        f"-------------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------------\n")
    
    print(election_results, end="")
    
    # Save the final vote count to the output file
    outfile.write(election_results)
    
    
    # Determine the percentage of votes for each candidate
    # Examine each candidate   
    for candidate_name in candidate_options:
        # Retrieve their vote tally
        votes = candidate_votes[candidate_name]
        
        # compute the vote percentage
        vote_percent = float(votes) / float(total_votes) * 100
        
        # print the candidate name and vote percentage to the outfile and terminal
        candidate_results = (f"{candidate_name}: {vote_percent:.1f}% ({votes:,})\n")
        outfile.write(candidate_results)
        print(candidate_results)
                
        # Determine election winner
        if (votes > winning_count) and (vote_percent > winning_percentage):
            winning_candidate = candidate_name
            winning_count = votes
            winning_percentage = vote_percent
        
    winning_candidate_summary = (
        f"-------------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------------\n")

    # print the winning candidate summary to the outfile and terminal
    outfile.write(winning_candidate_summary)
    print(winning_candidate_summary)
