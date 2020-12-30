# 1. path to data file
# 	 Define variables
# 	 read the csv file
# 1.1 Count the rows to find out the total months reported.
# 1.2 Find the cumulative profit loss from column 2
# 1.3 Calculate the change in profit between each reporting period
# 1.4 Calculate the average profit/loss over the period
# 1.5 find the greatest increase in profit for a period
# 1.6 Find the greatest decrease in profit for a period

# 2. print the variables
#	 print(f'Total votes {total_votes}')
#	 print(f'Each candidate: {candidates_unique}')
#	 print(f'Index: {candidates_unique.index(candidate_in)}')
#    Calculate the canidates vote percentage,
#	 Use x as the looper value

# 3.  Print the variables to the terminal
#	 print(f'Vote count for each candidate: {candidate_vote_count}')
#	 vprint(f'Max votes: {max_votes}')
#	 print(f'Election winner: {election_winner}')

# 4.  Create a text file
#	 Save to the analysis directory


# 1,___________________________________________________

import os
import csv

budget_data_csv = os.path.join('Resources', 'budget_data.csv')

total_months = 0
cumulative_profit_loss = []
change_in_profit = []
average_profit_loss[]
greatest_increase_in_profit[]
greatest_decrease_in_profit[]

with open(Election_Data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:

        total_months += 1

        cumulative_profit_loss = (row[2])

        if candidate_in in candidates_unique:
            candidate_index = candidates_unique.index(candidate_in)
            candidate_vote_count[candidate_index] = candidate_vote_count[candidate_index] + 1
        else:

            candidates_unique.append(candidate_in)
            candidate_vote_count.append(1)


pct = []
max_votes = candidate_vote_count[0]
max_index = 0

for x in range(len(candidates_unique)):

    vote_pct = round(candidate_vote_count[x]/total_votes*100, 2)
    pct.append(vote_pct)

    if candidate_vote_count[x] > max_votes:
        max_votes = candidate_vote_count[x]
        max_index = x

election_winner = candidates_unique[max_index]

# 2.__________________________________________

print('  ')
print('| Election Results |')
print('  ')
print(f'Total Votes: {total_votes}')
print('  ')
for x in range(len(candidates_unique)):
    print(f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})')
print('  ')
print(f'Election winner: {election_winner.upper()}')
print('  ')

# 3.________________________________________________

output_file = os.path.join("Analysis", "pypoll_election_results.txt")
with open(output_file, "w", newline="") as datafile:
    datafile.write('  \n')
    datafile.write('|                  Election Results                  |\n')
    datafile.write('  \n')
    datafile.write(f'Total Votes: {total_votes}\n')
    datafile.write('  \n')
    for x in range(len(candidates_unique)):
        datafile.write(
            f'{candidates_unique[x]} : {pct[x]}% ({candidate_vote_count[x]})\n')
    datafile.write('  \n')
    datafile.write(f'Election winner: {election_winner.upper()}\n')
    datafile.write('  \n')
    datafile.write("  END OF REPORT  ")
