import os
import sys
import json
import asyncio
import aiohttp
import logging

logging.basicConfig(level=logging.INFO)

GIST_API = "https://api.github.com/gists"


async def upload():
    token = os.environ.get("GIST_TOKEN")
    gist_id = os.environ.get("GIST_ID")

    if not token or not gist_id:
        logging.error("GIST_TOKEN and GIST_ID environment variables are required")
        sys.exit(1)

    with open("folia-versions.json", "r", encoding="utf-8") as f:
        json_content = f.read()

    with open("folia-versions.md", "r", encoding="utf-8") as f:
        md_content = f.read()

    payload = {
        "files": {
            "folia-versions.json": {"content": json_content},
            "folia-versions.md": {"content": md_content},
        }
    }

    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }

    async with aiohttp.ClientSession() as session:
        logging.info(f"Updating gist {gist_id}...")
        async with session.patch(
            f"{GIST_API}/{gist_id}", headers=headers, data=json.dumps(payload)
        ) as resp:
            logging.info(f"Response status: {resp.status}")
            text = await resp.text()
            if resp.status != 200:
                logging.error(f"Failed to update gist: {text}")
                sys.exit(1)
            logging.info("Gist updated successfully.")


if __name__ == "__main__":
    asyncio.run(upload())
