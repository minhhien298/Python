import csv

    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    genre_set = set()
    for row in csv_reader:
        if line_count == 0:
            print(f'Column names are {", ".join(row)}')
            line_count += 1
        else:
            genres = row[2].split('|')
            genre_set |= set(genres)
            line_count += 1

    listphim = list(genre_set)
    print(listphim)
    print(f'Processed {line_count} lines.')

def checklist(T):
 if 'Thriller'in T:
     return True

listso = []



counts = 0
with open('sample/movies.csv', encoding="utf8") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    for row in csv_reader:
     if(checklist(row[2].split('|'))== True ):
            counts += 1
    listso.append(counts)
    print(listso)

#     listso.append(str(sum(checklist(str(row[2].split('|'))) == True for row in csv_reader)))




