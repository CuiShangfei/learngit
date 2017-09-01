import csv

filename = 'one_way_adjust2.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)
    print(header_row)

    temp = []
    for row in reader:
        temp.append(float(row[-1]))
    print(temp)

    for index, column_header in enumerate(header_row):
        print(index, column_header)
