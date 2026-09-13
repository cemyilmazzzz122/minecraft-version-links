import aiohttp
import json
import asyncio
import sys
import os

META = "https://meta.fabricmc.net/v2/versions"


class Main:
    async def main():
        async with aiohttp.ClientSession() as session:
            async with session.get(f"{META}/game") as response:
                game_versions = await response.json()

            async with session.get(f"{META}/loader") as response:
                loaders = await response.json()
            loader_version = next(l["version"] for l in loaders if l["stable"])

            async with session.get(f"{META}/installer") as response:
                installers = await response.json()
            installer_version = next(i["version"] for i in installers if i["stable"])

            data = {}
            for v in game_versions:
                version_id = v["version"]
                url = f"{META}/loader/{version_id}/{loader_version}/{installer_version}/server/jar"
                data[version_id] = {
                    "stable": v["stable"],
                    "loader": loader_version,
                    "installer": installer_version,
                    "url": url,
                }

            latest = game_versions[0]["version"] if game_versions else None
            latest_stable = next((v["version"] for v in game_versions if v["stable"]), latest)

            return {
                "latest": latest,
                "latestStable": latest_stable,
                "loader": loader_version,
                "installer": installer_version,
                "versions": data,
            }


if __name__ == "__main__":
    try:
        data = asyncio.run(Main.main())
        with open("fabric-versions.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except KeyboardInterrupt:
        print("Process stopping due to keyboard interrupt")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
