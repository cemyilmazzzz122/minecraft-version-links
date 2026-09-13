import aiohttp
import json
import asyncio
import sys
import os

API = "https://fill.papermc.io/v3/projects/velocity"


class Main:
    async def main():
        async with aiohttp.ClientSession() as session:
            data_out = {}
            versions = []
            async with session.get(
                API,
                headers={"accept": "application/json"},
            ) as response:
                response = await response.json()
                for major, minor in response["versions"].items():
                    versions.extend(minor)
                data = {}
                for x in versions:
                    async with session.get(
                        f"{API}/versions/{x}",
                        headers={"accept": "application/json"},
                    ) as response:
                        response = await response.json()
                        versionName = response["version"]["id"]
                        if not response["builds"]:
                            continue
                        latestBuildNumber = response["builds"][0]
                        buildReq = await session.get(
                            f"{API}/versions/{x}/builds/{latestBuildNumber}",
                            headers={"accept": "application/json"},
                        )
                        res = await buildReq.json()
                        downloads = res.get("downloads", {})
                        if "server:default" not in downloads:
                            continue
                        data[versionName] = downloads["server:default"]["url"]
                data_out["latest"] = next((v for v in versions if v in data), versions[0])
                data_out["versions"] = data
                return data_out


if __name__ == "__main__":
    try:
        data = asyncio.run(Main.main())
        with open("velocity-versions.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except KeyboardInterrupt:
        print("Process stopping due to keyboard interrupt")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
