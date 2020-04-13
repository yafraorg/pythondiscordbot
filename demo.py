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
# simple test / demo function for arkCommands

import asyncio
import arkCommands

async def demo():
    ret = await arkCommands.arkmanager(["echo", "1"])
    return ret

async def main():
    print(f"started demo function")
    ret = await demo()
    print(ret)
    print(f"finished demo function")


tst = [main()]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tst))
#python3.7 asyncio.run(main())
