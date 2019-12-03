from db_connection import get_conn

db_connection = get_conn()


def execute_function(function_name, params):
    return globals()[function_name](params)


def test_not_null(params):
    database = params['DB']
    table = params['TABLE']
    field = params['FIELD']
    stmt = 'SELECT COUNT(*) FROM {}.{} WHERE {} IS NULL'.format(database, table, field)
    __assert_count_zero(stmt)


def test_timestamp_order(params):
    database = params['DB']
    table = params['TABLE']
    field1 = params['FIELD1']
    field2 = params['FIELD2']
    stmt = 'SELECT COUNT(*) FROM {db}.{tab} WHERE {f1} IS NOT NULL AND {f2} IS NOT NULL AND {f1} > {f2}'.format(
        db=database, tab=table, f1=field1, f2=field2)
    __assert_count_zero(stmt)


def test_field_in_range(params):
    database = params['DB']
    table = params['TABLE']
    field = params['FIELD']
    low = params.get('LOW', '- POWER(2,31)+1')
    high = params.get('HIGH', 'POWER(2,31)-1')
    stmt = 'SELECT COUNT(*) FROM {db}.{tab} WHERE {f} IS NOT NULL and ({f} > {high} OR {f} < {low})'.format(
        db=database, tab=table, f=field, low=low, high=high)
    __assert_count_zero(stmt)


def __assert_count_zero(stmt):
    cursor = db_connection.cursor()
    cursor.execute(stmt)
    result = cursor.fetchone()
    assert result[0] == 0
