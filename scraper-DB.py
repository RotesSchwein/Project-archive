import mysql.connector

def insert_data_to_db(data):
    try:
        connection = mysql.connector.connect(
            host = '',
            user = 'admin',
            password = '',
            database = 'scraperDB',
            port = 3306
        )
        cursor = connection.cursor()

        for item in data:
            sql = 'INSERT INTO gaijin_channel_article_info (article_title, article_written_time, article_url) VALUES (%s, %s, %s)'
            values = (item.Title, item.Date, item.URL)
            cursor.execute(sql, values)

        connection.commit()
        cursor.close()
        connection.close()
    except mysql.connector.Error as error:
        print(f"Error : {error}")
