import json
import sys
import traceback
from db_connection import get_conn

test_file = json.load(open('./tests_config.json'))
output_log = open('test_output.txt', 'w')

db_connection = get_conn()


def main():
    nb_passed_tests = 0
    nb_failures = 0

    for test_name in test_file.keys():
        test_config = test_file[test_name]
        print(test_config)
        error_msg = test_config['error_message']
        f = test_config['test']
        params = test_config['params']
        test_function = globals()[f]

        try:
            test_function(params)
            nb_passed_tests += 1
        except AssertionError as e:
            nb_failures += 1
            json_log = {'test_name': test_name, 'error_msg': error_msg, 'traceback': traceback.format_exc()}
            output_log.write(json.dumps(json_log))

    if nb_failures > 0:
        sys.exit(1)

    print('successes: {}, failures, {}'.format(nb_passed_tests, nb_failures))

def not_null(params):
    database = params['DB']
    table = params['TABLE']
    field = params['FIELD']
    stmt = 'SELECT COUNT(*) FROM {}.{} WHERE {} IS NOT NULL'.format(database, table, field)
    cursor = db_connection.cursor()
    cursor.execute(stmt)
    result = cursor.fetchone()
    assert result[0] == 0


if __name__ == '__main__':
    main()