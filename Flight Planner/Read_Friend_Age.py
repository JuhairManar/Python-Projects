import csv
with open('./data/my_friends.csv', 'r',encoding='utf-8') as file:
    lines = csv.reader(file)
    header = next(lines)
    for line in lines:
        print(line)
    print(header)