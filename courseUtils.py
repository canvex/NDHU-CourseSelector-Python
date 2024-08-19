import requests
import pickle
from bs4 import BeautifulSoup
from config import search_course_url


def get_session(cookie_file="cookies.pkl"):
    session = requests.Session()
    with open(cookie_file, "rb") as f:
        cookies = pickle.load(f)
    for cookie in cookies:
        session.cookies.set(cookie['name'], cookie['value'])
        # print(cookie)
    return session


def getData():
    session = get_session()
    get_response = session.get(search_course_url)
    soup = BeautifulSoup(get_response.text, 'html.parser')
    myname = soup.find('span', id='ContentPlaceHolder1_Label1').text
    viewstate = soup.select_one("input#__VIEWSTATE")['value']
    token = ""
    element = soup.select_one("input#ContentPlaceHolder1_hdn_msg")
    if element and 'value' in element.attrs:
        token = element['value']
    return viewstate, token, myname


if __name__ == "__main__":
    get_session()
