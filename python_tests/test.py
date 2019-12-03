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
        except AssertionError as e:
            nb_failures += 1
            json_log = {'test_name': test_name, 'error_msg': error_msg, 'traceback': traceback.format_exc(), 'error': str(e)}
            output_log.write(json.dumps(json_log))

    print('successes: {}, failures, {}'.format(nb_passed_tests, nb_failures))

    if nb_failures > 0:
        sys.exit(1)


if __name__ == '__main__':
    main()