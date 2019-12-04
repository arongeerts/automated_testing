import json
import sys
import traceback
from test_library import execute_function

test_file = json.load(open('./tests_config.json'))['tests']
output_log = open('test_output.txt', 'w')



def main():
    nb_passed_tests = 0
    nb_failures = 0

    for test_name in test_file.keys():
        test_config = test_file[test_name]
        error_msg = test_config['error_message']
        f = test_config['test']
        params = test_config['params']

        try:
            print('Running {}...'.format(test_name))
            execute_function(f, params)
            nb_passed_tests += 1
            log({'test_name': test_name, 'result': 'SUCCESS', 'error_msg': error_msg, 'traceback': None, 'error': None})
        except AssertionError as e:
            nb_failures += 1
            log({'test_name': test_name, 'result': 'FAIL', 'error_msg': error_msg, 'traceback': traceback.format_exc(), 'error': str(e)})

    print('successes: {}, failures, {}'.format(nb_passed_tests, nb_failures))

    if nb_failures > 0:
        sys.exit(1)

def log(json_message):
    output_log.write(json.dumps(json_message))


if __name__ == '__main__':
    main()