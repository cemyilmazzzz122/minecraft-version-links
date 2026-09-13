# Purpur versions links

JSON containing links to all known [Purpur](https://purpurmc.org/) (Paper fork) versions and their latest build download URL.

Sibling of [Folia](../folia) and [osipxd's Paper versions links](https://gist.github.com/osipxd/6119732e30059241c2192c4a8d2218d9). A GitHub Actions workflow queries the official [PurpurMC API](https://api.purpurmc.org) every 3 hours and pushes the result to a public Gist and to `purpur-versions.json` in this folder.

## Data

Latest data: [Gist](https://gist.github.com/cemyilmazzzz122/a1575b6b1264873c48ad6577440d8217), or `purpur-versions.json` in this folder.

Raw JSON: `https://gist.githubusercontent.com/cemyilmazzzz122/a1575b6b1264873c48ad6577440d8217/raw/purpur-versions.json`

Format:

```json
{
    "latest": "1.21.11",
    "versions": {
        "1.21.11": "https://api.purpurmc.org/v2/purpur/1.21.11/2568/download"
    }
}
```

## Run locally

```bash
pip install -r requirements.txt
cd purpur
python main.py
```

## Setup for the auto-update workflow (maintainer notes)

- Repository secret `GIST_TOKEN` — a GitHub token with the `gist` scope.
- Repository variable `GIST_ID_PURPUR` — the id of the target Gist.

## License

[MIT](../LICENSE)
