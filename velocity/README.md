# Velocity versions links

JSON containing links to all known [Velocity](https://papermc.io/software/velocity) proxy versions and their latest build download URL.

Sibling of [Folia](../folia) and [osipxd's Paper versions links](https://gist.github.com/osipxd/6119732e30059241c2192c4a8d2218d9), built the same way: a GitHub Actions workflow queries the [PaperMC Fill API](https://fill.papermc.io) every 3 hours and pushes the result to a public Gist and to `velocity-versions.json` in this folder.

## Data

Latest data: [Gist](https://gist.github.com/cemyilmazzzz122/0ecd188622159f87231d594e1c54e07f), or `velocity-versions.json` in this folder.

Raw JSON: `https://gist.githubusercontent.com/cemyilmazzzz122/0ecd188622159f87231d594e1c54e07f/raw/velocity-versions.json`

Format:

```json
{
    "latest": "3.4.0-SNAPSHOT",
    "versions": {
        "3.4.0-SNAPSHOT": "https://fill-data.papermc.io/v1/objects/<hash>/velocity-3.4.0-SNAPSHOT-###.jar"
    }
}
```

## Run locally

```bash
pip install -r requirements.txt
cd velocity
python main.py
```

## Setup for the auto-update workflow (maintainer notes)

- Repository secret `GIST_TOKEN` — a GitHub token with the `gist` scope.
- Repository variable `GIST_ID_VELOCITY` — the id of the target Gist.

## License

[MIT](../LICENSE)
