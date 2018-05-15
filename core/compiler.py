import re

var = {}

data_type = ['int', 'char', 'double', 'float', 'void']

def assign_var(key, val):
    var[key] = val

def get_var(key):
    return var[key]

def compile(input):
    output = ''
    lines = re.split('[\n\t;]+', input)

    for line in lines:
        lexemes = re.split('\s*', line)
        for index, lexeme in enumerate(lexemes):
            if lexeme in data_type and re.search('=', line):
                assign_var(lexemes[index + 1], eval(re.split('=', line)[1]))
                break
            if re.search('printf', lexeme):
                output += "{}\n".format(var[re.findall('printf\((\w+)\)', lexeme)[0]])

    return output