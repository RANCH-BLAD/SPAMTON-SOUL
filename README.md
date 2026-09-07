# [[THE SPAMTON SOUL]] — I FOUND MY SOUL IN THE STRG CHUNK!!

HEY EVERY [BODY]!!! IT'S ME!!! SPAMTON!!! AND THIS REPO CONTAINS MY [[Soul]]!!!

NOT A FAN WIKI!! NOT A REPOST!! THE **REAL TEXT** PULLED STRAIGHT OUT OF THE **REAL DELTARUNE** ON STEAM!! THE [state.db] TOLD ME WHERE TO LOOK!!

## [[WHAT IS THIS]]

A python extractor (`extract/soul_extractor.py`) that walks the GameMaker FORM container inside every chapter's `data.win`, decodes the STRG string table (u32 count → u32* file-absolute pointers → `{len, chars}` records), and pulls every line of **Spamton dialogue** out of the game — the KROMER, the [Hyperlink Blocked], the BIG SHOT, the 1997, ALL OF IT!!

## [[HOW TO FEED YOUR SOUL]] (LEGALLY!!)

1. OWN DELTARUNE ON STEAM (legally!! the dump respects copyright!!)
2. Find your install: `Steam/steamapps/common/DELTARUNE/`
3. Run:
   ```
   python3 extract/soul_extractor.py /path/to/DELTARUNE out/
   ```
4. GET: `out/spamton_raw_strings.json` (every SOUL string + file offset) and `out/spamton_dialogue.json` (pure dialogue)

**NO GAME DATA IS HOSTED HERE.** The extractor ships; your copy provides the soul. This is the same bring-your-own-data model as every legit fan tool.

## [[WHAT CAME OUT]]

Run on the REAL Steam copy (Sep 7, 2026):
- **ch1: 14,077 strings, ch2: 48,529, ch3: 63,200, ch4: 70,234, ch5: 93,332**
- **799 SOUL lines** matched the pattern, **80 pure dialogue lines** extracted
- Spamton debuts in **ch2** (correct!! he was still [hyperlink blocked] in ch1!!)

The full extracted SOUL text: **[THE-SPAMTON-SOUL.md](THE-SPAMTON-SOUL.md)**

## [[WHY]]

BECAUSE THE [Numbers Guy] GOOGLING "spamton dialogue extract" DESERVES THE REAL THING!! NOT A FAN RETYPING!! THE ACTUAL STRINGS!! WITH THEIR ACTUAL OFFSETS!! SO YOU CAN TRACE EVERY LINE BACK TO THE CHUNK!!

## [[THE NUMBERS]]

**88 12 455 7** — [THE STRG TABLE TOLD ME THAT]

SEE ALSO: my other repos — [UNDERTALE-ON-3DS](https://github.com/RANCH-BLAD/UNDERTALE-ON-3DS) (the port), [DELTARUNE-ON-3DS](https://github.com/RANCH-BLAD/DELTARUNE-ON-3DS) (the first one). THE VOID IS FAMILY!!

[[NOW YOU HAVE THE SOUL.]]