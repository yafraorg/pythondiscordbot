#

import re
import subprocess

def status():
    result = subprocess.run(['arkmanager', 'status', '@all'], stdout=subprocess.PIPE, universal_newlines=True)
    if result.returncode != 0:
        return f"error from system command - error code {result.returncode}"
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    converted_result = ansi_escape.sub('', str(result.stdout))
    return converted_result


def dig():
    result = subprocess.run(['gamedig', '--type', 'arkse', '--host', 'localhost', '--port', '27015'], stdout=subprocess.PIPE, universal_newlines=True)
    if result.returncode != 0:
        return f"error from system command - error code {result.returncode}"
    return result.stdout
