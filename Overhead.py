from pathlib import Path
import csv

fp = Path.cwd()/"csv_reports"/"overheads-day-90.csv"

# read the csv file.
with fp.open(mode="r", encoding="UTF-8", newline="") as file:
    reader = csv.reader(file)
    next(reader) # skip header

    # create an empty list for overhead
    overheads=[] 

    # append overhead into the overhead list
    for row in reader:
        #get the category and overhead for each record
        #and append to the overhead list
        overheads.append([row[0],row[1]])   
# print(overheads)


percentagelist=[]
def overheadfuc():
    '''
    Function to produce the highest overhead
    '''
    # Iterate through the overheads data
    for things in overheads:
        # Extract category and percentage values
        cat = things[0]
        percentage = float(things[1])
        # Append percentage to the percentagelist
        percentagelist.append(percentage)
        # Find the highest percentage in the list
        Highest = max(percentagelist)
        # Check if the current percentage is the highest
        if percentage == max (percentagelist):
            category = cat
    return f"[Highest Overhead]{category}:{Highest}%\n"

print(overheadfuc())