import os
import re
import subprocess

def compile(code):
    output = ''

    f = open('input.c', 'w')
    f.write(code)
    f.close()

    os.system('gcc -o output input.c')

    if re.search('scanf', code):
        output = 'ERROR\nCompiler does not support operation!'
    else:
        output = subprocess.check_output('./output').decode('utf-8')

    return output