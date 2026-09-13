import aiohttp
import json
import asyncio
import sys
import os

API = "https://api.purpurmc.org/v2/purpur"


class Main:
    async def main():
        async with aiohttp.ClientSession() as session:
            async with session.get(API, headers={"accept": "application/json", "user-agent": "purpur-version-links (github.com/cemyilmazzzz122/minecraft-version-links)"}) as response:
                response = await response.json()
                latest = response["metadata"]["current"]
                versions = response["versions"]

            data = {}
            for v in versions:
                async with session.get(f"{API}/{v}", headers={"accept": "application/json", "user-agent": "purpur-version-links (github.com/cemyilmazzzz122/minecraft-version-links)"}) as response:
                    if response.status != 200:
                        continue
                    res = await response.json()
                    build = res["builds"]["latest"]
                    data[v] = f"{API}/{v}/{build}/download"

            return {"latest": latest, "versions": data}


if __name__ == "__main__":
    try:
        data = asyncio.run(Main.main())
        with open("purpur-versions.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except KeyboardInterrupt:
        print("Process stopping due to keyboard interrupt")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
