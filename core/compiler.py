import re

var = {}

data_type = ['int', 'char', 'double', 'float', 'void']

def assign_var(key, val):
    var[key] = val

def get_var(key):
    return var[key]

def compile(input):
    skip_if = False
    skip_else = False
    
    output = ''
    lines = re.split('[\n\t;]+', input)

    for index, line in enumerate(lines):
        if skip_if:
            print(line)
            if re.match('\s*}\s*', line):
                continue
            else:
                skip_if = False
                continue

        if skip_else:
            if re.search('else{?', line):
                skip_if = True
                skip_else = False
                continue
        
        lexemes = re.split('\s*', line)
        for index, lexeme in enumerate(lexemes):
            if lexeme in data_type and re.search('=', line):
                vr = re.findall('[int|double|float|char|void] ([a-zA-Z][a-zA-Z0-9_]*) [a-zA-Z0-9!=><+-/* ]+', line)[0]
                expr = re.split('=', line)[1]
                for value in expr:
                    if value in var:
                        expr = expr.replace(value, "{}".format(var[value]))
                assign_var(vr, eval(expr))
                break
            if re.search('printf', lexeme):
                output += "{}\n".format(var[re.findall('printf\((\w+)\)', lexeme)[0]])
                break

        if re.search('if\(([a-zA-Z0-9!=>< ]+)\){?', line):
            condition = re.findall('if\(([a-zA-Z0-9!=>< ]*)\){?', line)[0]
            for index, value in enumerate(condition):
                if value in var:
                    condition = condition.replace(value, "{}".format(var[value]))

            if not eval(condition):
                skip_if = True
                continue
            else:
                skip_else = True
        
    return output