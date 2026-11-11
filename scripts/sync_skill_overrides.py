#!/usr/bin/env python3
"""Check or apply version-guarded personal skill overrides to an existing Codex home."""
import argparse
import hashlib
import json
from pathlib import Path
import shutil
import tempfile


def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else None


def contained(root, relative):
    path = (root / relative).resolve()
    if not path.is_relative_to(root.resolve()):
        raise ValueError(f"Path escapes root: {relative}")
    return path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--codex-home', required=True, type=Path)
    parser.add_argument('--apply', action='store_true', help='Apply after validating all base hashes')
    args = parser.parse_args()
    home = args.codex_home.resolve()
    if not home.is_dir():
        parser.error('Codex home must already exist')
    package = Path(__file__).resolve().parents[1] / 'skill-overrides'
    manifest = json.loads((package / 'manifest.json').read_text())
    if manifest['format'] != 1:
        raise ValueError('Unsupported manifest format')
    pending = []
    for entry in manifest['entries']:
        source = contained(package / 'files', entry['path'])
        target = contained(home, entry['path'])
        if digest(source) != entry['after_sha256']:
            raise ValueError(f"Override checksum mismatch: {entry['path']}")
        current = digest(target)
        if current == entry['after_sha256']:
            continue
        if current != entry['before_sha256']:
            raise ValueError(f"Base changed or missing; review before applying: {entry['path']}")
        pending.append((source, target, entry['path']))
    if not args.apply or not pending:
        print(f"Verified {len(manifest['entries'])} files; {len(pending)} pending; no writes")
        return
    backup_root = home / 'backups'
    backup_root.mkdir(exist_ok=True)
    backup = Path(tempfile.mkdtemp(prefix='skill-overrides-', dir=backup_root))
    for source, target, relative in pending:
        if target.exists():
            saved = backup / relative
            saved.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(target, saved)
        target.parent.mkdir(parents=True, exist_ok=True)
        with tempfile.NamedTemporaryFile(dir=target.parent, delete=False) as temp:
            temp.write(source.read_bytes())
            staged = Path(temp.name)
        try:
            if target.exists():
                shutil.copymode(target, staged)
            staged.replace(target)
        finally:
            staged.unlink(missing_ok=True)
    print(f"Applied {len(pending)} files; backup: {backup}")


if __name__ == '__main__':
    main()
