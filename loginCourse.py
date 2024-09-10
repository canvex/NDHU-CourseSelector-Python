from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import time
from datetime import datetime


def login(stdid, stdpwd):
    print(f"現在時間: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    driver = webdriver.Chrome()
    url = "https://sys.ndhu.edu.tw/AA/CLASS/subjselect/Default.aspx"
    driver.get(url)
    time.sleep(2)

    username_input = driver.find_element(By.ID, "ContentPlaceHolder1_ed_StudNo")
    password_input = driver.find_element(By.ID, "ContentPlaceHolder1_ed_pass")
    username_input.send_keys(stdid)
    password_input.send_keys(stdpwd)

    login_button = driver.find_element(By.ID, "ContentPlaceHolder1_BtnLoginNew")
    login_button.click()

    time.sleep(2)

    try:
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
    except Exception as e:
        print(f"處理 alert 時發生錯誤: {e}")

    # 儲存 cookie
    cookies = driver.get_cookies()
    with open("cookies.pkl", "wb") as f:
        pickle.dump(cookies, f)

    driver.quit()


if __name__ == "__main__":
    login("yourstudentid", "yourpwd")
