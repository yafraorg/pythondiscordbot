#

import re
import subprocess

def arkmanager(command: str, command2: str, command3: str) -> str:
    result = subprocess.run(['arkmanager', command, command2, command3], stdout=subprocess.PIPE, universal_newlines=True)
    if result.returncode != 0:
        return f"error from system command - error code {result.returncode}"
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    converted_result = ansi_escape.sub('', str(result.stdout))
    return converted_result


def dig(port: str) -> str:
    result = subprocess.run(['gamedig', '--type', 'arkse', '--host', 'localhost', '--port', port], stdout=subprocess.PIPE, universal_newlines=True)
    if result.returncode != 0:
        return f"error from system command - error code {result.returncode}"
    return result.stdout
