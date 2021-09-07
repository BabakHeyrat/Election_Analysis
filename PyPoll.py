# The Data we need to retrieve
#1. Total number of votes cast
#2. A complete list of all the candidates who received votes
#3.The perecentage of votes each candidate won
#4 The total number of votes each candidate won
#5 THe winner of the election based on popular vote.
# Import our dependencies
import csv
import os
# Assign a variable to load a file from a path
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path
file_to_save = os.path.join("analysis", "election_analysis.txt")


#Initialize the total vote counter
total_votes = 0
# Initialize the number of candidates and number of votes
candidate_options= []
#Initialize a candidate vote counter dictionary
candidate_votes = {}
# Open the election results and read the file
# Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0
with open(file_to_load) as election_data:
    # To do: read and analyze the data here
    # Read the file object with the reader function
    file_reader = csv.reader(election_data)

    # Read the header row
    headers = next(file_reader)

    #Print each row in the CSV File
    for row in file_reader:

        # Add to the total vote count
        total_votes += 1

        #Print the candidate name from each row
        candidate_name = row[2]

        # If the candidate does not match any existing name
        if candidate_name not in candidate_options:

            # Add the candidate name to the candidate list
            candidate_options.append(candidate_name)

            # Begin tracking that candidate's vote count.
            candidate_votes[candidate_name] = 0

        #Add a vote that candidate's count
        candidate_votes[candidate_name] += 1
# Determine the percentage of votes for each candidate
#1 Iterate through the candidate list
for candidate_name in candidate_votes:
    #2 Retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #3 calculate the percentage of votes.
    vote_percentage = float(votes) / float(total_votes) * 100
    
    # To do: print out each candidate's name, vote count, and percentage of the votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")
    # Determine wiining vote and candidate
    # Determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        # If true then set winning_count = votes and winning_percent =
        # vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #And, set the winning_candidate equal to the candidate's name.
        winning_candidate = candidate_name
# To do: print out the winning candidate, vote and and percentage
# to terminal
winning_candidate_summary = (
    f'------------------\n'
    f'Winner: {winning_candidate}\n'
    f'Winning Vote Count : {winning_count:,}\n'
    f'Winning Percentage: {winning_percentage:.1f}\n'
    f'----------------\n')
print(winning_candidate_summary)