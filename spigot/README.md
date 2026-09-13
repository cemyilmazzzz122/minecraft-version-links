# Spigot versions links

JSON containing links to all known [Spigot](https://www.spigotmc.org/) versions and a prebuilt server jar download URL.

## Important: no official prebuilt jars

Unlike Paper/Folia/Purpur/Velocity, SpigotMC does **not** distribute prebuilt server jars — the Mojang EULA requires
you to compile Spigot yourself locally with [BuildTools](https://www.spigotmc.org/wiki/buildtools/). There is no
official API that returns a direct-download jar URL.

This project instead scrapes version numbers from [getbukkit.org/download/spigot](https://getbukkit.org/download/spigot)
(a long-standing third-party mirror that publishes prebuilt jars) and resolves each version to its stable CDN URL
(`https://cdn.getbukkit.org/spigot/spigot-<version>.jar`). Treat the resulting links as best-effort/community-sourced,
not official Spigot releases.

If you want an official, EULA-compliant build pipeline instead, see [hub.spigotmc.org/versions](https://hub.spigotmc.org/versions/)
for the BuildTools version refs and run BuildTools yourself.

## How it works

A GitHub Actions workflow runs every 3 hours (and on every push that touches `spigot/`):

1. `main.py` fetches `https://getbukkit.org/download/spigot`, extracts every listed version, and checks that
   `https://cdn.getbukkit.org/spigot/spigot-<version>.jar` resolves.
2. `lib/validate.py` lints the code and re-checks every link.
3. `lib/upload_gist.py` pushes `spigot-versions.json` (and `spigot-versions.md`) to a public Gist.
4. The workflow commits the updated JSON back to this folder.

## Data

Latest data: [Gist](https://gist.github.com/cemyilmazzzz122/0f26a94dd2b9ae3b1655621c8ccb3927), or `spigot-versions.json` in this folder.

Raw JSON: `https://gist.githubusercontent.com/cemyilmazzzz122/0f26a94dd2b9ae3b1655621c8ccb3927/raw/spigot-versions.json`

Format:

```json
{
    "latest": "1.21.4",
    "versions": {
        "1.21.4": "https://cdn.getbukkit.org/spigot/spigot-1.21.4.jar"
    }
}
```

## Run locally

```bash
pip install -r requirements.txt
cd spigot
python main.py
```

## Setup for the auto-update workflow (maintainer notes)

- Repository secret `GIST_TOKEN` — a GitHub token with the `gist` scope.
- Repository variable `GIST_ID_SPIGOT` — the id of the target Gist.

## License

[MIT](../LICENSE)
