import aiohttp
import json
import asyncio
import re
import sys
import os

PROMOTIONS = "https://files.minecraftforge.net/net/minecraftforge/forge/promotions_slim.json"
MAVEN = "https://maven.minecraftforge.net/net/minecraftforge/forge"


class Main:
    async def main():
        async with aiohttp.ClientSession() as session:
            async with session.get(PROMOTIONS) as response:
                promos = (await response.json())["promos"]

            by_mc = {}
            for key, forge_version in promos.items():
                m = re.match(r"^(.*)-(recommended|latest)$", key)
                if not m:
                    continue
                mc_version, kind = m.groups()
                # prefer "recommended" over "latest" if both exist
                if mc_version not in by_mc or kind == "recommended":
                    by_mc[mc_version] = forge_version

            data = {}
            for mc_version, forge_version in by_mc.items():
                full = f"{mc_version}-{forge_version}"
                url = f"{MAVEN}/{full}/forge-{full}-installer.jar"
                async with session.head(url, allow_redirects=True) as resp:
                    if resp.status == 200:
                        data[mc_version] = {"forge": forge_version, "url": url}

            def sort_key(v):
                return [int(p) if p.isdigit() else p for p in re.split(r"[.\-]", v)]

            ordered = dict(sorted(data.items(), key=lambda kv: sort_key(kv[0]), reverse=True))
            latest = next(iter(ordered), None)

            return {"latest": latest, "versions": ordered}


if __name__ == "__main__":
    try:
        data = asyncio.run(Main.main())
        with open("forge-versions.json", "w", encoding="utf-8") as f:
            json.dump(data, f, indent=4)
    except KeyboardInterrupt:
        print("Process stopping due to keyboard interrupt")
        try:
            sys.exit(130)
        except SystemExit:
            os._exit(130)
