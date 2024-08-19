import requests
import concurrent.futures
import time
from datetime import datetime
import courseUtils
from config import sele_course_url
import threading
import sys

# 設定重試次數
MAX_RETRIES = 3

session = courseUtils.get_session()


with open("courseID.txt", "r") as file:
    course_ids = file.read().splitlines()


def send_selection_request(course_id, token):
    # thread_id = threading.get_ident()
    # print(f"{datetime.now()} - Thread ID: {thread_id} - Start processing Course ID: {course_id}")

    payload = {
        "type": 2,      # 請求的類型 1正式選課 2預選 4退選
        "x": token,
        "no": course_id  # 課程 ID
    }

    for attempt in range(MAX_RETRIES):
        try:
            response = session.post(sele_course_url, data=payload)
            response.raise_for_status()

            response_data = response.json()
            msg = response_data.get("msg")

            if msg == 1:
                print(
                    f"{datetime.now()} - Course ID {course_id} selected successfully.")
                return True
            else:
                print(
                    f"{datetime.now()} - Course ID {course_id} failed with code {msg} Retrying... ({attempt+1}/{MAX_RETRIES})")
        except requests.RequestException as e:
            print(
                f"{datetime.now()} - Request error for Course ID {course_id}: {e}. Retrying... ({attempt+1}/{MAX_RETRIES})")

        time.sleep(1)

    print(f"{datetime.now()} - Course ID {course_id} failed after {MAX_RETRIES} attempts.")
    return False


def StartSelect(token):
    with concurrent.futures.ThreadPoolExecutor(max_workers=15) as executor:
        futures = [executor.submit(send_selection_request, course_id, token)
                   for course_id in course_ids]

        for future in concurrent.futures.as_completed(futures):
            try:
                result = future.result()
            except Exception as e:
                print(f"An error occurred: {e}")
    sys.exit("程式結束，請至選課系統確認!")


if __name__ == "__main__":
    StartSelect("")
