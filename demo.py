import asyncio
import arkCommands

async def demo():
    ret = await arkCommands.arkmanager(["echo", "status", "@main"])
    return ret

async def main():
    print(f"started demo function")
    ret = await demo()
    print(ret)
    print(f"finished demo function")

asyncio.run(main())