import re

var = {}

data_types = ['int', 'char', 'double', 'float', 'void']

def assign_var(key, val):
    var[key] = val

def get_var(key):
    return var[key]

def compile(input):
    output = ''
    lines = re.split('[\n\t;]+', input)

    for line in lines:
        tokens = re.split('\s+', line)
        for i, token in enumerate(tokens):
            if token in data_types:
                assign_var(tokens[i+1], tokens[i+3])

    return var