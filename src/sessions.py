import requests
from fake_useragent import UserAgent

session_1 = requests.Session()
session_2 = requests.Session()

user_agent = UserAgent().random

update_cookies_called = False
get_script_info_called = False