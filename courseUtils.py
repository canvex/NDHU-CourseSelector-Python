import requests
import pickle
from bs4 import BeautifulSoup
from config import search_course_url


def getData(cookie_file="cookies.pkl"):
    session = requests.Session()
    with open(cookie_file, "rb") as f:
        cookies = pickle.load(f)
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
        # print(cookie)
    session.headers['User-Agent'] = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/128.0.0.0 Safari/537.36'
    get_response = session.get(search_course_url)
    soup = BeautifulSoup(get_response.text, 'html.parser')
    myname = soup.find('span', id='ContentPlaceHolder1_Label1').text
    viewstate = soup.select_one("input#__VIEWSTATE")['value']
    token = ""
    element = soup.select_one("input#ContentPlaceHolder1_hdn_msg")
    if element and 'value' in element.attrs:
        token = element['value']
    return session, viewstate, token, myname


if __name__ == "__main__":
    getData()
