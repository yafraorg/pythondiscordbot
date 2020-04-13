#
import time
import re
import subprocess


async def arkmanager(command: []) -> str:
    result = subprocess.run(command, stdout=subprocess.PIPE,
                            universal_newlines=True)
    if result.returncode != 0:
        return f"error from system command - error code {result.returncode}"
    time.sleep(3)
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    converted_result = ansi_escape.sub('', str(result.stdout))
    return converted_result


async def dig(port: str) -> str:
    result = subprocess.run(['gamedig', '--type', 'arkse', '--host', 'localhost', '--port', port],
                            stdout=subprocess.PIPE, universal_newlines=True)
    if result.returncode != 0:
        return f"error from system command - error code {result.returncode}"
    return result.stdout
