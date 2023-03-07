import csv

# with open('csv_file', 'action') as alias:
#     csv_reader = csv.reader(alias)

names = []
html_output = ''

with open('csv_sample.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # next(csv_reader) 
    # skips over lines in reader
    
    # for line in csv_reader:
    #     print(line)

    # with open('csv_sample1.csv', 'w') as new_file:
    #     csv_writer = csv.writer(new_file, delimiter='-')
    #     # delimiter specifies separator if not comma
    #     for line in csv_reader:
    #         csv_writer.writerow(line)

    # csv_dict_reader = csv.DictReader(csv_file)
    # for line in csv_dict_reader:
    #     print(line)

    # with open('csv_sample1.csv', 'w') as new_file:
    #     field_names = ['first_name', 'last_name']

    #     csv_dict_writer = csv.DictWriter(new_file, fieldnames=field_names)
    #     csv_dict_writer.writeheader()
    #     # write header for first line if fieldnames are specified

    #     for line in csv_dict_reader:
    #         del line['last_name']
    #         # deletes info according to column name in reader file

    #         csv_dict_writer.writerow(line)

    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line)
        names.append(f"{line['first_name']} {line['last_name']}")

    for name in names:
        print(name)