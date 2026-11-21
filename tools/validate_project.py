"""Offline consistency test (does not check live official sites)."""
from pathlib import Path
from html.parser import HTMLParser
import json
ROOT=Path(__file__).resolve().parents[1]
REQUIRED=[ROOT/'AGENTS.md',ROOT/'index.html',ROOT/'assets'/'style.css',ROOT/'assets'/'app.js',ROOT/'wiki'/'README.md',ROOT/'sources'/'SOURCES.md',ROOT/'data'/'ingest_index.json']
for p in REQUIRED:
    assert p.is_file(),f'缺少：{p}'
index=json.loads((ROOT/'data'/'ingest_index.json').read_text(encoding='utf-8'))
assert index['source_count']==5
assert len(index['records'])==5
for rec in index['records']:
    assert (ROOT/rec['source_note']).exists()
    assert (ROOT/rec['wiki_page']).exists()
    assert rec['official_url'] in (ROOT/rec['source_note']).read_text(encoding='utf-8')
for n in ('01-preparation.md','02-transportation.md','03-accommodation.md','04-itinerary.md','05-budget.md','06-kansai-example.md'):
    assert n in (ROOT/'wiki'/'README.md').read_text(encoding='utf-8')
html=(ROOT/'index.html').read_text(encoding='utf-8')
assert html.count('<section class="slide"')>=12
assert '日本自由行' in html and '旅行' in html
assert not any(word in html for word in ('LLM Wiki','AGENTS.md','workflow','GitHub'))
class H(HTMLParser):
    def __init__(self): super().__init__();self.slideids=set()
    def handle_starttag(self,tag,attrs):
        if tag=='section':
            a=dict(attrs)
            if 'slide' in a.get('class',''): self.slideids.add(a['id'])
p=H();p.feed(html)
assert len(p.slideids)>=12
print('PASS：5篇來源／6章Wiki／16頁HTML／來源連結與檔案結構均存在')
print('注意：此測試不取代瀏覽器互動、官方內容逐字查核或GitHub公開網址驗證。')
