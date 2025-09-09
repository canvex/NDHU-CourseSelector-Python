from selenium import webdriver
from selenium.webdriver.common.by import By
import pickle
import time
from selenium.webdriver.chrome.options import Options
import logging
logger = logging.getLogger(__name__)


def login(stdid, stdpwd):
    logger.info(f"開始執行登入")

    options = Options()
    options.add_argument("--headless")  # 如果想要隱藏瀏覽器可以開啟這個

    driver = webdriver.Chrome()
    url = "https://sys.ndhu.edu.tw/AA/CLASS/subjselect/Default.aspx"
    driver.get(url)
    time.sleep(2)

    username_input = driver.find_element(
        By.ID, "ContentPlaceHolder1_ed_StudNo")
    password_input = driver.find_element(By.ID, "ContentPlaceHolder1_ed_pass")
    username_input.send_keys(stdid)
    password_input.send_keys(stdpwd)

    login_button = driver.find_element(
        By.ID, "ContentPlaceHolder1_BtnLoginNew")
    login_button.click()

    time.sleep(2)

    try:
        alert = driver.switch_to.alert
        alert.accept()
        time.sleep(2)
    except Exception as e:
        logger.error(f"處理 alert 時發生錯誤: {e}")

    # 儲存 cookie
    cookies = driver.get_cookies()
    with open("cookies.pkl", "wb") as f:
        pickle.dump(cookies, f)

    driver.quit()
    logger.info("cookies紀錄完成 ")


if __name__ == "__main__":
    login("yourstudentid", "yourpwd")
