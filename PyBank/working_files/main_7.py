import csv
import os


# set path for file
# cereal_csv = os.path.join("cereal.csv")
budget_csv = os.path.join(
    r"C:\Users\justd\Documents\HW_Boot_camp\python-challenge_1\PyBank", "budget_data.csv")


# Open and read csv
# with open(budget_csv) as csv_file:
with open(budget_csv, newline="") as csvfile:

    csv_reader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvfile)
    date = []
    total_months = []
    Profit_Loss = []

    avg_profit_loss = []
    Delta_Profit_Loss = []
    max_monthly_profit_date = ""
    min_monthly_profit_date = ""
 #   for i in csv_reader:

    for j in range(1, len(Profit_Loss)):

        total_months.append(i[0])
        Profit_Loss.append(int(i[1]))
        date.append(j[0])
        # revenueChange.append(RevChg)
        Delta_Profit_Loss.append(Profit_Loss[j] - Profit_Loss[j-1])

        avg_profit_loss = sum(Delta_Profit_Loss) / len(Delta_Profit_Loss)

        max_monthly_profit = max(Delta_Profit_Loss)
        min_monthly_profit = min(Delta_Profit_Loss)

        max_monthly_profit_date = date[Delta_Profit_Loss.index(
            max_monthly_profit)]
        min_monthly_profit_date = date[Delta_Profit_Loss.index(
            min_monthly_profit)]

print(f'            Financial Analysis')
print(f'    ________________________________________')
print(f'    Total Months:          ', len(total_months))
print(f'    Total Profits:          $', sum(Profit_Loss))
print(f'    Total Profits:          $', Delta_Profit_Loss)
#print(f'    Average_Profit_Change:  $', round(avg_profit_loss, 2))
# print(f'    Max Monthly Profit Date and Profit:',
#       max_monthly_profit_date,  '($', max_monthly_profit, ')')
# print(f'    Min Monthly Profit Date and Profit:',
#       min_monthly_profit_date,  '($', min_monthly_profit, ')')
