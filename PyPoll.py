import os
import os.path

# Assign a variable for the file to load and the path.
file_to_load = '/Users/claudiabrito/Desktop/Election-Analysis/Resources/election_results.csv'

# Open the election results and read the file.
election_data = open(file_to_load, 'r')

# To do: perform analysis.

# Close the file.
election_data.close()

# Open the election results and read the file
with open(file_to_load) as election_data:

     # To do: perform analysis.
     print(election_data)
import os
print(dir(os))

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("/Users/claudiabrito/Desktop/Election-Analysis/Resources", "/Users/claudiabrito/Desktop/Election-Analysis/Resources/election_results.csv")
# Open the election results and read the file.


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("/Users/claudiabrito/Desktop/Election-Analysis/Resources/analysis", "/Users/claudiabrito/Desktop/Election-Analysis/Resources/analysis/election_analysis.txt")

# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

# Write some data to the file.
    #txt_file.write("Hello World")
    #txt_file.write("Arapahoe")
    #txt_file.write("Denver")
    #txt_file.write("Jefferson")

# Write three counties to the file. Another option
    #txt_file.write("Arapahoe, Denver, Jefferson")
# Write three counties to the file.
    #txt_file.write("Arapahoe\nDenver\nJefferson")
 # Write three counties to the file.
    txt_file.write("Counties in the Election\n")

    txt_file.write("----------------------------\n")

    txt_file.write("Arapahoe\nDenver\nJefferson")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print each row in the CSV file.
    for row in file_reader:
        print(row)
# Read the file object with the reader function.
    file_reader = csv.reader(election_data)

    # Print the header row.
    headers = next(file_reader)
    print(headers)