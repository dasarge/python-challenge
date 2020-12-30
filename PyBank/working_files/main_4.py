import os
import csv

results_csv = os.path.join("budget_data.csv")
with open('results_csv', newline='') as csvfile:
title = []  # Title of Study
number_months = []  # Total_months Total Months:
total_profits = []  # Total profits
month_to_month_change_profits = []  # Month to month change in profits
average_month_to_month_change_profits = []  # Average monthly profit change
highest_profits = []  # Greatest increase in profits
highest_profits_date = []  # Date greatest increase in profits
highest_profits_amount = []  # Amount greatest increase in profits
lowest_profits = []  # greatest decrease in profits
lowest_profits_date = []  # Date of greatest decrease in profits
lowest_profits_amount = []  # Amount of greatest decrease in profits
csv_header = []
# start count after header row
#csv_header = next(results_csv)

# Use encoding for Windows
# with open(results_csv, newline='', encoding='utf-8') as csvfile:
with open('results_csv', newline='') as csvfile:
    # with open(results_csv, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(results_csv)
    count = len()
    summary = []
    # for row in csvreader:
    #     # Add title
    #     title.append(row[1])

    #     # Add price
    #     price.append(row[4])

    #     # Add number of subscribers
    #     subscribers.append(row[5])

    #     # Add amount of reviews
    #     reviews.append(row[6])

    #     # Determine percent of review left to 2 decimal places
    #     percent = round(int(row[6]) / int(row[5]), 2)
    #     review_percent.append(percent)

    #     # Get length of the course to just a number
    #     new_length = row[9].split(" ")
    #     length.append(float(new_length[0]))

# Zip lists together
cleaned_csv = zip(title, price, subscribers, reviews, review_percent, length)

# Set variable for output file
output_file = os.path.join("web_final.csv")

#  Open the output file
with open(output_file, "w", newline="") as datafile:
    writer = csv.writer(datafile)

    # Write the header row
    writer.writerow(["Title", "Course Price", "Subscribers", "Reviews Left",
                     "Percent of Reviews", "Length of Course"])

    # Write in zipped rows
    writer.writerows(cleaned_csv)
