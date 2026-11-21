#!/usr/bin/env python3
"""Local curated-notes ingest. No web crawling, model calls, or automatic Wiki rewriting.

Rebuilds a traceable index over five source-note Markdown files and their Wiki targets.
Run in project root: python tools/ingest.py
"""
from __future__ import annotations
import hashlib, json, re
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
SOURCES = [
    ('S01','01-visa-info.md','01-preparation.md','https://www.japan.travel/tw/plan/visa-info/','人工操作並修正（使用者回報）'),
    ('S02','02-train-bus.md','02-transportation.md','https://www.japan.travel/tw/guide/how-to-travel-by-train-and-bus-in-japan/','AI產生整理稿；待使用者逐項複核'),
    ('S03','03-accommodation.md','03-accommodation.md','https://www.japan.travel/en/au/plan/accommodation/','AI產生整理稿；待使用者逐項複核'),
    ('S04','04-kansai-trio.md','04-itinerary.md','https://www.japan.travel/tw/itineraries/the-kansai-trio-kyoto-nara-and-osaka/','AI產生整理稿；待使用者逐項複核'),
    ('S05','05-budget.md','05-budget.md','https://www.japan.travel/tw/guide/japan-on-a-budget/','AI產生整理稿；待使用者逐項複核'),
]
def digest(text: str) -> str:
    return hashlib.sha256(text.encode('utf-8')).hexdigest()
def main():
    records=[]
    for ident, src, wiki, url, status in SOURCES:
        sp=ROOT/'sources'/src; wp=ROOT/'wiki'/wiki
        if not sp.is_file(): raise SystemExit(f'缺少摘要檔：{sp}')
        if not wp.is_file(): raise SystemExit(f'缺少Wiki檔：{wp}')
        source=sp.read_text(encoding='utf-8'); page=wp.read_text(encoding='utf-8')
        if url not in source or url not in page: raise SystemExit(f'{ident}來源網址或Wiki連結缺失')
        if len(source)<350 or len(page)<500: raise SystemExit(f'{ident}正文可能缺失')
        title=source.splitlines()[0].lstrip('# ').strip()
        records.append({'id':ident,'title':title,'source_note':f'sources/{src}',
            'wiki_page':f'wiki/{wiki}','official_url':url,'checked_on':'2026-11-21',
            'note_sha256':digest(source),'wiki_sha256':digest(page),'note_chars':len(source),
            'status':status,'method':'官方網頁重點原創摘要→本地Wiki；非官方全文下載'})
        print(f'OK {ident} → wiki/{wiki} ({len(source)} chars in source note)')
    result={'project':'日本自由行規劃入門','method':'curated-notes local ingest, not full-text web crawl',
        'source_count':len(records),'wiki_chapters':6,'source_check_date':'2026-11-21',
        'records':records}
    target=ROOT/'data'/'ingest_index.json'; target.parent.mkdir(exist_ok=True)
    target.write_text(json.dumps(result,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
    print(f'INDEX COMPLETE: {len(records)}/5 sources → {target.relative_to(ROOT)}')
if __name__=='__main__': main()
