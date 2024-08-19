from countdown import countdown_timer
from config import start_time
from loginCourse import login
from findCourse import find_courses

# 填寫登入帳號密碼
stdid = input("Your Student ID: ")
stdpwd = input("Your password: ")

countdown_timer(start_time, lambda: login(stdid, stdpwd))
find_courses()
