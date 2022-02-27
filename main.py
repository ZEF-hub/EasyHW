# from bs4 import BeautifulSoup
# from fake_useragent import UserAgent
# from requests import Session, post
#
# session = Session()
# url_auth = 'https://login.mos.ru'
# url_auth_ref = 'https://login.mos.ru/sps/login/methods/password'
# url_get = 'https://www.mos.ru/visit/gibddlicense/reserve/?reasonId=26'
# user = UserAgent().random
#
# header = {
#     'user-agent': user
# }
#
# data = {
#     'login': '',
#     'password': ''
# }
# response = session.get(url_auth_ref)
# response = session.post(url_auth, data=data, headers=header)
# response = session.post(url_get).text
# print(response)








import requests, json
url_auth = 'https://login.mos.ru'
url_auth_ref = 'https://login.mos.ru/sps/login/methods/password'
url_get = 'https://dnevnik.mos.ru/diary/diary/homeworks'
link = 'https://dnevnik.mos.ru/core/api/student_homeworks?'
login = ''
password = ''

s = requests.Session()
r = s.get(url_auth_ref)
headers = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:96.0) Gecko/20100101 Firefox/96.0'}
data = {'login':login, 'password': password}

d = s.post(url_auth, data=data, headers=headers)

dd = s.get(url_get)
print(dd.text)


rq = s.get(link, data=data, headers=headers)
print(rq)
# with open('data.json', 'w') as f:
#     json.dump(rq, f)