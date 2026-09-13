# Fabric versions links

JSON containing a ready-to-run server jar download link for **every** Minecraft version [Fabric](https://fabricmc.net/) has ever supported — stable releases as well as snapshots, pre-releases, betas and alphas — each flagged with whether it's stable.

## How it works

Fabric doesn't ship one server jar per Minecraft version like Paper/Folia do — a server jar is generated on demand
from a (game version, loader version, installer version) triple via the official
[Fabric meta API](https://meta.fabricmc.net). This project uses the latest **stable** loader and installer,
combined with every game version the API knows about (stable and unstable alike), via:

```
https://meta.fabricmc.net/v2/versions/loader/<game_version>/<loader_version>/<installer_version>/server/jar
```

Because that URL is deterministic and there are hundreds of game versions (500+, including very old
snapshots/alphas/betas), the workflow doesn't HEAD-check every single one on every run — `lib/validate.py` spot-checks
`latest`, `latestStable`, and a small random sample instead, to avoid hammering the Fabric meta API for no benefit.

A GitHub Actions workflow runs every 3 hours (and on every push that touches `fabric/`), regenerates the mapping, spot-validates
it, pushes the result to a public Gist, and commits `fabric-versions.json` back to this folder.

## Data

Latest data: [Gist](https://gist.github.com/cemyilmazzzz122/c8915045aecf952f0a65e7f08a09dc35), or `fabric-versions.json` in this folder.

Raw JSON: `https://gist.githubusercontent.com/cemyilmazzzz122/c8915045aecf952f0a65e7f08a09dc35/raw/fabric-versions.json`

Format:

```json
{
    "latest": "26.3-rc-2",
    "latestStable": "26.2",
    "loader": "0.19.5",
    "installer": "1.1.2",
    "versions": {
        "26.3-rc-2": {
            "stable": false,
            "loader": "0.19.5",
            "installer": "1.1.2",
            "url": "https://meta.fabricmc.net/v2/versions/loader/26.3-rc-2/0.19.5/1.1.2/server/jar"
        },
        "26.2": {
            "stable": true,
            "loader": "0.19.5",
            "installer": "1.1.2",
            "url": "https://meta.fabricmc.net/v2/versions/loader/26.2/0.19.5/1.1.2/server/jar"
        }
    }
}
```

`latest` is the newest known version regardless of stability; `latestStable` is the newest one with `"stable": true`.

## Run locally

```bash
pip install -r requirements.txt
cd fabric
python main.py
```

## Setup for the auto-update workflow (maintainer notes)

- Repository secret `GIST_TOKEN` — a GitHub token with the `gist` scope.
- Repository variable `GIST_ID_FABRIC` — the id of the target Gist.

## License

[MIT](../LICENSE)
