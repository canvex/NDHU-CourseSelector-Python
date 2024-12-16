# config.py
from datetime import datetime, timedelta

target_time = datetime(2024, 12, 18, 12, 30, 0)
start_time = target_time - timedelta(minutes=3)  # 提前3分鐘登入選課系統

# 選課
sele_course_url = "https://sys.ndhu.edu.tw/AA/CLASS/subjselect/course_sele.ashx"
# 查預選課表
search_course_url = "https://sys.ndhu.edu.tw/AA/CLASS/subjselect/course_sele.aspx"

# 設定重試次數
MAX_RETRIES = 50
# 重試頻率(單位:秒)
RETRY_RATE = 0.1

# 請求的類型 1正式選課 2預選 3正式退課 4預選退選
SELE_MODE = 1
