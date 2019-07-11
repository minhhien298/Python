import csv

with open('sample/movies.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} - {row[1]} - {row[2]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')

import csv

with open('sales100.csv') as csv_file:  # mở file csv
        csv_reader = csv.reader(csv_file)  # đọc file csv
        region_set = set()
        count = 0
        for row in csv_reader:  # vòng lặp for chạy từng dòng trong file
            if count > 0:
                region_set.add(row[0])
            count += 1

        print(sorted(region_set))





    # luc phim theo nam
    # cac phim khong lap lai
    # the loai phim nao co nhieu phim nhat, the loai it nhat