import requests
import concurrent.futures
import time
from datetime import datetime
import courseUtils
from config import sele_course_url, MAX_RETRIES, RETRY_RATE, SELE_MODE
import threading
import sys

# 設定重試次數


# print(f"0現在時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")


def send_selection_request(course_id, session, token):

    # thread_id = threading.get_ident()
    # print(f"{datetime.now()} - Thread ID: {thread_id} - Start processing Course ID: {course_id}")
    # print(f"3現在時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    payload = {
        "type": SELE_MODE,       # 請求的類型 1正式選課 2預選 3正式退課 4預選退選
        "x": token,      # 沒什麼用，亂填也可以
        "no": course_id  # 課程 ID
    }

    for attempt in range(MAX_RETRIES):
        try:
            response = session.post(sele_course_url, data=payload)
            response.raise_for_status()

            response_data = response.json()
            # print(response_data)
            msg = response_data.get("msg")
            s_name = ""
            e_name = ""
            if SELE_MODE == 1:
                s_name = response_data.get("subj_data")["s_name"]  # 中文課名
                e_name = response_data.get("subj_data")["e_name"]  # 英文課名

            if msg == 1:
                print(
                    f"{datetime.now()}\t {course_id}\t {s_name}\t {e_name} operation successfully.")
                return True
            else:
                print(
                    f"{datetime.now()}\t {course_id}\t failed with code {msg} Retrying... ({attempt+1}/{MAX_RETRIES})")
        except requests.RequestException as e:
            print(
                f"{datetime.now()}\t Request error for Course ID {course_id}: {e}. Retrying... ({attempt+1}/{MAX_RETRIES})")

        time.sleep(RETRY_RATE)

    print(f"{datetime.now()}\t Course ID {course_id} failed after {MAX_RETRIES} attempts.")
    return False


def StartSelect(session, token):
    print("開始執行選課操作 "+str(datetime.now()))
    with open("courseID.txt", "r") as file:
        course_ids = file.read().splitlines()
    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        # print(f"2現在時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        futures = [executor.submit(send_selection_request, course_id, session, token)
                   for course_id in course_ids]

        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
            except Exception as e:
                print(f"An error occurred: {e}")
    input("程式結束，請至選課系統確認! (Press Enter to leave) "+str(datetime.now()))
    sys.exit(0)


if __name__ == "__main__":
    # print(f"1現在時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    session, viewstate, token, myname = courseUtils.getData()
    StartSelect(session, token)
