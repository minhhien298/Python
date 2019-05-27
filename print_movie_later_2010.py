import csv

<<<<<<< HEAD
with open('sample/movies.csv') as csv_file:
=======
with open('sample/movies.csv', encoding="utf8") as csv_file:
>>>>>>> 57e9312495c19ad96ca8854812fb4ff0f4712470
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count > 0:
            film = row[1]
            if film.endswith(" "):
                year = film[-6:-2]
            else:
                year = film[-5:-1]

            try: # Cần phải có try để bắt lỗi khi convert string sang int
                if int(year) >= 2010:
                    #print(f'{row[0]} - {row[1]} - {row[2]}.')
                    pass
            except ValueError:
                print(f"{line_count} - {film}")
                #passe
        line_count += 1
    print(f'Processed {line_count} lines.')