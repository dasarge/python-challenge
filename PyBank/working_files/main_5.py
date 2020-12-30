import os
import csv

budget_data_csv = os.path.join('budget_data.csv')

with open(budget_data_csv, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)

    for row in csvreader:

        total_votes += 1

        candidate_in = (row[2])
        print(candidate_in)
