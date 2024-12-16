from bs4 import BeautifulSoup
from seleCourse import StartSelect
import courseUtils
from datetime import datetime
from countdown import countdown_timer
from config import target_time, search_course_url
import sys


def find_courses():
    print("開始查詢預選課表 "+str(datetime.now()))
    session, viewstate, token, myname = courseUtils.getData()
    payload = {
        "__VIEWSTATE": viewstate,
        "ctl00$ContentPlaceHolder1$Button7": "查詢預排課程"
    }
    post_response = session.post(search_course_url, data=payload)
    if post_response.status_code == 200:
        post_soup = BeautifulSoup(post_response.text, 'html.parser')
        # 找到選課資料的表格
        table = post_soup.find(
            "table", {"id": "ContentPlaceHolder1_grd_subjs"})
        print(myname)
        if table:
            seen_ids = set()
            count = 0
            print("你的預選課程:\n")
            with open("courseID.txt", "w", encoding="utf-8") as file:
                for td in table.find_all("td"):
                    a_tag = td.find("a", {"id": True})
                    if a_tag:
                        course_id = a_tag['id'][1:]
                        if course_id not in seen_ids:
                            count += 1
                            file.write(f"{course_id}\n")
                            seen_ids.add(course_id)
                            print(course_id)
            print(f"\n共{count}筆課程\n")
        else:
            print("錯誤! 未找到選課資料表格。")
            sys.exit()
    else:
        print(
            f"Failed to retrieve the page. Status code: {post_response.status_code}")
        sys.exit()
    print("預選課表查詢完成 "+str(datetime.now()))
    countdown_timer(target_time, lambda: StartSelect(session, token))


if __name__ == "__main__":
    find_courses()
