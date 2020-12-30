import csv
import os

# set path for file
# cereal_csv = os.path.join("cereal.csv")
budget_csv = os.path.join(
    r"C:\Users\justd\Documents\HW_Boot_camp\python-challenge_1\PyBank", "budget_data.csv")
# -------------------------------------------------------

# Open and read csv
# with open(budget_csv) as csv_file:
with open(budget_csv, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    # csv_header = next(csvfile) # <= this is incorrect
    header = next(csv_reader)

    date = []
    # total_months = [] # Changed name
    months = []
    total_months = 0
    total_net = 0
    Profit_Loss = []
    Delta_Profit_Loss = []
    max_monthly_profit = ["", 0]
    min_monthly_profit = ["", 9999999999999999999]
    avg_profit_loss = []

    first_row = next(csv_reader)
    total_months += 1
    total_net += int(i[1])
    prev_net = int(first_row[1])

    for i in csv_reader:
        # date.append(i[0])
        months.append(i[0])
        total_months += 1  # Add one for each month=> 1 row equals each month
        total_net += int(i[1])
        # revenue.append(int(row[1]))
        # Profit_Loss.append(int(i[1]))
        net_change = int(i[1]) - prev_net
        prev_net = int(i[1])
        Delta_Profit_Loss.append(net_change)

    if net_change > max_monthly_profit[1]:
        max_monthly_profit[0] = i[0]
        max_monthly_profit[1] = net_change

    if net_change < min_monthly_profit[1]:
        min_monthly_profit[0] = i[0]
        min_monthly_profit[1] = net_change
​
# -----------------------------------------------------------------------
# for j in range(1, len(Profit_Loss)):

# TotalRev = TotalRev + int(row[1])

#   Delta_Profit_Loss.append(Profit_Loss[j] - Profit_Loss[j-1])

# RevEnd = int(row[1])

# AveRevChg = TotalRevChange / itemCount
avg_profit_loss = sum(Delta_Profit_Loss) / len(Delta_Profit_Loss)

# GIncrease = max(revenueChange)
# max_monthly_profit = max(Delta_Profit_Loss)

# IncreaseDate = date[revenueChange.index(GIncrease)]
# max_monthly_profit_date = date[Delta_Profit_Loss.index(
#     max_monthly_profit)]
#       min_monthly_profit_date = date[Delta_Profit_Loss.index(
#          min_monthly_profit)]
# --write to file----------------------------------------------
# with open('financial_report' + str(str(i)+1) + '.txt', 'w') as text:
# --------------------------------------------------------------
print(f'            Financial Analysis')
print(f'    ________________________________________')
print(f'    Total Months:          ', total_months)
print(f'    Total Profits:          $', total_net)
print(f'    Average_Profit_Change:  $', round(avg_profit_loss, 2))
print(f'    Max Monthly Profit Date and Profit:',
      max_monthly_profit[0],  '($', max_monthly_profit[1], ')')
print(f'    Min Monthly Profit Date and Profit:',
      min_monthly_profit[0],  '($', min_monthly_profit[1], ')')
