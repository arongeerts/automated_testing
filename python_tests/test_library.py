from python_tests.test import db_connection


def execute_function(function_name, params):
    return globals()[function_name](params)


def test_not_null(params):
    database = params['DB']
    table = params['TABLE']
    field = params['FIELD']
    stmt = 'SELECT COUNT(*) FROM {}.{} WHERE {} IS NOT NULL'.format(database, table, field)
    cursor = db_connection.cursor()
    cursor.execute('show databases')
    print(cursor.fetchall())
    cursor.execute(stmt)
    result = cursor.fetchone()
    assert result[0] == 0
