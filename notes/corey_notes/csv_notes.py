# csv
import csv

names = []
html_output = ''

# for files in different directories, use relative file path syntax
with open('./working_files/csv_sample.csv', 'r') as csv_file:
    csv_reader = csv.reader(csv_file)

    # next method skips over lines in reader
    # next(csv_reader) 

    # for line in csv_reader:
    #     print(line)

    with open('./working_files/csv_sample1.csv', 'w') as new_file:
        # delimiter specifies separator if not comma
        csv_writer = csv.writer(new_file, delimiter='-')
        for line in csv_reader:
            csv_writer.writerow(line)

    # csv_dict_reader = csv.DictReader(csv_file)
    # for line in csv_dict_reader:
    #     print(line)

    # with open('csv_sample1.csv', 'w') as new_file:
    #     field_names = ['first_name', 'last_name']

    #     csv_dict_writer = csv.DictWriter(new_file, fieldnames=field_names)
    #     # write header for first line if fieldnames are specified
    #     csv_dict_writer.writeheader()

    #     for line in csv_dict_reader:
    #         # del deletes info according to column name in reader file
    #         del line['last_name']

    #         csv_dict_writer.writerow(line)

    csv_reader = csv.DictReader(csv_file)
    for line in csv_reader:
        print(line)
        names.append(f"{line['first_name']} {line['last_name']}")

    for name in names:
        print(name)