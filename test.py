from pathlib import Path; import sys

import os, shutil
npo_path = Path(os.environ.get("GITHUB_WORKSPACE"))

repos_path = Path("/tmp/repositories")
data = {
    "gentoo": {"rename": [("app-admin/doas", "app-admin/open-doas")], }
}
# repo editing
for repo in repos_path.iterdir():
    if repo.is_dir():
        #apagar ficheiros desnecessários
        with open(f"/tmp/repositories/{repo.name}/timestamp-commit", "r") as g:
            commit_hash = g.read().strip()
        repo_msg = "Below is the content from "
        path_delete = [Path(repo / "profiles" / "repo_name")]
        keeps = [gitkeep for gitkeep in repo.rglob(".gitkeep")]
        trash = [trash for nome in ("timestamp.chk", "timestamp.commit", "timestamp.x", "timestamp", "Manifest.gz") for trash in repo.rglob(nome)]
        lixo = path_delete + keeps + trash
        para_deletação = [".git", ".editorconfig", ".gitignore", ".gitattributes", ".github", "README.md", "LICENSE", "COPYING", "CHANGELOG.md", ".mailmap", "header.txt", "skel.ebuild", "skel.metadata.xml", "README.txt"]
        for item in para_deletação:
            item_path = repo / item
            if item_path.exists():
                if item_path.is_dir():
                    for sub_item in item_path.rglob("*"):
                        sub_item.unlink()
                    item_path.rmdir()
                else:
                    item_path.unlink()
            else:
                pass
        for i in lixo:
            if i.exists():
                i.unlink(missing_ok=True)
        for i in path_delete:
            i.unlink(missing_ok=True)

        # data variable repo edits
        #rename
        for i in data.get(key=repo.name).get(key="rename"):
            antiga_pasta = Path(repo / i[1])
            novo_nome = str(repo / i[2])
            antiga_pasta.rename(novo_nome)
        #

        # /profiles/profiles.desc merging
        with open(Path(repo / "profiles" / "profiles.desc"), "r") as file:
            l = file.read()
        with open(Path(npo_path / "profiles" / "profiles.desc"), "a") as file:
            file.write("")
            file.write(l)
        
        

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