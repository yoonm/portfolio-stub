import csv
with open("ripper.csv", "r") as csvfile:
    our_reader = csv.reader(csvfile)
    results = [row[4] for row in our_reader]
print(results[0])
