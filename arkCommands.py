# -------------------------------------------------------------------------------
#  Copyright 2018 yafra.org
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.
# -------------------------------------------------------------------------------
# command module for ark server management called by a bot

import re
import subprocess


async def arkmanager(command: []) -> str:
    command.insert(0, "/home/arkserver/bin/arkmanager")
    result = subprocess.run(command, stdout=subprocess.PIPE,
                            universal_newlines=True, shell=False)
    if result.returncode != 0:
        return f"error from system command - error code {result.returncode}"
    ansi_escape = re.compile(r'\x1B\[[0-?]*[ -/]*[@-~]')
    converted_result = ansi_escape.sub('', str(result.stdout))
    return converted_result


async def dig(port: str) -> str:
    result = subprocess.run(['/usr/bin/gamedig', '--type', 'arkse', '--host', 'localhost', '--port', port],
                            stdout=subprocess.PIPE, universal_newlines=True)
    if result.returncode != 0:
        return f"error from system command - error code {result.returncode}"
    return result.stdout
