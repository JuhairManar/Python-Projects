import csv

with open('./data/currencyrates.csv', 'r',encoding='utf-8') as file:
    lines = csv.reader(file)
    for line in lines:
        if 'Bangladesh' in line[0]:
            print(line)

