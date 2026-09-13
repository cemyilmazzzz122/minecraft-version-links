# Folia versions links

JSON containing links to all known [Folia](https://papermc.io/software/folia) versions and their latest build download URL.

This is the Folia counterpart of [osipxd's Paper versions links](https://gist.github.com/osipxd/6119732e30059241c2192c4a8d2218d9) gist, kept up to date automatically by a scheduled GitHub Actions workflow (adapted from [qing762/paper-version-links](https://github.com/qing762/paper-version-links)'s approach), instead of being maintained by hand.

## How it works

A GitHub Actions workflow runs every 3 hours (and on every push that touches `folia/`):

1. `main.py` queries the [PaperMC Fill API](https://fill.papermc.io) for the `folia` project, resolving every known Minecraft version to its latest build's download URL.
2. `lib/validate.py` lints the code and checks that every download link actually resolves.
3. `lib/upload_gist.py` pushes the freshly generated `folia-versions.json` (and the accompanying `folia-versions.md` note) to a public Gist via the GitHub API.
4. The workflow also commits the updated `folia-versions.json` back to this folder.

## Data

Latest data: [Gist](https://gist.github.com/cemyilmazzzz122/c12cf493b0f1e104c175f2bc8a1eccb6) or `folia-versions.json` in this folder.

Raw JSON: `https://gist.githubusercontent.com/cemyilmazzzz122/c12cf493b0f1e104c175f2bc8a1eccb6/raw/folia-versions.json`

Format:

```json
{
    "latest": "26.2",
    "versions": {
        "26.2": "https://fill-data.papermc.io/v1/objects/<hash>/folia-26.2-7.jar",
        "26.1.2": "https://fill-data.papermc.io/v1/objects/<hash>/folia-26.1.2-8.jar"
    }
}
```

## Run locally

```bash
pip install -r requirements.txt
cd folia
python main.py
```

Produces `folia-versions.json` in this folder.

## Setup for the auto-update workflow (maintainer notes)

The workflow needs:

- A repository secret `GIST_TOKEN` — a GitHub token with the `gist` scope.
- A repository variable `GIST_ID_FOLIA` — the id of the target Gist (from its URL: `gist.github.com/<user>/<GIST_ID>`).

## License

[MIT](../LICENSE)
