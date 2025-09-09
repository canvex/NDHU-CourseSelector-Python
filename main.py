import logging
import os
from datetime import datetime
from countdown import countdown_timer
from config import start_time
from loginCourse import login
from findCourse import find_courses

# 建立 log 資料夾
log_dir = "logs"
os.makedirs(log_dir, exist_ok=True)

# 每次執行產生一個新的 log 檔（檔名含日期時間）
log_filename = datetime.now().strftime("%Y%m%d_%H%M%S.log")
log_path = os.path.join(log_dir, log_filename)

# 設定 logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    handlers=[
        logging.FileHandler(log_path, encoding="utf-8"),  # 寫檔
        logging.StreamHandler()  # 同時印到 CMD
    ]
)

logger = logging.getLogger(__name__)

# 填寫登入帳號密碼

stdid = input("Your Student ID: ")
stdpwd = input("Your password: ")

countdown_timer(start_time, lambda: login(stdid, stdpwd))
find_courses()
