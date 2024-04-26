import csv

with open('metro_products.csv', newline='') as csvfile:
    csvreader = csv.reader(csvfile)
    for row in csvreader:
        print(row)