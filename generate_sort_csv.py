import csv
file1 = "csv/zadanie.csv"
main_file = "csv/recommends.csv"

with open(main_file, "r") as f:
    lol = f.readlines()
    lol.sort()
with open(file1, 'w', newline='') as csvfile:
    filewriter = csv.writer(csvfile)
    for i in lol:
        tr = i.split(',')
        filewriter.writerow([tr[0], tr[1], tr[2][:-1:]])
