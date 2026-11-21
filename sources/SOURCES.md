# 日本自由行規劃入門｜5篇官方資料來源與Ingest追蹤

- 官方來源核對日期：2026-11-21
- **已建立5篇本地來源摘要：5／5**
- **已編寫完成六章Wiki教學稿：6／6**
- **使用者逐步人工操作與修正的篇數：1／5**（第2～5篇由AI本次直接產出，需繳交前自行檢查）
- 本專案的Ingest指「閱讀官方公開資料→整理成Markdown筆記→編入Wiki→建立本地索引及查核」，**不是聲稱已用課堂專屬工具自動擷取網頁全文**。

| 編號 | 文章與官網網址 | 本地摘要 | Wiki章節 | 資料狀態 |
|---|---|---|---|---|
| S01 | [入境日本與簽證資訊](https://www.japan.travel/tw/plan/visa-info/) | `01-visa-info.md` | `01-preparation.md` | 使用者已逐步執行並回報檢查、修正 |
| S02 | [如何在日本搭火車與巴士旅行](https://www.japan.travel/tw/guide/how-to-travel-by-train-and-bus-in-japan/) | `02-train-bus.md` | `02-transportation.md` | AI已完成摘要與編入Wiki，待使用者複核 |
| S03 | [Accommodation](https://www.japan.travel/en/au/plan/accommodation/) | `03-accommodation.md` | `03-accommodation.md` | AI已完成摘要與編入Wiki，待使用者複核 |
| S04 | [關西三都：京都、奈良與大阪](https://www.japan.travel/tw/itineraries/the-kansai-trio-kyoto-nara-and-osaka/) | `04-kansai-trio.md` | `04-itinerary.md`、`06-kansai-example.md` | AI已完成摘要與編入Wiki，待使用者複核 |
| S05 | [日本旅遊預算指南](https://www.japan.travel/tw/guide/japan-on-a-budget/) | `05-budget.md` | `05-budget.md` | AI已完成摘要與編入Wiki，待使用者複核 |

## 第1篇Ingest操作紀錄（與使用者對話一致）

- [x] 使用者自行開啟日本觀光局第一篇文章並截圖。
- [x] 使用者建立`sources/01-visa-info.md`並截圖。
- [x] 使用者更新`wiki/01-preparation.md`並截圖。
- [x] 因停留期限措辭過於籠統，使用者修正15、30、90、180天的適用差異並截圖。
- [x] 使用者修改第1篇Ingest處理紀錄並截圖。
- [x] 本交付包已同步總表與最新的Markdown內容。

## 第2～5篇本次自動製作的文件

- [x] 資料02：摘要＋Wiki正文已製作
- [x] 資料03：摘要＋Wiki正文已製作
- [x] 資料04：摘要＋Wiki正文已製作
- [x] 資料05：摘要＋Wiki正文已製作
- [ ] 使用者實際在Windows驗證、重新跑Ingest索引並截圖

## 重複使用的檢查步驟

1. 檢查文章的官方網址與主題是否相符。
2. 對照本地摘要與Wiki，判斷事實、解釋及示範是否有混淆。
3. 對可能改變的資訊標註「需重新確認」。
4. 產生或更新 `data/ingest_index.json`；對照索引中5項完整存在。
5. 若查核不通過，返回來源摘要或Wiki修訂，再重新檢查。
