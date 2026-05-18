"""Create a public GitHub gist from a directory of files.

Usage:
    python create_gist.py <staging_dir> <description>

Reads token from `git credential fill` for github.com.
Prints the html_url + raw URLs of created files.
"""
import json
import os
import subprocess
import sys
from pathlib import Path
from urllib import request


def get_token() -> str:
    p = subprocess.run(
        ["git", "credential", "fill"],
        input="protocol=https\nhost=github.com\n\n",
        capture_output=True,
        text=True,
        check=True,
    )
    for line in p.stdout.splitlines():
        if line.startswith("password="):
            return line[len("password="):]
    raise RuntimeError("No token in git credential output")


def create_gist(staging_dir: Path, description: str, token: str) -> dict:
    files = {}
    for f in sorted(staging_dir.iterdir()):
        if f.is_file():
            files[f.name] = {"content": f.read_text(encoding="utf-8")}
    body = json.dumps({
        "description": description,
        "public": True,
        "files": files,
    }).encode("utf-8")
    req = request.Request(
        "https://api.github.com/gists",
        data=body,
        method="POST",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "Bmad82-coda",
            "Content-Type": "application/json",
        },
    )
    with request.urlopen(req) as resp:
        if resp.status != 201:
            raise RuntimeError(f"Gist creation failed: {resp.status}")
        return json.loads(resp.read().decode("utf-8"))


def update_gist(gist_id: str, files: dict, token: str) -> dict:
    body = json.dumps({"files": {k: {"content": v} for k, v in files.items()}}).encode("utf-8")
    req = request.Request(
        f"https://api.github.com/gists/{gist_id}",
        data=body,
        method="PATCH",
        headers={
            "Authorization": f"Bearer {token}",
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "Bmad82-coda",
            "Content-Type": "application/json",
        },
    )
    with request.urlopen(req) as resp:
        if resp.status not in (200, 201):
            raise RuntimeError(f"Gist update failed: {resp.status}")
        return json.loads(resp.read().decode("utf-8"))


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print("Usage: python create_gist.py <staging_dir> <description>", file=sys.stderr)
        sys.exit(1)
    staging = Path(sys.argv[1])
    desc = sys.argv[2]
    token = get_token()
    result = create_gist(staging, desc, token)
    print(f"HTML_URL={result['html_url']}")
    print(f"ID={result['id']}")
    print(f"DESC={result['description']}")
    print(f"PUBLIC={result['public']}")
    for fname, fdata in result["files"].items():
        print(f"FILE_RAW: {fname} -> {fdata['raw_url']}")
