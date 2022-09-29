#The data we need to retrieve.
# 1. The total number of votes
# 2. A complete list of candidates who received votes
# 3. The percentage of votes each candidate won
# 4. The total number of votes each candidate won
# 5. The winner of the election based on popular vote

# Add our dependencies
import csv

import os

# Assign a variable for the file to load and the path
file_to_load = os.path.join("Resources", "election_results.csv")

# Create a filename variable path to the file
file_to_save = os.path.join("Analysis","election_analysis.txt")

#Intitalizing a total vote counter
total_votes = 0

# candidates names
candidate_options = []

# candidate votes
candidate_votes = {}

#Winning candidate and tracker
winner = ""

winning_count = 0

winning_percentage = 0

# Open election results and read the file
with open(file_to_load) as election_data:

# Read the file object with the reader function
    file_reader = csv.reader(election_data)

# Print the header row.
    headers = next(file_reader)

# Print each row in the CSV file
    for row in file_reader:
            
    #2. Add to the total vote count

        total_votes +=1

        # Print candidates name from each row
        candidate_name = row[2]

        #If statement
        if candidate_name not in candidate_options:

            # Add it to the list of candidates
            candidate_options.append(candidate_name)
            
        #Value for the key
            candidate_votes[candidate_name] = 0

        # Add a counter
        candidate_votes[candidate_name] += 1

# Save the results to our text file
with open(file_to_save, "w") as txt_file:

# Final count to the terminal
    election_results =( 
        f"\nElection Results\n"
        f"------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"------------------\n")
    
    print(election_results, end="")

    txt_file.write(election_results)

    for candidate_name in candidate_options:

        #Vote count of candidate
        votes = candidate_votes[candidate_name]

        #Percentage of votes
        vote_percentage = (votes)/(total_votes) * 100
        x = round(vote_percentage,1)

    # Determine the winner
        if (votes > winning_count) and (vote_percentage > winning_percentage):

            winning_count = votes

            winning_percentage = vote_percentage

            winner = candidate_name
        
        # Code updated to = candidate results
        candidate_results = (f"{candidate_name}: received {x}% ({votes:,})\n")

        # Print each candidate results,counts,and percentage
        print(candidate_results)

        # Save results to text file
        txt_file.write(candidate_results)
    
        y = round(winning_percentage,1)
    winning_candidate_summary = ( 
        f"-------------------\n"
        f"Winner: {winner}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {y}%\n"
        f"-------------------\n")
    print(winning_candidate_summary)

    # Save the winning candidate result on text file
    txt_file.write(winning_candidate_summary)
