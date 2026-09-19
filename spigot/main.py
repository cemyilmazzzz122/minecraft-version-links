import aiohttp
import json
import asyncio
import re
import sys
import os

PAGE = "https://getbukkit.org/download/spigot"
CDN = "https://cdn.getbukkit.org/spigot/spigot-{version}.jar"


async def headStatus(session, url, attempts=3):
    # Retry on 5xx / connection errors so a transient CDN hiccup
    # doesn't silently drop a version from the output.
    status = None
    for attempt in range(1, attempts + 1):
        try:
            async with session.head(url, allow_redirects=True) as resp:
                status = resp.status
        except (aiohttp.ClientError, asyncio.TimeoutError) as e:
            status = type(e).__name__
        else:
            if status < 500:
                return status
        if attempt < attempts:
            await asyncio.sleep(attempt * 5)
    return status


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
                status = await headStatus(session, url)
                if status == 200:
                    data[v] = url
                else:
                    print(f"Skipping {v}: {url} ({status})")

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
