import csv

with open('sample/sales100.csv', mode='r', encoding="utf8") as in_file:
    csv_reader = csv.reader(in_file)  # đọc file csv
    next(csv_reader, None)
    #data = list(csv_reader)
    #row_count = len(data)
    #with open('sample/sales100.csv', mode='w', encoding="utf8") as outfile:
        #writer = csv.writer(outfile)
    mydict = {rows[2]:rows[11] for rows in csv_reader}


print(mydict)
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