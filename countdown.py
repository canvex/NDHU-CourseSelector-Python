from datetime import datetime, timedelta
import time
import sys


def countdown_timer(target_time, callback):
    # 設定提前開始的時間 (2秒前)
    start_time = target_time - timedelta(seconds=2)
    endDate = target_time+timedelta(days=7)
    now = datetime.now()
    total_wait_time = (start_time - now).total_seconds()
    if now > endDate:
        print(f"超出選課時間!\n選課時間為{target_time.strftime('%Y-%m-%d')} 到 {endDate.strftime('%Y-%m-%d')}")
        sys.exit()
    else:
        if now < start_time:
            print(
                f"程式將在 {start_time} 開始執行，剩餘 {total_wait_time:.0f} 秒... 目前 {now.strftime('%Y-%m-%d %H:%M:%S')}")
            elapsed_time = 0

            while now < start_time:
                remaining_time = (start_time - now).total_seconds()

                if elapsed_time >= 10:
                    print(
                        f"程式將在 {start_time} 開始執行，剩餘 {remaining_time:.0f} 秒... 目前 {now.strftime('%Y-%m-%d %H:%M:%S')}")
                    elapsed_time = 0

                time.sleep(0.5)
                elapsed_time += 0.5
                now = datetime.now()
            callback()
        else:
            print(f"程式將在 {now.strftime('%Y-%m-%d %H:%M:%S')} 開始執行")
            callback()
