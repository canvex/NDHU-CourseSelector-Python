# config.py
from datetime import datetime, timedelta

target_time = datetime(2024, 8, 18, 21, 26, 45)
start_time = target_time - timedelta(minutes=3)  # 提前3分鐘進系統

# 選課
sele_course_url = "https://sys.ndhu.edu.tw/AA/CLASS/subjselect/course_sele.ashx"
# 查預選課表
search_course_url = "https://sys.ndhu.edu.tw/AA/CLASS/subjselect/course_sele.aspx"
