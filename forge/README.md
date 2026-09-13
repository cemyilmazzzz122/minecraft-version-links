# Forge versions links

JSON containing links to the recommended (falling back to latest) [Minecraft Forge](https://files.minecraftforge.net/) installer jar for every Minecraft version Forge supports.

## Note: installer jars, not server jars

Forge distributes an **installer** jar per version (`forge-<mc>-<forge>-installer.jar`); running it with
`--installServer` produces the actual server jar locally. There is no official single-file "just run this" server
jar the way Paper/Folia/Purpur/Velocity provide. Links in this dataset are installer jars from the official
[Forge Maven](https://maven.minecraftforge.net/net/minecraftforge/forge/), sourced from
[`promotions_slim.json`](https://files.minecraftforge.net/net/minecraftforge/forge/promotions_slim.json)
(the "recommended"/"latest" build per Minecraft version).

## How it works

A GitHub Actions workflow runs every 3 hours (and on every push that touches `forge/`):

1. `main.py` reads `promotions_slim.json`, prefers each Minecraft version's "recommended" build (falling back to
   "latest"), builds the Maven installer URL, and checks it resolves.
2. `lib/validate.py` lints the code and re-checks every link.
3. `lib/upload_gist.py` pushes `forge-versions.json` (and `forge-versions.md`) to a public Gist.
4. The workflow commits the updated JSON back to this folder.

## Data

Latest data: [Gist](https://gist.github.com/cemyilmazzzz122/f9bf284d57eb271abe2e64daee68f249), or `forge-versions.json` in this folder.

Raw JSON: `https://gist.githubusercontent.com/cemyilmazzzz122/f9bf284d57eb271abe2e64daee68f249/raw/forge-versions.json`

Format:

```json
{
    "latest": "1.21.11",
    "versions": {
        "1.21.11": {
            "forge": "61.2.0",
            "url": "https://maven.minecraftforge.net/net/minecraftforge/forge/1.21.11-61.2.0/forge-1.21.11-61.2.0-installer.jar"
        }
    }
}
```

## Run locally

```bash
pip install -r requirements.txt
cd forge
python main.py
```

## Setup for the auto-update workflow (maintainer notes)

- Repository secret `GIST_TOKEN` — a GitHub token with the `gist` scope.
- Repository variable `GIST_ID_FORGE` — the id of the target Gist.

## License

[MIT](../LICENSE)
