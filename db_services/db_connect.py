import pymysql

from db_services.config import Config


class TestQueries:
    connection = None

    def execute_script(self):
        if self.connection is None:
            return self.__connect_with_db()
        return self.connection

    def close_connection(self):
        if self.connection is not None:
            return self.connection.close()

    def __connect_with_db(self):
        self.connection = pymysql.connect(
            host=Config.HOST,
            user=Config.USER,
            port=Config.PORT,
            password=Config.PASSWORD,
            database=Config.DB_NAME,
            cursorclass=pymysql.cursors.DictCursor
        )
        return self.connection
