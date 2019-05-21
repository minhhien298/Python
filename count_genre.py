import csv

# đếm và chọn ra phần tử dictionary nào có value cao nhất
def get_max_from_dic(dictionary):
    max_count = 0
    key_has_max_count = None
    for key, val in dictionary.items():
        if val > max_count:
            key_has_max_count = key
            max_count = val
    return key, max_count


# Liệt kê tất cả genre film
def main():
    with open('movies.csv') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        line_count = 0
        genre_dic = dict()
        for row in csv_reader:
            if line_count > 0:
                genres = row[2].split('|')
                for genre in genres:
                    if genre_dic.get(genre) is None:
                        genre_dic[genre] = 1
                    else:
                        genre_dic[genre] = int(genre_dic.get(genre)) + 1

            line_count += 1

        print(genre_dic)
        print(get_max_from_dic(genre_dic))


if __name__ == "__main__":
    main()