# Minecraft version links

JSON files with download links for every known version of popular Minecraft server software, kept up to date automatically by scheduled GitHub Actions workflows. Each platform lives in its own folder and publishes to its own public Gist.

Format follows [osipxd's Paper versions links](https://gist.github.com/osipxd/6119732e30059241c2192c4a8d2218d9) gist (approach adapted from [qing762/paper-version-links](https://github.com/qing762/paper-version-links)).

| Platform | Folder | Gist | Raw JSON |
|---|---|---|---|
| Fabric | [`fabric/`](fabric) | [c8915045…](https://gist.github.com/cemyilmazzzz122/c8915045aecf952f0a65e7f08a09dc35) | [fabric-versions.json](https://gist.githubusercontent.com/cemyilmazzzz122/c8915045aecf952f0a65e7f08a09dc35/raw/fabric-versions.json) |
| Folia | [`folia/`](folia) | [c12cf493…](https://gist.github.com/cemyilmazzzz122/c12cf493b0f1e104c175f2bc8a1eccb6) | [folia-versions.json](https://gist.githubusercontent.com/cemyilmazzzz122/c12cf493b0f1e104c175f2bc8a1eccb6/raw/folia-versions.json) |
| Forge | [`forge/`](forge) | [f9bf284d…](https://gist.github.com/cemyilmazzzz122/f9bf284d57eb271abe2e64daee68f249) | [forge-versions.json](https://gist.githubusercontent.com/cemyilmazzzz122/f9bf284d57eb271abe2e64daee68f249/raw/forge-versions.json) |
| Purpur | [`purpur/`](purpur) | [a1575b6b…](https://gist.github.com/cemyilmazzzz122/a1575b6b1264873c48ad6577440d8217) | [purpur-versions.json](https://gist.githubusercontent.com/cemyilmazzzz122/a1575b6b1264873c48ad6577440d8217/raw/purpur-versions.json) |
| Spigot | [`spigot/`](spigot) | [0f26a94d…](https://gist.github.com/cemyilmazzzz122/0f26a94dd2b9ae3b1655621c8ccb3927) | [spigot-versions.json](https://gist.githubusercontent.com/cemyilmazzzz122/0f26a94dd2b9ae3b1655621c8ccb3927/raw/spigot-versions.json) |
| Velocity | [`velocity/`](velocity) | [0ecd1886…](https://gist.github.com/cemyilmazzzz122/0ecd188622159f87231d594e1c54e07f) | [velocity-versions.json](https://gist.githubusercontent.com/cemyilmazzzz122/0ecd188622159f87231d594e1c54e07f/raw/velocity-versions.json) |

See each folder's README for platform-specific notes and the JSON format.

## How it works

Every platform has its own workflow in [`.github/workflows/`](.github/workflows), running every 3 hours (staggered so they don't overlap), on every push that touches its folder, and on manual dispatch:

1. `<platform>/main.py` queries the platform's API and writes `<platform>-versions.json`.
2. `<platform>/lib/validate.py` lints the code and checks that the download links resolve.
3. `<platform>/lib/upload_gist.py` pushes the JSON (and the accompanying `<platform>-versions.md` note) to that platform's Gist.
4. The workflow commits the updated JSON back to this repo.

## Run locally

```bash
pip install -r requirements.txt
cd folia
python main.py
```

Produces `folia-versions.json` in that folder.

## Setup for the auto-update workflows (maintainer notes)

- Repository secret `GIST_TOKEN` — a GitHub token with the `gist` scope.
- Repository variables `GIST_ID_FABRIC`, `GIST_ID_FOLIA`, `GIST_ID_FORGE`, `GIST_ID_PURPUR`, `GIST_ID_SPIGOT`, `GIST_ID_VELOCITY` — the id of each platform's Gist.

## License

[MIT](LICENSE)
