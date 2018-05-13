import re

var = {}

data_types = ['int', 'char', 'double', 'float', 'void']

def assign_var(key, val):
    var[key] = val

def get_var(key):
    return var[key]

def compile(input):
    output = ''
    lines = re.split('[\s;]+', input)

    return lines