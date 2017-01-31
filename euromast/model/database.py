import psycopg2
import psycopg2.extras
from os import environ, path

class Database:
    def __init__(self):
        self.conn = psycopg2.connect(environ.get('DATABASE_URL'))
        self.openCur = None

    def getConn(self):
        self.openCur = self.conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
        return self.openCur

    def closeConn(self):
        self.openCur.close()
        self.openCur = None

    def commit(self):
        return self.conn.commit()

    def migrateAndSeed(self):
        buf = open(path.join(path.dirname(__file__), 'data.sql'), 'r')
        sql = buf.read()
        buf.close()
        sqlCommand = sql.split(';')[:-1]

        curr = self.getConn()

        for command in sqlCommand:
            try:
                curr.execute(command)
            except Exception as e:
                    print(e)

        self.commit()
        self.closeConn()
