import csv

# đếm và chọn ra phần tử dictionary nào có value cao nhất

global a
global b

def get_max_from_dic(dictionary):
    max_count = 0
    key_has_max_count = None
    for key, val in dictionary.items():  # Duyệt key, value trong dictionary
        if val > max_count:
            key_has_max_count = key
            max_count = val
    return key_has_max_count, max_count


def checkYear(a,b):
    for aphay in a:  # Lặp qua mảng này
        if b.get(aphay) is None:
            b[aphay] = 1
        else:
            b[aphay] = int(b.get(aphay)) + 1
        return b[aphay]


# Liệt kê tất cả genre film
def main():
    with open('sample/movies.csv') as csv_file:  #Mở file csv ra
        csv_reader = csv.reader(csv_file, delimiter=',')  #đọc file csv với delimiter '
        line_count = 0
        genre_dic = dict()  # Khởi tạo một dictionary
        for row in csv_reader:  # Duyệt từng dòng
            if line_count > 0:  # Chỉ quan tâm đến dòng từ 1 trở đi

                film = row[1]
                if film.endswith(" "):  # Lấy ra năm
                    year = film[-6:-2]
                else:
                    year = film[-5:-1]

                try:  # Cần phải có try để bắt lỗi khi convert string sang int
                    intyear = int(year)  # Chuyển đổi năm dạng string sang integer
                    if 2000 <= intyear <= 2010:
                        genres = row[2].split('|')  # Tách từng genre ra thành một mảng
                        checkYear(genres, genre_dic)

                except ValueError as e:
                    pass

                genres = row[2].split('|')  # Tách từng genre ra thành một mảng
                checkYear(genres, genre_dic)


            line_count += 1

        print(genre_dic)
        print(get_max_from_dic(genre_dic))


if __name__ == "__main__":
    main()