from tests.data_for_test1 import TestData
from processing.constans.test_table_sql_queries import TestTableQueries


class TestTable:
    def __init__(self, connection):
        self.connection = connection

    def create(self, start, end):
        test_record = (TestData.test_data_1
                       + (start, end)
                       + TestData.test_data_2)
        with self.connection.cursor() as cursor:
            cursor.execute(TestTableQueries.INSERT_RECORD, test_record)
            self.connection.commit()

    def get_all(self):
        with self.connection.cursor() as cursor:
            cursor.execute(TestTableQueries.SELECT_ALL)
            rows = cursor.fetchall()
            return rows

    def copy(self, record_id):
        with self.connection.cursor() as cursor:
            cursor.execute(
                TestTableQueries
                .COPY_RECORD
                .format(record_id=record_id)
            )

    def get_last_record(self):
        with self.connection.cursor() as cursor:
            cursor.execute(TestTableQueries.SELECT_LAST_RECORD)
            rows = cursor.fetchall()
            return rows

    def update(self, start, end):
        with self.connection.cursor() as cursor:
            cursor.execute(TestTableQueries.UPDATE_DATA, (start, end))
            self.connection.commit()

    def delete(self, record_id):
        with self.connection.cursor() as cursor:
            cursor.execute(
                TestTableQueries
                .DELETE_RECORD_BY_ID
                .format(record_id=record_id)
            )
            self.connection.commit()
