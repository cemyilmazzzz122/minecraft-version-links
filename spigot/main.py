import aiohttp
import json
import asyncio
import re
import sys
import os

PAGE = "https://getbukkit.org/download/spigot"
CDN = "https://cdn.getbukkit.org/spigot/spigot-{version}.jar"


class Main:
    async def main():
        async with aiohttp.ClientSession() as session:
            async with session.get(PAGE) as response:
                html = await response.text()

            versions = re.findall(r"<h4>Version</h4>\s*<h2>([^<]+)</h2>", html)
            if not versions:
                raise RuntimeError("No versions found on getbukkit.org page; page layout may have changed")

            data = {}
            for v in versions:
                url = CDN.format(version=v)
                async with session.head(url, allow_redirects=True) as resp:
                    if resp.status == 200:
                        data[v] = url

            return {"latest": versions[0], "versions": data}


if __name__ == "__main__":
    try:
        data = asyncio.run(Main.main())
        with open("spigot-versions.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except KeyboardInterrupt:
        print("Process stopping due to keyboard interrupt")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
