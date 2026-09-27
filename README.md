# NDHU CourseSelector

國立東華大學選課輔助程式。程式會在指定時間登入選課系統，讀取帳號中的**預排課程**，並在正式選課時間對這些課程送出選課請求。執行後仍須自行登入學校選課系統確認結果。

## 環境需求&建置

- Windows
- Python 3，[官方下載網站](https://www.python.org/downloads/)
- [Microsoft Edge](https://www.microsoft.com/edge/download)

在 **PowerShell** 中依序執行
```powershell
cd /path/to/NDHU-CourseSelector-Python
pip install -r requirements.txt
```

接著完成以下準備：

1. 先到學校選課系統登入，確認要選的課程已加入**預排課程**。程式會在執行時重新產生 `courseID.txt`，所以不需要手動修改這個檔案。
2. 開啟 `config.py`，把 `target_time` 改成**本次正式選課開始的日期與時間**，格式為 `datetime(年, 月, 日, 時, 分, 秒)`。`start_time` 預設比 `target_time` 早 3 分鐘，用來登入與讀取預排課程；請確認電腦時間正確，並在 `start_time` 前啟動程式。
3. 在 Edge 開啟 `edge://settings/help` 查看版本。專案附帶的 `msedgedriver.exe` 版本為 **140.0.3485.54**；若與 Edge 的前三段版本號不同，請從 [Microsoft Edge WebDriver 官方下載頁](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver)下載對應的 Windows 版本，解壓後取代專案根目錄的 `msedgedriver.exe`。

從專案根目錄執行：

```powershell
python main.py
```

依提示輸入學號及密碼。程式會等到 `start_time` 登入，將登入 Cookie 儲存在 `cookies.pkl`，查詢預排課程並寫入 `courseID.txt`；到 `target_time` 後依清單送出選課請求。畫面及 `logs/` 中會顯示執行紀錄。執行結束時按 Enter 離開，**最後請到學校系統核對選課結果**。`cookies.pkl` 是登入憑證，請勿分享。

> 如果在 `start_time` 之後、`target_time` 之前啟動，程式會立即登入並查詢預排課程；如果 `target_time` 已超過 7 天，程式會直接結束。
