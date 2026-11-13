"""Erzeugt wwdt/warteschlange.json fuer die Cloud-Routine 'Buffer nachfuellen'."""
import json, pathlib

LA = "\n\nUnd lass ein Like und ein Abo da – das würde mir echt helfen!"
alt = json.load(open(pathlib.Path(__file__).with_name("warteschlange.json"), encoding="utf-8"))
E = alt["eintraege"][:6]  # Fr–So (bereits festgelegt)

def yt(due, datei, titel, text):
    E.append({"kanal": "youtube", "dueAt": due, "datei": datei, "titel": titel, "text": text})

def tt(due, datei, text):
    E.append({"kanal": "tiktok", "dueAt": due, "datei": datei, "text": text})

# Du entscheidest: (nr, datei, titel, beschreibung, hashtags, tiktok-frage)
DE = {
 2: ("55-du-entscheidest-2-unsichtbar-oder-gedanken.mp4", "Unsichtbar sein oder Gedanken lesen? Du entscheidest! #shorts",
     "A: Unsichtbar. B: Gedanken lesen. Was nimmst du? Schreib A oder B in die Kommentare.", "#duentscheidest #unsichtbar #gedankenlesen #aoderb #wuerdestdu #shorts", "Unsichtbar sein oder Gedanken lesen?"),
 3: ("56-du-entscheidest-3-reich-oder-freunde.mp4", "Reich ohne Freunde oder arm mit echten Freunden? Du entscheidest! #shorts",
     "A: reich, aber ohne Freunde. B: arm, aber mit echten Freunden. Was nimmst du? Schreib A oder B in die Kommentare.", "#duentscheidest #aoderb #wuerdestdu #freunde #geld #shorts", "Reich ohne Freunde oder arm mit echten Freunden?"),
 4: ("57-du-entscheidest-4-jung-oder-millionen.mp4", "10 Jahre jünger oder 10 Millionen Euro? Du entscheidest! #shorts",
     "A: zehn Jahre jünger. B: zehn Millionen Euro. Was nimmst du? Schreib A oder B in die Kommentare.", "#duentscheidest #aoderb #wuerdestdu #millionen #shorts", "10 Jahre jünger oder 10 Millionen Euro?"),
 5: ("58-du-entscheidest-5-villa-oder-reisen.mp4", "Traumvilla oder jeden Tag um die Welt reisen? Du entscheidest! #shorts",
     "A: deine Traumvilla. B: jeden Tag ein neues Land. Was nimmst du? Schreib A oder B in die Kommentare.", "#duentscheidest #aoderb #wuerdestdu #reisen #traumhaus #shorts", "Traumvilla oder jeden Tag reisen?"),
 6: ("59-du-entscheidest-6-vergangenheit-oder-zukunft.mp4", "Vergangenheit ändern oder Zukunft sehen? Du entscheidest! #shorts",
     "A: Vergangenheit ändern. B: Zukunft sehen. Was nimmst du? Schreib A oder B in die Kommentare.", "#duentscheidest #aoderb #wuerdestdu #zeitreise #shorts", "Vergangenheit ändern oder Zukunft sehen?"),
 7: ("60-du-entscheidest-7-ewig-25-oder-150.mp4", "Für immer 25 oder 150 Jahre leben? Du entscheidest! #shorts",
     "A: für immer 25. B: 150 Jahre leben. Was nimmst du? Schreib A oder B in die Kommentare.", "#duentscheidest #aoderb #wuerdestdu #shorts", "Für immer 25 oder 150 Jahre leben?"),
 8: ("61-du-entscheidest-8-arbeiten-oder-millionen.mp4", "Nie wieder arbeiten oder 100 Millionen Euro? Du entscheidest! #shorts",
     "A: nie wieder arbeiten, aber nur genug zum Leben. B: 100 Millionen, aber du arbeitest weiter. Schreib A oder B in die Kommentare.", "#duentscheidest #aoderb #wuerdestdu #arbeit #millionen #shorts", "Nie wieder arbeiten oder 100 Millionen Euro?"),
 9: ("62-du-entscheidest-9-million-oder-identitaet.mp4", "1 Million Euro, aber du verlierst deine Identität? Du entscheidest! #shorts",
     "A: die Million mit neuem Namen und neuem Leben. B: du bleibst du. Schreib A oder B in die Kommentare.", "#duentscheidest #aoderb #wuerdestdu #shorts", "1 Million Euro, aber du verlierst deine Identität?"),
 10: ("63-du-entscheidest-10-geld-oder-helfen.mp4", "100.000 € für dich oder einem Fremden helfen? Du entscheidest! #shorts",
     "A: das Geld für dich. B: einem Fremden helfen, der es dringend braucht. Schreib A oder B in die Kommentare.", "#duentscheidest #aoderb #wuerdestdu #helfen #shorts", "100.000 € für dich oder einem Fremden helfen?"),
 11: ("64-du-entscheidest-11-millionen-oder-liebe.mp4", "10 Millionen Euro, aber nie wieder verliebt? Du entscheidest! #shorts",
     "A: zehn Millionen, nie wieder verliebt. B: die Liebe behalten. Schreib A oder B in die Kommentare.", "#duentscheidest #aoderb #wuerdestdu #liebe #shorts", "10 Millionen Euro, aber nie wieder verliebt?"),
}

def de_yt(due, n):
    d, t, b, h, _ = DE[n]
    yt(due, d, t, b + " Ich zähle eure Stimmen mit." + LA + "\n\n" + h)

def de_tt(due, n):
    d, *_, frage = DE[n]
    tt(due, d, f"{frage} Du entscheidest! 👇 Schreib A oder B\n\n#duentscheidest #aoderb #waswürdestdutun #fürdich")

G1 = ("51-iphone-oder-samsung-updates.mp4", "iPhone oder Samsung: Wer gibt dir länger Updates? #shorts",
      "iPhone oder Samsung – wer hält dein Handy länger sicher? Samsung verspricht bei der Galaxy S25 sieben Jahre Updates, Apple nennt keine Zahl. Schreib in die Kommentare, welches Handy du hast!" + LA +
      "\n\nQuellen: heise.de, teltarif.de, netzwelt.de (Galaxy S25: 7 Jahre Updates); techbook, macwelt, heise (iOS 26 ohne iPhone XS/XR); EU-Ökodesign-Verordnung (EU) 2023/1670. Kein Kaufrat, keine Werbung.\n\n#Shorts #iPhone #Samsung #Updates #Technik")
G2 = ("52-katze-oder-hund.mp4", "Katze oder Hund: Wer gewinnt bei den Zahlen? #shorts",
      "Katze oder Hund – wer gewinnt, wenn man nur die Zahlen fragt? Beliebtheit, Kosten und Steuer im Vergleich. Welches Tier gewinnt bei dir? Schreib es in die Kommentare!" + LA +
      "\n\nQuellen: IVH/ZZF „Der deutsche Heimtiermarkt 2025“; Deutscher Tierschutzbund; Berliner Sparkasse. Kostenangaben sind Schätzungen. Kein Tierarzt-Rat.\n\n#Shorts #Katze #Hund #Haustiere #Vergleich")
G3 = ("53-playstation-oder-xbox.mp4", "PlayStation oder Xbox: Wer hat mehr verkauft? #shorts",
      "PlayStation oder Xbox – wer hat mehr Konsolen verkauft? Und wer nennt seine Zahlen überhaupt? Welche Konsole hast du? Schreib es in die Kommentare!" + LA +
      "\n\nQuellen: Sony-Quartalsbericht (PS5 rund 95,3 Mio. bis 30.06.2026, berichtet von Gematsu, Thurrott, Push Square); Microsoft (über 21 Mio., 2024); VGChartz-Schätzung laut Pure Xbox. Ausgeliefert ist nicht gleich verkauft. Keine Werbung.\n\n#Shorts #PlayStation #Xbox #Gaming #Vergleich")
G7 = ("54-kaffee-gegen-energy-teil-20.mp4", "Kaffee gegen Energy: 3 Runden, 1 Punkt ☕ Teil 20 #shorts",
      "Kaffee gegen Energy-Drink in drei Runden: Koffein, Zucker, Jugendliche. Endstand 1:0 für den Kaffee – aber nur schwarz. Team Kaffee oder Team Energy? Schreib es in die Kommentare." + LA +
      "\n\nQuellen: BfR (Koffeingehalte, Jugendliche höchstens 3 mg pro kg Körpergewicht); Stiftung Warentest (rund 27 g Zucker pro 250 ml); WHO (höchstens 25 g freier Zucker pro Tag).\n\n#kaffee #energydrink #koffein #gegeneinander #fakten #shorts")

# YouTube So 20:30 und ab Mo 23.11. taeglich 18:00 (16.–22.11. belegt die andere Sitzung)
de_yt("2026-11-15T20:30:00+01:00", 3)
plan = [4, G1, 2, G3, 5, G2, 6, 7, 8, 9, 10, 11, G7]
tage = ["2026-11-23", "2026-11-24", "2026-11-25", "2026-11-26", "2026-11-27", "2026-11-28", "2026-11-29",
        "2026-11-30", "2026-12-01", "2026-12-02", "2026-12-03", "2026-12-04", "2026-12-05"]
for tag, x in zip(tage, plan):
    due = f"{tag}T18:00:00+01:00"
    de_yt(due, x) if isinstance(x, int) else yt(due, *x)

# TikTok 19:00 an freien Tagen
tt("2026-11-16T19:00:00+01:00", "45-zucker-oder-suessstoff-teil-14.mp4", "Zucker oder Süßstoff – wer verliert? 🍬 Teil 14 👇\n\n#waswürdestdutun #süßstoff #zucker #fakten #fürdich")
tt("2026-11-19T19:00:00+01:00", "49-zigarette-gegen-vape-teil-17.mp4", "Zigarette gegen Vape: 5 Runden, 1 Sieger? 🚬 Teil 17 👇\n\n#waswürdestdutun #zigarette #vape #fakten #fürdich")
tt("2026-11-20T19:00:00+01:00", "48-shisha-oder-zigarette-teil-18.mp4", "Shisha oder Zigarette – was ist wirklich schlimmer? 💨 Teil 18 👇\n\n#waswürdestdutun #shisha #zigarette #fakten #fürdich")
tt("2026-11-21T19:00:00+01:00", "50-tabakerhitzer-oder-zigarette-teil-19.mp4", "Tabakerhitzer oder Zigarette – ist Erhitzen wirklich besser? Teil 19 👇\n\n#waswürdestdutun #tabakerhitzer #zigarette #fakten #fürdich")
for tag, n in [("2026-11-22", 3), ("2026-11-24", 4), ("2026-11-25", 2), ("2026-11-26", 5), ("2026-11-27", 6),
               ("2026-11-28", 7), ("2026-11-29", 8), ("2026-11-30", 9), ("2026-12-01", 10), ("2026-12-02", 11)]:
    de_tt(f"{tag}T19:00:00+01:00", n)

alt["eintraege"] = E
json.dump(alt, open(pathlib.Path(__file__).with_name("warteschlange.json"), "w", encoding="utf-8"), ensure_ascii=False, indent=2)
print(len(E), "Eintraege")
