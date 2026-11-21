# Windows最快完成作業：操作說明

## A. 先確認HTML成品
1. 將ZIP解壓縮，打開 `japan-travel-llm-wiki` 資料夾。
2. **雙擊 `index.html`**，在Chrome或Edge開啟；右下角「下一頁」或方向鍵可以換頁。
3. 到「預算練習」修改金額，檢查總計會變；「小測驗」選答案後按檢查。
4. 截圖：簡報首頁、關西5日行程頁、預算輸入結果（放Word第二部分）。

## B. 確認5篇Ingest索引
1. 在資料夾內點一下路徑列，輸入 `cmd` 按Enter（開啟命令提示字元）。
2. 輸入 `python tools\ingest.py` 並按Enter。若Windows顯示找不到Python，先安裝Python或在有Python的電腦操作。
3. 畫面應出現 `OK S01` 至 `OK S05`，最後出現 `INDEX COMPLETE: 5/5`。
4. 再輸入 `python tools\validate_project.py`，檢查是否顯示 `PASS`。
5. 截圖命令視窗與`sources/SOURCES.md`：這個證據顯示本地摘要實際被工具讀取和建立索引；**不等於官方全文網路爬取**。

## C. 更新Word報告
1. 開啟 `reports/LLM_Wiki_作業報告_草稿.docx`。
2. 填入學號、班級、姓名；插入**你實際保留的**AI討論與操作截圖。
3. GitHub公開倉庫與Pages網址只有部署成功後才能填寫。
4. 注意報告中的未完成驗證提醒；不要把AI生成的第2～5篇誤寫成你逐篇親自操作。

## D. 上傳GitHub Pages
1. 登入GitHub，新增Public repository，建議名稱 `japan-travel-llm-wiki`。
2. `Add file → Upload files`，把解壓縮後**專案資料夾內的檔案和資料夾**全部上傳到儲存庫根目錄（不是再包一層資料夾）。
3. 按 `Commit changes`。
4. 到儲存庫 `Settings → Pages → Build and deployment → Deploy from a branch`，選 `main` 與 `/(root)`，按 `Save`。
5. 等GitHub顯示Pages網址後，**親自開啟連結測試**手機/電腦、換頁、預算、測驗；把Repository和Pages網址貼進Word。

## E. 最後檢查
- 網頁只包含日本旅遊教學，沒有AI討論或workflow等報告內容。
- 官方原始網址可點擊；可變動資訊有提醒查核。
- Word中附模型名稱（ChatGPT GPT-6）、來源、架構、截圖、flow圖、loop說明、真實反思及心得。
- 截圖必須是你實際做過的操作，不能用偽造的終端畫面代替。
