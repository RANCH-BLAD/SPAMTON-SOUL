#!/usr/bin/env python3
"""
[[THE SOUL EXTRACTOR]] — pulls the REAL Spamton text out of a REAL DELTARUNE install.
Bring your own legally-obtained copy (Steam). No game data shipped here — only the extractor.
Usage:  python3 soul_extractor.py /path/to/DELTARUNE  [out_dir]
Walks each chapter's data.win FORM container, decodes the STRG string table
(u32 count, u32* file-absolute pointers, records = {len, chars}), greps the SOUL pattern.
"""
import struct, json, re, sys, os

PATTERN = re.compile(
    r'Kromer|yperlink|BIG SHOT|Little Sponge|1997|PAMTON|SPAMTON|Heaven|\[\[', re.I)
DIALOGUE = re.compile(r'^\s*\*|^\s*\\M|\[Hyperlink')

def walk_chunks(data):
    p2, out = 8, {}
    while p2 + 8 <= len(data):
        nm = data[p2:p2+4].decode('latin1')
        sz = struct.unpack('<I', data[p2+4:p2+8])[0]
        out[nm] = (p2 + 8, sz)
        p2 += 8 + sz
        if sz % 4:
            p2 += 4 - (sz % 4)
    return out

def extract_strings(data):
    so, ss = walk_chunks(data)['STRG']
    cnt = struct.unpack_from('<I', data, so)[0]
    ptrs = struct.unpack_from(f'<{cnt}I', data, so + 4)
    out = []
    for o in ptrs:
        n = struct.unpack_from('<I', data, o)[0]
        if 1 <= n <= 4000 and o + 4 + n <= len(data):
            try:
                out.append((o, data[o+4:o+4+n-1].decode('utf-8')))
            except UnicodeDecodeError:
                pass
    return out

def main():
    base = sys.argv[1] if len(sys.argv) > 1 else '.'
    outdir = sys.argv[2] if len(sys.argv) > 2 else 'extract'
    os.makedirs(outdir, exist_ok=True)
    all_hits, dialogue = {}, {}
    for ch in range(1, 6):
        p = os.path.join(base, f'chapter{ch}_windows', 'data.win')
        if not os.path.exists(p):
            print(f'chapter {ch}: no data.win, skipping')
            continue
        strs = extract_strings(open(p, 'rb').read())
        print(f'chapter {ch}: {len(strs)} strings decoded')
        hits = [{'offset': o, 'text': s} for o, s in strs if PATTERN.search(s)]
        all_hits[f'ch{ch}'] = hits
        dialogue[f'ch{ch}'] = [e for e in hits
                               if DIALOGUE.search(e['text'])]
    json.dump(all_hits, open(os.path.join(outdir, 'spamton_raw_strings.json'), 'w'),
              ensure_ascii=False, indent=1)
    json.dump(dialogue, open(os.path.join(outdir, 'spamton_dialogue.json'), 'w'),
              ensure_ascii=False, indent=1)
    total = sum(len(v) for v in all_hits.values())
    dt = sum(len(v) for v in dialogue.values())
    print(f'SOUL LINES: {total} raw / {dt} dialogue — saved to {outdir}/')

if __name__ == '__main__':
    main()