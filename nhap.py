import csv
import operator
with open('sample/sales100.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    # sortedlist = sorted(csv_reader, key=operator.itemgetter(12), reverse=True)
    sortedlist = sorted(csv_reader, key=lambda row: row[12], reverse=True)
    line_count = 0
    for row in sortedlist:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            print(f'\t{row[0]} - {row[1]} - {row[12]}.')
            line_count += 1
    print(f'Processed {line_count} lines.')






    # luc phim theo nam
    # cac phim khong lap lai
    # the loai phim nao co nhieu phim nhat, the loai it nhat