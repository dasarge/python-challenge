import csv
import os

# cereal_csv = os.path.join("cereal.csv")
budget_csv = os.path.join('budget_data.csv')

# Open and read csv
with open(budget_csv) as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")

    # Read the header row first (skip this part if there is no header)
    csv_header = next(csv_file)

    for x in csv_reader:
        x = csv_reader
        total_months = 0
        monthly_profit = 0
        total_profit = 0
        total_months += 1
        total_profit += int(row[1])
        # if total_months is < 2:
        #     then monthly_profit = 0
        # else:
        #     monthly_profit = monthly_profit
        # total_profit = total_profit + monthly_profit


print(f'    Financial Analysis')
print(f'    ________________________________')
print(f'    Total Months: {total_months}')
print(f'    Total Profits: {total_profit} ')
