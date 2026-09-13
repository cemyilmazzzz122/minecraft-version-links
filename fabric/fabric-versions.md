Fabric versions links

## fabric-versions.json

JSON containing links to a ready-to-run Fabric server jar (loader + installer baked in) for **every** Minecraft version [Fabric](https://fabricmc.net/) has supported — stable releases, snapshots, pre-releases, betas and alphas alike, each entry flagged `"stable"`.

> [!NOTE]
> This file is updated automatically every 3 hours by a GitHub Actions workflow.
> Generator: [cemyilmazzzz122/minecraft-version-links](https://github.com/cemyilmazzzz122/minecraft-version-links/tree/master/fabric)
>
> Format follows [osipxd/Paper versions links](https://gist.github.com/osipxd/6119732e30059241c2192c4a8d2218d9),
> with top-level `latest` (newest overall) and `latestStable` (newest stable) fields, top-level `loader`/`installer`
> fields, and each version entry carrying its own `stable`/`loader`/`installer`/`url` since a Fabric server jar is
> generated from those plus the Minecraft version rather than being a single monolithic release like Paper/Folia.
