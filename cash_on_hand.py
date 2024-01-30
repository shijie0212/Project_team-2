from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"cash-on-hand-sgd.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for delivery record
    cash_on_hand=[] 

    # append delivery record into the deliveryRecords list
    for row in reader:
        #get the driver id, sales, distance, and event type for each record
        #and append to the deliveryRecords list
        cash_on_hand.append([row[0],row[1]])   
# print(cash_on_hand)

def CashonhandFUC():
    previous = 0
    deficit_list = []
    deficit_info =""
    for item in cash_on_hand:
        new_difference = int(item[1]) - previous 
        previous = int(item[1])
        if new_difference < 0:
            day=item[0]
            # deficit_list.append(new_difference)
            deficit_list.append([abs(new_difference), day])
            deficit_info += f'[CASH DEFICIT]Day:{day}, Difference: SGD{abs(new_difference)}\n'
                # Sort deficit_info by deficit amount in descending order
    deficit_list.sort(reverse = True)

    # Print the top 3 highest deficit amounts and their corresponding days
    for i, (difference, day) in enumerate(deficit_list[:3], start=1):
        if i == 1:
            ordinal = ""
        elif i == 2:
            ordinal = "2ND"
        else:
            ordinal = "3RD"
        deficit_info += f'[{ordinal} HIGHEST DEFICIT] Day:{day}, Difference:SGD{difference}\n'
    return deficit_info
print(CashonhandFUC())