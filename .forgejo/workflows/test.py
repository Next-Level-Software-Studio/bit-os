from pathlib import Path; import sys

import os, shutil
npo_path = Path(os.environ.get("GITHUB_WORKSPACE"))
repos = {
    "gentoo": "https://github.com/gentoo/gentoo.git",
    "npo": "http://nextlevlehng64k4zhaqzu4ulz3jote5xvobsi65dtqvy7bkwra7gzyd.onion/git/Next-Level-Software-Studio/npo.git",
    "steam-overlay": "https://github.com/anyc/steam-overlay.git",
    "torbrowser": ""
}
repos_path = Path("/tmp/repositories")
exclude_packages = ["app-admin/doas::gentoo"]
absolute_exclude_files = [".git", ".editorconfig", ".gitignore", ".gitattributes", ".github", "README.md", "LICENSE", "COPYING", "CHANGELOG.md", ".mailmap", "header.txt", "skel.ebuild", "skel.metadata.xml", "README.txt"]
exclude_files = ["timestamp.chk", "timestamp.commit", "timestamp.x", "timestamp", "Manifest.gz"]
# repo editing
for repo in repos_path.iterdir():
    if repo.is_dir():
        ...

    # final repo version merging
    for item_origem in repo.rglob('*'):
        rel_path = item_origem.relative_to(repo)
        item_destino = npo_path / rel_path
        if item_origem.is_file() and item_destino.exists():
            print(f"Conflito detetado: O ficheiro '{rel_path}' já existe em ambas as pastas.")
            print("A interromper a operação para evitar substituições.")
            sys.exit(1)
    shutil.copytree(repo, npo_path, dirs_exist_ok=True)
    print(f"Pasta {repo.name} mesclada ao repositório com sucesso!")