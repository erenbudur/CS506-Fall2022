import re
from tokenize import Double

def test_num(value):
    if re.match(r'^\d+$', value) :
        return int(value)
    if re.match(r'^-?\d+(?:\.\d+)$', value) :
        return float(value)
    return value

def read_csv(csv_file_path):
    """
        Given a path to a csv file, return a matrix (list of lists)
        in row major.
    """
    with open(csv_file_path, 'r') as f:
        results = []
        for line in f:
                row = line.rstrip().split(',')
                results.append(list(map(lambda x: test_num(x),row)))

        return results    
