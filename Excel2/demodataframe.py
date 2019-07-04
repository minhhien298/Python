import psycopg2
try:
    connection = psycopg2.connect(user="user",
                                  password="abc123",
                                  host="192.168.1.123",
                                  port="5432",
                                  database="dvdrental")
    cursor = connection.cursor()
    # Print PostgreSQL Connection properties
    print(connection.get_dsn_parameters(), "\n")

    # Print PostgreSQL version
    #cursor.execute("SELECT film_id, title, description FROM film")
    cursor.execute("INSERT INTO fun (name) VALUES ('Hien');")
    #fun_id = cursor.fetchone()[0]
    #print(fun_id)
    # commit the changes to the database
    connection.commit()
    '''rows = cursor.fetchall()
    for row in rows:
        print(row)'''

except (Exception, psycopg2.Error) as error:
    print("Error while connecting to PostgreSQL", error)
finally:
    if connection:
        cursor.close()
        connection.close()
        print("PostgreSQL connection is closed")