import csv

with open('sample/sales100.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file)  # đọc file csv
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