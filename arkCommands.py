#
import asyncio
import re
import subprocess


async def arkmanager(command: []) -> str:
    result = subprocess.run(command, stdout=subprocess.PIPE,
                            universal_newlines=True)
    if result.returncode != 0:
        return f"error from system command - error code {result.returncode}"
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    converted_result = ansi_escape.sub('', str(result.stdout))
    return converted_result


async def arkmanager2(command: []) -> str:
    my_command = ' '.join(map(str, command))
    proc = await asyncio.create_subprocess_shell(
        my_command,
        stdout=asyncio.subprocess.PIPE)
    stdout = await proc.communicate()
    if proc.returncode != 0:
        return f"error from system command - error code {proc.returncode}"
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    converted_result = ansi_escape.sub('', str(stdout.decode()))
    return converted_result


async def dig(port: str) -> str:
    result = subprocess.run(['gamedig', '--type', 'arkse', '--host', 'localhost', '--port', port],
                            stdout=subprocess.PIPE, universal_newlines=True)
    if result.returncode != 0:
        return f"error from system command - error code {result.returncode}"
    return result.stdout
