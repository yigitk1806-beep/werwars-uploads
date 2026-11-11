"""Baut wwdt/plan.json aus katalog.json: pro Kanal ein Video am Tag um 18 Uhr (Europe/Berlin).

Aufruf:  python wwdt/plan_bauen.py [Startdatum JJJJ-MM-TT]
TikTok bekommt alle Videos in REIHENFOLGE_TIKTOK, YouTube nur Videos mit "youtube"-Block (dort noch nicht online).
Bereits geplante Einträge (Datum in der Vergangenheit) bleiben erhalten, neue Videos kommen hinten dran.
"""
import datetime as dt
import json
import sys
from pathlib import Path

HIER = Path(__file__).resolve().parent


class _Berlin(dt.tzinfo):
    """Europe/Berlin ohne tzdata: MEZ +1, MESZ +2 (letzter Sonntag März bis letzter Sonntag Oktober, 1 Uhr UTC)."""
    def _ss(self, jahr, monat):
        tag = max(d for d in range(25, 32) if dt.date(jahr, monat, d).weekday() == 6)
        return dt.datetime(jahr, monat, tag, 1)
    def utcoffset(self, d):
        return dt.timedelta(hours=1) + self.dst(d)
    def dst(self, d):
        if d is None: return dt.timedelta(0)
        n = d.replace(tzinfo=None)
        return dt.timedelta(hours=1) if self._ss(d.year, 3) + dt.timedelta(hours=1) <= n < self._ss(d.year, 10) + dt.timedelta(hours=1) else dt.timedelta(0)
    def tzname(self, d):
        return "MESZ" if self.dst(d) else "MEZ"


BERLIN = _Berlin()
URL = "https://raw.githubusercontent.com/yigitk1806-beep/werwars-uploads/main/wwdt/videos/"
UHRZEIT = {"tiktok": (18, 0), "youtube": (12, 0)}  # YouTube mittags: mehr Klicks (Yusuf, 11.11.2026)
# Stärkste Videos zuerst (nach YouTube-Aufrufen), danach die neuen
REIHENFOLGE_TIKTOK = [2, 18, 16, 11, 12, 26, 14, 4, 17, 19, 7, 1, 21, 15, 22, 13, 27, 6, 23, 3, 5, 9, 28, 20, 10, 24, 25, 29, 8, 31, 30, 32]


def termin(tag: dt.date, kanal: str) -> str:
    return dt.datetime(tag.year, tag.month, tag.day, *UHRZEIT[kanal], tzinfo=BERLIN).isoformat()


def main() -> None:
    kat = {v["nr"]: v for v in json.loads((HIER / "katalog.json").read_text(encoding="utf-8"))["videos"]}
    planf = HIER / "plan.json"
    alt = json.loads(planf.read_text(encoding="utf-8"))["posts"] if planf.exists() else []
    jetzt = dt.datetime.now(BERLIN)
    behalten = list(alt)  # bestehende Termine nie verschieben (könnten schon in Buffer stehen)
    start = dt.date.fromisoformat(sys.argv[1]) if len(sys.argv) > 1 else (jetzt + dt.timedelta(days=1)).date()
    schon = {(p["kanal"], p["nr"]) for p in behalten}
    posts = list(behalten)
    reihe = [n for n in REIHENFOLGE_TIKTOK + [n for n in sorted(kat) if n not in REIHENFOLGE_TIKTOK] if not kat[n].get("schon_auf_tiktok")]
    for kanal, liste in (("tiktok", reihe), ("youtube", [n for n in sorted(kat) if "youtube" in kat[n]])):
        letzte = max([dt.datetime.fromisoformat(p["dueAt"]).date() for p in behalten if p["kanal"] == kanal] + [start - dt.timedelta(days=1)])
        tag = max(start, letzte + dt.timedelta(days=1))
        for n in liste:
            if (kanal, n) in schon:
                continue
            v = kat[n]
            p = {"kanal": kanal, "nr": n, "dueAt": termin(tag, kanal), "video": URL + v["datei"]}
            if kanal == "tiktok":
                p["text"] = v["tiktok"]
            else:
                p.update(title=v["youtube"]["title"], text=v["youtube"]["text"], categoryId=v["youtube"]["categoryId"])
            posts.append(p)
            tag += dt.timedelta(days=1)
    posts.sort(key=lambda p: (p["dueAt"], p["kanal"]))
    planf.write_text(json.dumps({"kanaele": {"tiktok": "kadirsonsuz5", "youtube": "Was würdest du tun?"}, "posts": posts}, ensure_ascii=False, indent=1), encoding="utf-8")
    for k in ("tiktok", "youtube"):
        ps = [p for p in posts if p["kanal"] == k]
        print(k, len(ps), "Posts", ps[0]["dueAt"][:10] if ps else "-", "bis", ps[-1]["dueAt"][:10] if ps else "-")


if __name__ == "__main__":
    main()
