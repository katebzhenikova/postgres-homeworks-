import csv


def read_csv(filename):
    with open(filename, newline='') as f:
        reader = csv.reader(f)
        return list(reader)[1:]


#print(read_csv('north_data/employees_data.csv'))
