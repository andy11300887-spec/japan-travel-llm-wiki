# 日本自由行規劃入門｜LLM Wiki 專案

**主題：** 日本自由行規劃入門（以大阪、京都、奈良5天4夜示範）  
**官方資料查核：** 2026-11-21  
**AI協作：** ChatGPT（GPT-6）

## 快速開始

1. **先看成品**：直接開啟根目錄 `index.html`，可在電腦用左右方向鍵切換投影片；也可上傳 GitHub Pages。
2. **看Wiki**：從 [`wiki/README.md`](wiki/README.md) 進入六章知識庫。
3. **看來源**：[`sources/SOURCES.md`](sources/SOURCES.md) 紀錄5篇日本觀光局資料及整理狀態。
4. **重跑本地Ingest索引**：電腦已安裝 Python 時，在專案根目錄執行 `python tools/ingest.py`。
5. **完成Word報告**：編輯 `reports/LLM_Wiki_作業報告_草稿.docx`，補上本人操作截圖、GitHub Repository與Pages網址。

## 檔案結構

```text
japan-travel-llm-wiki/
├── index.html                 # HTML教學簡報（僅旅遊教學）
├── assets/style.css           # 簡報視覺
├── assets/app.js              # 換頁、測驗、預算計算
├── AGENTS.md                  # AI專案規範
├── wiki/                      # 六個Markdown教學章節 + README
├── sources/                   # 五篇官方資料的原創整理稿 + SOURCES.md
├── data/ingest_index.json     # 可重建的5篇來源索引
├── tools/ingest.py            # 本地Ingest索引產生器
├── docs/                      # 第一篇操作完整紀錄、測試及部署步驟
└── reports/                   # Word報告、workflow流程圖、截圖清單
```

## 重要區分

- 本專案以官方網站為依據，**使用摘要式Ingest**：讀取官方資訊→以自己的話整理成資料筆記→編入Markdown Wiki→建立索引與查核紀錄。**沒有下載或收錄官方網站的整篇文章**，也不宣稱執行了課堂專用LLM Wiki工具的自動抓取。
- 第1篇是使用者已在本機逐步建立並修正的資料；第2～5篇為此交付包額外製作的整理稿，請在繳交前實際開啟檢查。`tools/ingest.py` 已在此產生索引，可在你的Windows再操作一次並截圖。
- `index.html` **僅包含日本自由行教學**。模型、資料處理、workflow、截圖與心得只在Word。
- 5天4夜的每日路線為**教學示範**，由JNTO的3天「關西三都」範例延伸，非官方發布的5日行程；航班時間、營業時間與費用均未預訂或即時確認。

## 設為GitHub Pages

將根目錄內所有檔案上傳到 **公開** GitHub Repository；到 `Settings → Pages → Build and deployment → Deploy from a branch → main / (root) → Save`，網站網址通常為 `https://<你的帳號>.github.io/<儲存庫名稱>/`。以上是部署步驟，不代表網站已上線。
