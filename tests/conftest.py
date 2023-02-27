import datetime

import pytest

from db_services.db_connect import TestQueries
from processing.test_table_methods import DBMethods
from utils import Utils

list_id_to_del = []


@pytest.fixture()
def set_up_1():
    connection = TestQueries().execute_script()
    start = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    yield
    end = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    DBMethods(connection).insert_data(start, end)


@pytest.fixture()
def set_up_2():
    connection = TestQueries().execute_script()
    all_id = DBMethods(connection).select_records()
    the_biggest_id = all_id[-1]['id']
    random_id_to_copy = Utils.random_id(the_biggest_id)
    DBMethods(connection).copy_records(random_id_to_copy)
    start = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    yield
    end = datetime.datetime.today().strftime("%Y-%m-%d %H:%M:%S")
    DBMethods(connection).update_data(start, end)
    DBMethods(connection).select_records()
    last_added_id = DBMethods(connection).select_last_record()
    list_id_to_del.append(last_added_id[0]['id'])
    list_id = Utils.from_list_to_str(list_id_to_del)
    DBMethods(connection).delete_record_by_id(list_id)


@pytest.fixture(autouse=True)
def close_connect():
    TestQueries().close_connection()
