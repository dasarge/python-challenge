import os
import csv

# results_csv = os.path.join("budget_data.csv")
# with open('results_csv', newline='') as csvfile:

budget_data = os.path.join('budget_data.csv')
with open('budget_data.csv', newline="") as csvfile:

    total_votes = 0

    # with open('results_csv', newline='') as csvfile:

    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:
        total_votes += 1

    print(f'Total Votes: {total_votes}')
