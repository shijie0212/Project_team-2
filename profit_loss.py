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
