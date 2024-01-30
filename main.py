import Overhead,cash_on_hand,profit_loss
def main():
    overhead_result=Overhead.overheadfuc()
    cash_on_hand_result=cash_on_hand.CashonhandFUC()
    profit_loss_result=profit_loss.profitlossFUC()
    # Concatenate the results
    summary = f"{overhead_result}{cash_on_hand_result}{profit_loss_result}"

    # Return the summary string
    return summary

# Open the file and write the result
with open("Summary_report.txt", "w") as file:
    # Call main function to get the result
    summary = main()
    # Write the result to the file
    file.write(summary)