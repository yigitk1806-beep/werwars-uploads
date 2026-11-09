"""Neue Videos für „Was würdest du tun?“ automatisch einplanen.

Ablauf: Lege fertige Videos nach D:\\Projekte\\hf-videos\\_AUTO-UPLOAD
  - <name>.mp4                 das Video (mit Logo und Like/Abo-Ende)
  - <name>.json  (optional)    {"tiktok": "...", "youtube": {"title": "...", "text": "...", "categoryId": "27"}}
                               ohne "youtube" geht es nur auf TikTok (z. B. wenn schon auf YouTube online)
Dann einplanen.bat doppelklicken. Das Skript
  1. kopiert jedes Video ins Repo (wwdt/videos), trägt es in katalog.json ein,
  2. hängt es im Plan hinten an (täglich 18 Uhr, je Kanal),
  3. lädt alles auf GitHub hoch und verschiebt die Dateien nach _AUTO-UPLOAD\\hochgeladen.
Die tägliche Routine (7 Uhr) übernimmt den Rest in Buffer.
"""
import json
import re
import shutil
import subprocess
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")
HIER = Path(__file__).resolve().parent
REPO = HIER.parent
EINGANG = Path(r"D:\Projekte\hf-videos\_AUTO-UPLOAD")
FERTIG = EINGANG / "hochgeladen"
STANDARD = "{titel} 👇\n\n#waswürdestdutun #wusstestdu #fakten #fürdich"


def slug(s: str) -> str:
    s = s.lower().replace("ä", "ae").replace("ö", "oe").replace("ü", "ue").replace("ß", "ss")
    return re.sub(r"[^a-z0-9]+", "-", s).strip("-")[:60]


def main() -> int:
    EINGANG.mkdir(parents=True, exist_ok=True)
    FERTIG.mkdir(exist_ok=True)
    neu = sorted(EINGANG.glob("*.mp4"))
    if not neu:
        print("Keine neuen Videos in", EINGANG)
        return 0
    katf = HIER / "katalog.json"
    kat = json.loads(katf.read_text(encoding="utf-8"))
    nr = max(v["nr"] for v in kat["videos"]) + 1
    for mp4 in neu:
        if mp4.stat().st_size > 95 * 1024 * 1024:
            print("ZU GROSS (über 95 MB), übersprungen:", mp4.name)
            continue
        meta_f = mp4.with_suffix(".json")
        meta = json.loads(meta_f.read_text(encoding="utf-8")) if meta_f.exists() else {}
        titel = re.sub(r"^\d+\s*", "", mp4.stem)
        datei = f"{nr:02d}-{slug(titel)}.mp4"
        shutil.copy2(mp4, HIER / "videos" / datei)
        eintrag = {"nr": nr, "datei": datei, "tiktok": meta.get("tiktok") or STANDARD.format(titel=titel)}
        if meta.get("youtube"):
            eintrag["youtube"] = meta["youtube"]
        kat["videos"].append(eintrag)
        print(f"+ {nr:02d} {titel}  (TikTok{' + YouTube' if 'youtube' in eintrag else ''})")
        nr += 1
    katf.write_text(json.dumps(kat, ensure_ascii=False, indent=1), encoding="utf-8")
    subprocess.run([sys.executable, "-I", str(HIER / "plan_bauen.py")], check=True)
    subprocess.run(["git", "add", "wwdt"], cwd=REPO, check=True)
    subprocess.run(["git", "commit", "-q", "-m", "wwdt: neue Videos eingeplant"], cwd=REPO, check=True)
    r = subprocess.run(["git", "push", "-q", "origin", "main"], cwd=REPO)
    if r.returncode:
        print("FEHLER beim Hochladen zu GitHub – Dateien bleiben im Eingang.")
        return 1
    for mp4 in neu:
        for f in (mp4, mp4.with_suffix(".json")):
            if f.exists():
                shutil.move(str(f), FERTIG / f.name)
    print("Fertig. Die Routine plant morgen früh in Buffer ein.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
