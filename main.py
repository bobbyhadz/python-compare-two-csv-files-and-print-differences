# Python: Compare two CSV files and print the differences 

with open(
        'csv-file-1.csv', encoding='utf-8'
) as file_1, open(
    'csv-file-2.csv', encoding='utf-8'
) as file_2:
    file_1_lines = file_1.readlines()
    file_2_lines = file_2.readlines()

with open(
    'differences.csv',
    'w',
    encoding='utf-8'
) as differences_file:
    for line in file_2_lines:
        if line not in file_1_lines:
            print(line)
            differences_file.write(line)
