from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"profit-and-loss-sgd.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for profit and loss
    profitloss=[] 

    # append profit into the profit and lost list
    for row in reader:
        #get the days, sales, trading profit, operating expenses and net profit for each record
        #and append to the profit and loss list
        profitloss.append([row[0],row[1],row[2],row[3],row[4]])   
# print(profitloss)

def profitlossFUC():
    previous = 0
    deficit_list = []
    deficit_info=""
    for item in profitloss:
        new_difference = int(item[4]) - previous 
        previous = int(item[4])
        if new_difference < 0:
            day=item[0]
            # deficit_list.append(new_difference)
            deficit_list.append([abs(new_difference), day])
            deficit_info += f'[NET PROFIT DEFICIT]Day:{day}, Difference: SGD{abs(new_difference)}\n'
                # Sort deficit_info by deficit amount in descending order
    deficit_list.sort(reverse=True)
