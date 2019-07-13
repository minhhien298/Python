import csv
from collections import defaultdict
result = defaultdict(int)

with open('sample/sales100.csv', encoding="utf8") as in_file:
    csv_reader = csv.reader(in_file)  # đọc file csv
    next(csv_reader, None)

    for row in csv_reader:
        key = row[2]
        if key in result:
            pass
        result[key] += float(''.join(row[11].split('|')))
print(sorted(result.items(), key=lambda kv: kv[0]))

# https://stackoverflow.com/questions/14091387/creating-a-dictionary-from-a-csv-file
# https://stackoverflow.com/questions/6740918/creating-a-dictionary-from-a-csv-file




# data = list(csv_reader)
# row_count = len(data)
# with open('sample/sales100.csv', mode='w', encoding="utf8") as outfile:
# writer = csv.writer(outfile)
#print(row_count)


'''
    region_set = set()
    item_set = set()
    count = 0
    genre_dic = dict()
    for row in csv_reader:  # vòng lặp for chạy từng dòng trong file
        if count > 0:
            region_set.add(row[0])
            item_set.add(row[2])
        count += 1

        for genres2 in item_set:
            if genre_dic.get(genres2) is None:
                genre_dic[genres2] = 0
            else:
                # genre_dic[genres2] = int(genre_dic.get(genres2)) + 1
                genre_dic[genres2] += float(''.join(row[11].split('|')))


    print(sorted(region_set))
    print(sorted(item_set))
    print(genre_dic)
'''