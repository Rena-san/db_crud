class TestTableQueries:
    INSERT_RECORD = """
             INSERT INTO `test` (name, status_id, method_name, project_id, 
                                 session_id, start_time, end_time, 
                                 env, browser) 
             VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
                   """

    COPY_RECORD = """
                INSERT INTO `test` (name, status_id, method_name, project_id, 
                                    session_id, env, browser) 
                SELECT name, status_id, method_name, project_id, session_id, 
                        env, browser
                FROM `test` WHERE `id` IN ({record_id})
                """

    SELECT_ALL = "SELECT id FROM `test`"

    SELECT_LAST_RECORD = """
                SELECT `id` 
                FROM `test` 
                WHERE `id` = LAST_INSERT_ID();
                """

    UPDATE_DATA = """
                UPDATE `test` 
                SET start_time = %s, end_time = %s
                """

    DELETE_RECORD_BY_ID = """
                DELETE FROM `test` 
                WHERE `id` IN ({record_id})
                """
