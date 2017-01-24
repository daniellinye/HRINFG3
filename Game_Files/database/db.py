import psycopg2
from os import environ, path

class Database:
    def __init__(self):
        self.conn = psycopg2.connect('postgresql://localhost/?user=postgres&password=postgres')


    def migrateAndSeed(self):
        buf = open(path.join(path.dirname(__file__), 'data.sql'), 'r')
        sql = buf.read()
        buf.close()
        sqlCommand = sql.split(';')
        curr = self.conn.cursor()

        for command in sqlCommand:
            try:
                curr.execute(command)
            except Exception as e:
                print(e)

        self.conn.commit()
        curr.close()
