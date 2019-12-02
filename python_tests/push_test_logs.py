with open('test_output.txt') as f:
    lines = f.read().split('\n')
    for line in lines:
        print(line)