#

import re
import subprocess

def status():
    result = subprocess.run(['arkmanager', 'status', '@all'], stdout=subprocess.PIPE, universal_newlines=True)
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    ansi_escape.sub('', result)
    return result


def dig():
    result = subprocess.run(['gamedig', '--type', 'arkse', '--host', 'localhost', '--port', '27015'], stdout=subprocess.PIPE, universal_newlines=True)
    return result
